

# Broad Steps to Work with MySQL and Python

## 1) Install MySQL

First, make sure **MySQL Server** is installed on your system.

You should have:

* MySQL Server
* MySQL Workbench (optional but useful)
* a database created for practice

Example database:

```sql
CREATE DATABASE college_db;
```

---

## 2) Install MySQL connector in Python

Python needs a package to talk to MySQL.

Install:

```bash
pip install mysql-connector-python
```

This lets Python connect to MySQL.

---

## 3) Import the connector in Python

In your Python program:

```python
import mysql.connector
```

---

## 4) Establish connection to MySQL

Use host, username, password, and database name.

Example:

```python
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="college_db"
)
```

If connection is successful, Python can now talk to MySQL.

---

## 5) Create a cursor object

Cursor is used to send SQL commands from Python to MySQL.

```python
cur = con.cursor()
```

---

## 6) Execute SQL queries

Use `execute()` to run SQL commands.

Examples:

### Create table

```python
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    marks INT
)
""")
```

### Insert data

```python
cur.execute("INSERT INTO student VALUES (101, 'Aarav', 'Python', 85)")
```

### Select data

```python
cur.execute("SELECT * FROM student")
rows = cur.fetchall()
```

---

## 7) Commit the changes

If you do **INSERT / UPDATE / DELETE**, save changes using:

```python
con.commit()
```

Without commit, changes may not be stored permanently.

---

## 8) Fetch records

For SELECT queries, fetch the result.

### Fetch all rows

```python
rows = cur.fetchall()
for row in rows:
    print(row)
```

### Fetch one row

```python
row = cur.fetchone()
print(row)
```

---

## 9) Close connection

Always close database connection after work is done.

```python
con.close()
```

---

# Full Flow in One Line

### Python + MySQL workflow:

**Install connector → Import package → Connect to MySQL → Create cursor → Execute SQL → Commit if needed → Fetch records → Close connection**

---

# Simple Example Structure

```python
import mysql.connector

# 1. connect
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="college_db"
)

# 2. create cursor
cur = con.cursor()

# 3. execute query
cur.execute("SELECT * FROM student")

# 4. fetch data
rows = cur.fetchall()
for row in rows:
    print(row)

# 5. close connection
con.close()
```

---

# Typical Operations You Can Perform

Once Python is connected to MySQL, you can do:

## CREATE

Create tables

## INSERT

Add new records

## SELECT

Read records

## UPDATE

Modify records

## DELETE

Remove records

So essentially, Python can perform **CRUD operations** on MySQL.

---

# Broad classroom explanation

If you want to explain it to students in plain words:

### Step 1

MySQL stores the data.

### Step 2

Python connects to MySQL using a connector.

### Step 3

Python sends SQL queries through a cursor.

### Step 4

MySQL executes those queries.

### Step 5

Python reads the result and displays it.

---

# Good teaching order

I’d teach it in this order:

## Program 1

**Connect Python to MySQL**

## Program 2

**Create table using Python**

## Program 3

**Insert one record**

## Program 4

**Insert user-entered record**

## Program 5

**Fetch and display records**

## Program 6

**Update record**

## Program 7

**Delete record**
