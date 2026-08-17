# bcrypt in Python — A Student Reading Guide

## 1. What is bcrypt?

**bcrypt** is a password-hashing algorithm designed specifically for securely storing passwords.

The basic idea is:

```text
User Password
      ↓
    bcrypt
      ↓
Password Hash
      ↓
Store the Hash
```

For example:

```python
import bcrypt

password = "hello123"

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print(hashed)
```

Output may look like:

```text
b'$2b$12$K8kL...'
```

The output is **not the original password**.

---

# 2. Installing bcrypt

Install it using:

```bash
pip install bcrypt
```

Then import it:

```python
import bcrypt
```

---

# 3. `bcrypt.gensalt()`

### Purpose

`gensalt()` generates a **salt** that is used when creating the password hash.

```python
salt = bcrypt.gensalt()

print(salt)
```

Example:

```text
b'$2b$12$N9qo8uLOickgx2ZMRZoMye'
```

You normally don't need to manually create or manage the salt.

You simply do:

```python
hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)
```

### Why is salt important?

Suppose two users have the same password:

```text
Rahul → hello123
Priya → hello123
```

Without salting, they could potentially end up with the same hash.

With bcrypt:

```text
hello123 → Hash A
hello123 → Hash B
```

The hashes are different because different salts are used.

---

# 4. `bcrypt.hashpw()`

This is the main function used to **create a password hash**.

Syntax:

```python
bcrypt.hashpw(password, salt)
```

Example:

```python
password = "hello123"

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print(hashed)
```

### Breaking it down

```python
password.encode()
```

converts the Python string into bytes.

For example:

```text
"hello123"
       ↓
b"hello123"
```

bcrypt works with bytes.

Then:

```python
bcrypt.gensalt()
```

generates a random salt.

Finally:

```python
bcrypt.hashpw(...)
```

creates the hash.

---

# 5. `bcrypt.checkpw()`

This function is used to **verify a password**.

Syntax:

```python
bcrypt.checkpw(password, hashed_password)
```

Example:

```python
password = "hello123"

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

if bcrypt.checkpw(password.encode(), hashed):
    print("Correct password")
else:
    print("Wrong password")
```

Output:

```text
Correct password
```

---

## What happens internally?

Suppose the stored hash is:

```text
$2b$12$....................
```

The user enters:

```text
hello123
```

bcrypt does not simply compare:

```text
"hello123" == "$2b$12$..."
```

Instead, `checkpw()` uses information contained in the stored hash, including its salt and cost parameters, to hash the supplied password and determine whether it matches.

```text
Entered Password
       ↓
   bcrypt
       ↓
Compare with stored hash
       ↓
   ┌───┴───┐
   ↓       ↓
 True    False
   ↓       ↓
Correct   Wrong
```

---

# 6. Why `checkpw()` is important

A common beginner question is:

> "If we don't store the original password, how can we know whether the user entered the correct password?"

That's exactly what `checkpw()` solves.

We store:

```text
Username → Password Hash
```

not:

```text
Username → Password
```

During login:

```text
User enters password
        ↓
checkpw()
        ↓
Stored Hash
        ↓
True / False
```

---

# 7. `bcrypt.hashpw()` Does NOT Produce the Same Hash Every Time

This is a very important experiment for students.

Run:

```python
import bcrypt

password = "hello123"

hash1 = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

hash2 = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

print(hash1)
print(hash2)
```

You will get two different hashes.

For example:

```text
Hash 1:
b'$2b$12$ABC................'

Hash 2:
b'$2b$12$XYZ................'
```

Even though:

```text
Password 1 = hello123
Password 2 = hello123
```

the hashes are different.

### Why?

Because:

```python
bcrypt.gensalt()
```

generates a new random salt.

---

# 8. But Both Passwords Still Verify

This is the interesting part.

```python
print(
    bcrypt.checkpw(
        password.encode(),
        hash1
    )
)
```

Output:

```text
True
```

And:

```python
print(
    bcrypt.checkpw(
        password.encode(),
        hash2
    )
)
```

also gives:

```text
True
```

So:

```text
Same Password
     ↓
Different Hashes
     ↓
Both Can Be Verified
```

---

# 9. What if the Password is Wrong?

```python
wrong_password = "hello456"

result = bcrypt.checkpw(
    wrong_password.encode(),
    hash1
)

print(result)
```

Output:

```text
False
```

Therefore:

```python
bcrypt.checkpw(
    b"hello123",
    hash1
)
```

→ `True`

while:

```python
bcrypt.checkpw(
    b"hello456",
    hash1
)
```

→ `False`

---

# 10. `bcrypt.gensalt()` and Work Factor

You may see:

```python
bcrypt.gensalt(rounds=12)
```

Example:

```python
salt = bcrypt.gensalt(rounds=12)
```

The `rounds` parameter controls the **computational cost** of the hashing operation.

For example:

```python
bcrypt.gensalt(rounds=10)
```

versus:

```python
bcrypt.gensalt(rounds=12)
```

A higher cost makes password hashing more computationally expensive.

That's intentional.

### Why make it slow?

Attackers may try millions of password guesses.

A password-hashing algorithm should make each guess relatively expensive.

```text
Fast hashing
    ↓
Attacker can try many guesses quickly
    ↓
Bad


Slower password hashing
    ↓
Each guess costs more
    ↓
Better resistance to brute-force attacks
```

The appropriate work factor depends on the environment and should be chosen based on current security guidance and acceptable server performance.

---

# 11. Understanding the bcrypt Hash

A bcrypt hash commonly looks like:

```text
$2b$12$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
```

It contains information used by bcrypt to perform verification.

Conceptually:

```text
$2b$12$....................
 │   │
 │   └── Cost / work factor
 │
 └────── bcrypt version
```

The remaining portion contains the salt and derived hash information.

**Important:** Don't think of the hash as simply "the encrypted password."

It is a **password hash representation** containing the information bcrypt needs for verification.

---

# 12. Hashing vs Encryption

This distinction is extremely important.

### Encryption

Encryption is designed to be reversible when you have the appropriate key.

```text
Original Data
     ↓
 Encryption
     ↓
Encrypted Data
     ↓
 Decryption
     ↓
Original Data
```

### Password Hashing

Password hashing is designed for verification rather than recovering the original password.

```text
Password
    ↓
 Hashing
    ↓
Hash
```

There isn't a normal:

```text
Hash → Original Password
```

operation.

---

# 13. Complete bcrypt Example

Here is a small standalone example combining the important functions:

```python
import bcrypt

# Original password
password = "hello123"

# Generate salt
salt = bcrypt.gensalt()

# Generate hash
hashed_password = bcrypt.hashpw(
    password.encode(),
    salt
)

print("Password:", password)
print("Hash:", hashed_password)


# Correct password
entered_password = "hello123"

if bcrypt.checkpw(
    entered_password.encode(),
    hashed_password
):
    print("Correct password")
else:
    print("Wrong password")


# Wrong password
entered_password = "hello456"

if bcrypt.checkpw(
    entered_password.encode(),
    hashed_password
):
    print("Correct password")
else:
    print("Wrong password")
```

Expected output conceptually:

```text
Password: hello123

Hash:
$2b$12$..........................

Correct password

Wrong password
```

---

# 14. The Three Functions Students Should Remember

For a beginner, these are the important ones:

| Function           | Purpose                          |
| ------------------ | -------------------------------- |
| `bcrypt.gensalt()` | Generate a random salt           |
| `bcrypt.hashpw()`  | Create a password hash           |
| `bcrypt.checkpw()` | Verify a password against a hash |

Think:

```text
gensalt()
   ↓
hashpw()
   ↓
Store Hash
   ↓
checkpw()
   ↓
True / False
```

---

# 15. How This Fits into Flask

In a real Flask registration system:

```python
password = request.form["password"]

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

# Store hashed in database
```

During login:

```python
password = request.form["password"]

if bcrypt.checkpw(
    password.encode(),
    stored_hash
):
    print("Login successful")
```

So the complete real-world flow is:

```text
                 REGISTER
                    │
                    ▼
             User Password
                    │
                    ▼
             bcrypt.hashpw()
                    │
                    ▼
             Password Hash
                    │
                    ▼
                DATABASE
                    │
                    │
                    ▼
                  LOGIN
                    │
                    ▼
             Entered Password
                    │
                    ▼
            bcrypt.checkpw()
                    │
              ┌─────┴─────┐
              ▼           ▼
            True        False
              │           │
              ▼           ▼
           Login        Reject
```

### One sentence to remember

> **bcrypt doesn't store the password; it creates a salted, deliberately expensive hash that can later be used to verify whether a supplied password is correct.**
