`cy.session()` is one of the most useful Cypress features for writing **fast, reliable, and scalable** test suites. It avoids logging in before every test by caching and restoring authenticated sessions.

---

# Session Objective (45-60 mins)

By the end of the session, students should understand:

* Why repeated logins slow tests
* What `cy.session()` does
* How Cypress stores sessions
* Creating reusable login sessions
* Validating sessions
* Real-world implementation

---

# Teaching Flow

## 1. The Problem (5 mins)

Ask students:

> "Imagine you have 50 test cases. Every test logs into the application first."

Example:

```javascript
it("Test 1", () => {
    login()
})

it("Test 2", () => {
    login()
})

it("Test 3", () => {
    login()
})

...
```

Ask:

> How many times are we logging in?

Students:

> 50

Then ask:

> Is login our test?

No.

We're wasting time testing login repeatedly.

---

## Explain

Every login

* opens login page
* types username
* types password
* waits
* authenticates
* redirects

Even though nothing changes.

---

# Real World Analogy

Imagine entering a college.

Security checks your ID once.

You receive a visitor badge.

Would security verify your ID every time you enter another classroom?

No.

The badge proves you are already authenticated.

`cy.session()` is that visitor badge.

---

# 2. Without cy.session() (10 mins)

Example

```javascript
describe("Products", () => {

    beforeEach(() => {

        cy.visit("/login")

        cy.get("#username").type("admin")

        cy.get("#password").type("admin123")

        cy.get("#loginBtn").click()

    })

    it("Open Dashboard", () => {

    })

    it("Open Reports", () => {

    })

    it("Open Users", () => {

    })

})
```

Ask:

How many logins?

Answer:

Three.

---

# Explain Timeline

```
Test 1

Visit Login
↓

Enter Username

↓

Enter Password

↓

Login

↓

Dashboard


---------------------------

Test 2

Visit Login

↓

Enter Username

↓

Enter Password

↓

Login

↓

Reports


---------------------------

Test 3

Again...
```

Students immediately notice the repetition.

---

# 3. Introduce cy.session() (10 mins)

Syntax

```javascript
cy.session(id, setupFunction)
```

Example

```javascript
cy.session("admin", () => {

    cy.visit("/login")

    cy.get("#username").type("admin")

    cy.get("#password").type("admin123")

    cy.get("#loginBtn").click()

})
```

Explain

```
admin
↓

Session Name

↓

Stored

↓

Reuse Later
```

---

# 4. Convert Previous Example

Without session

```javascript
beforeEach(() => {

    cy.visit("/login")

    cy.get("#username").type("admin")

    cy.get("#password").type("admin123")

    cy.get("#loginBtn").click()

})
```

Replace with

```javascript
beforeEach(() => {

    cy.session("admin", () => {

        cy.visit("/login")

        cy.get("#username").type("admin")

        cy.get("#password").type("admin123")

        cy.get("#loginBtn").click()

    })

})
```

---

Explain

First test

```
No Session

↓

Login

↓

Save Session
```

Second test

```
Session Exists

↓

Restore Session

↓

Skip Login
```

---

# 5. Complete Example (15 mins)

Using DemoBlaze

```javascript
describe("Products", () => {

    beforeEach(() => {

        cy.session("testuser", () => {

            cy.visit("/")

            cy.contains("Log in").click()

            cy.get("#loginusername").type("testuser")

            cy.get("#loginpassword").type("password123")

            cy.contains("button", "Log in").click()

            cy.contains("Welcome").should("be.visible")

        })

        cy.visit("/")

    })

    it("Open Phones", () => {

        cy.contains("Phones").click()

    })

    it("Open Laptops", () => {

        cy.contains("Laptops").click()

    })

    it("Open Monitors", () => {

        cy.contains("Monitors").click()

    })

})
```

---

# Important Point

Students often ask:

> If session is restored, why do we still call `cy.visit("/")`?

Because the session restores authentication data (cookies, local storage, etc.), **not the page itself**. After restoring the session, you still need to navigate to the page where the test should begin.

---

# 6. Validation (Very Important)

Without validation

```javascript
cy.session("admin", () => {

    login()

})
```

Better

```javascript
cy.session("admin", () => {

    login()

},
{
    validate() {

        cy.visit("/dashboard")

        cy.contains("Welcome")

    }
})
```

Explain

If session expires,

Cypress automatically performs login again.

---

# 7. Multiple Users

Admin

```javascript
cy.session("admin", () => {

    login("admin", "admin123")

})
```

Manager

```javascript
cy.session("manager", () => {

    login("manager", "manager123")

})
```

Employee

```javascript
cy.session("employee", () => {

    login("employee", "employee123")

})
```

One command

Different cached sessions.

---

# 8. Best Practice - Custom Command

`commands.js`

```javascript
Cypress.Commands.add("loginSession", (username, password) => {

    cy.session(username, () => {

        cy.visit("/login")

        cy.get("#username").type(username)

        cy.get("#password").type(password)

        cy.get("#loginBtn").click()

        cy.contains("Welcome").should("be.visible")

    })

})
```

Usage

```javascript
beforeEach(() => {

    cy.loginSession("admin", "admin123")

    cy.visit("/dashboard")

})
```

Much cleaner.

---

# 9. How Cypress Thinks (Visualization)

```
Test Starts

      │

      ▼

Session Exists?

 ┌──────────────┐
 │      No      │
 └──────────────┘
        │
        ▼
Login
        │
        ▼
Save Session
        │
        ▼
Run Test


Next Test

        │
        ▼

Session Exists?

 ┌──────────────┐
 │     Yes      │
 └──────────────┘
        │
        ▼
Restore Session
        │
        ▼
Run Test
```

---

# 10. Advantages

| Without `cy.session()`  | With `cy.session()`           |
| ----------------------- | ----------------------------- |
| Logs in every test      | Logs in only once per session |
| Slower execution        | Faster execution              |
| More network traffic    | Less network traffic          |
| Repeated authentication | Session reused                |
| More maintenance        | Cleaner code                  |

---

# Common Interview Questions

### Q1. What does `cy.session()` do?

It caches and restores the browser session (such as cookies and storage) so repeated login steps can be skipped.

---

### Q2. Does it store screenshots?

No.

---

### Q3. Does it cache browser cookies?

Yes.

---

### Q4. Does it cache Local Storage?

Yes.

---

### Q5. Does it skip visiting pages?

No. You still need to call `cy.visit()` after restoring the session.

---

### Q6. Why is it faster?

Because Cypress restores the saved authenticated session instead of executing the login workflow before every test.

---

# Mini Lab (10 minutes)

**Scenario:** You are testing an HR portal with three authenticated tests.

1. Create a reusable `loginSession()` custom command.
2. Cache the session for the user `hradmin`.
3. Use the session in three tests:

   * View Employees
   * Add Employee
   * View Reports
4. Verify that the login steps execute only once while all three tests start in an authenticated state.

This exercise helps students experience the performance benefit of `cy.session()` firsthand and reinforces how to organize reusable authentication logic in real-world Cypress projects.
