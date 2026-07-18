# MOCK API

This topic naturally follows **`cy.intercept()`** because students already know how to **observe** network traffic. Now they'll learn how to **replace** the backend entirely.

A 1-hour session should focus on the idea that **"Instead of calling the real server, Cypress can pretend to be the server."**

---

# API Mocking using `cy.intercept()` and Fixtures

## Learning Objectives

By the end of this session, students will be able to:

* Explain what API Mocking is.
* Understand why mocking is useful.
* Create fixture files.
* Return mock responses using `cy.intercept()`.
* Test applications without a real backend.
* Simulate different backend scenarios (success, error, empty data).

---

# 1. What is API Mocking?

Imagine your frontend application normally communicates with a backend server.

```
Frontend
     │
HTTP Request
     │
     ▼
Backend Server
     │
HTTP Response
     │
     ▼
Frontend Updates Screen
```

Normally, every button click sends a request to the backend.

But what happens if

* backend is down?
* backend is still under development?
* internet is unavailable?
* API returns inconsistent data?

Testing becomes difficult.

---

## API Mocking Definition

> **API Mocking is the process of replacing a real backend response with a fake response so the application can be tested independently of the server.**

Instead of contacting the real server,

Cypress itself returns the response.

---

# 2. Real API vs Mock API

### Real API

```
Application

↓

GET /users

↓

Real Server

↓

Database

↓

Real Response
```

---

### Mock API

```
Application

↓

GET /users

↓

Cypress intercepts request

↓

Returns Fake Response

↓

Application receives fake data
```

Notice:

The server is never contacted.

---

# 3. Why Use API Mocking?

## Reason 1 – Backend Not Ready

Frontend developers usually begin before backend development is complete.

Mock APIs allow UI development to continue.

---

## Reason 2 – Faster Tests

Real API

```
Browser

↓

Internet

↓

Server

↓

Database

↓

Response
```

May take 2–5 seconds.

Mock API

```
Browser

↓

Cypress

↓

Fake Response
```

Usually finishes in milliseconds.

---

## Reason 3 – Stable Tests

Real APIs may

* change data
* become unavailable
* timeout
* become slow

Mock data never changes.

---

## Reason 4 – Test Rare Scenarios

Suppose you want to test

```
500 Internal Server Error

404 Not Found

Empty Data

Unauthorized User
```

A real server may not easily produce these responses.

Mocking allows them instantly.

---

# 4. What is a Fixture?

A Fixture is simply a file containing sample data.

Usually stored here

```
cypress/

    fixtures/

        users.json

        employee.json

        products.json
```

Think of it as

> "Saved API Responses"

---

Example

users.json

```json
[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@example.com"
  },
  {
    "id": 2,
    "name": "Priya Patel",
    "email": "priya@example.com"
  }
]
```

---

# 5. Folder Structure

```
project

│

├── cypress

│      │

│      ├── e2e

│      │      mock.cy.js

│      │

│      ├── fixtures

│      │      users.json

│      │      employees.json

│      │

│      └── support
```

---

# 6. Basic Mock Syntax

```javascript
cy.intercept("GET", "/users", {
    fixture: "users.json"
})
```

Meaning

```
Whenever

GET /users

is requested,

return

users.json
```

No server is contacted.

---

# 7. Complete Example

Assume the application loads

```
GET /users
```

Create

users.json

```json
[
    {
        "id":1,
        "name":"Rahul"
    },
    {
        "id":2,
        "name":"Sneha"
    }
]
```

Now

```javascript
describe("Mock Users", () => {

    it("Loads fake users", () => {

        cy.intercept(
            "GET",
            "/users",
            {
                fixture: "users.json"
            }
        ).as("users")

        cy.visit("/")

        cy.wait("@users")

    })

})
```

The application believes

```
Backend sent data.

Actually,

Cypress did.
```

---

# 8. Returning Static JSON Without Fixture

Instead of a fixture file,

you can directly write

```javascript
cy.intercept("GET", "/users", {

    statusCode:200,

    body:[
        {
            id:1,
            name:"Amit"
        }
    ]

})
```

Useful for small responses.

---

# 9. Mocking POST Requests

Application sends

```
POST /login
```

Return success.

```javascript
cy.intercept("POST", "/login", {

    statusCode:200,

    body:{

        token:"ABC123",

        username:"Rahul"

    }

})
```

Now login succeeds even if no backend exists.

---

# 10. Mock Error Responses

Return

500 Server Error

```javascript
cy.intercept("GET", "/users", {

    statusCode:500,

    body:{

        message:"Internal Server Error"

    }

})
```

Students can now verify

```
Application displays

"Something went wrong."
```

---

# 11. Mock Empty Data

```javascript
cy.intercept("GET", "/users", {

    statusCode:200,

    body:[]

})
```

Useful for checking

```
"No Records Found"
```

---

# 12. Mock 404

```javascript
cy.intercept("GET", "/users", {

    statusCode:404,

    body:{

        message:"Not Found"

    }

})
```

---

# 13. Mock Delayed Response

Sometimes applications display

Loading...

Simulate delay.

```javascript
cy.intercept("GET", "/users", {

    delay:3000,

    fixture:"users.json"

})
```

Students can verify

```
Loading Spinner

appears

for 3 seconds.
```

---

# 14. Intercept with Alias

```javascript
cy.intercept(
    "GET",
    "/users",
    {
        fixture:"users.json"
    }
).as("users")
```

Later

```javascript
cy.wait("@users")
```

---

# 15. Verifying Mocked Response

```javascript
cy.wait("@users").then((interception)=>{

    expect(interception.response.statusCode)
        .to.equal(200)

})
```

---

# 16. Real vs Mock Comparison

| Real API                 | Mock API            |
| ------------------------ | ------------------- |
| Needs backend            | No backend required |
| Internet required        | No                  |
| Slower                   | Very fast           |
| Data changes             | Fixed data          |
| May fail                 | Stable              |
| Difficult to test errors | Easy                |

---

# 17. When Should We Mock?

Mock when

* Backend not available
* UI testing
* Edge cases
* Error handling
* Fast automated tests
* CI/CD pipelines

Use the real API when

* Testing backend functionality
* End-to-end integration
* Verifying database updates
* Validating actual API behavior

---

# 18. Real-World Example

Imagine an e-commerce website.

```
Product Page

↓

GET /products

↓

Server
```

Suppose today

* server crashes
* internet fails

Can frontend developers continue?

Yes.

They create

products.json

and mock it.

The UI behaves exactly as if products came from the server.

---

# 19. Best Practices

* Keep fixture files small and readable.
* Use meaningful names such as `users.json`, `products.json`, `orders.json`.
* Create separate fixtures for success, empty, and error cases.
* Mock only what your test needs.
* Use real APIs for full end-to-end validation and mocked APIs for fast, deterministic UI tests.

---

# Common Mistakes

### 1. Fixture name incorrect

```javascript
fixture:"user.json"
```

But file is

```
users.json
```

---

### 2. Incorrect URL

```javascript
cy.intercept("GET","/user")
```

Application calls

```
/users
```

Intercept never matches.

---

### 3. Calling `cy.intercept()` after `cy.visit()`

```javascript
cy.visit("/")

cy.intercept(...)
```

Too late—the request may already have been sent.

Correct order:

```javascript
cy.intercept(...)

cy.visit("/")
```

---

### 4. Wrong HTTP method

Application sends

```
POST
```

You intercept

```
GET
```

No interception occurs.

---

# Summary

* **API Mocking** replaces a real backend response with a fake one.
* **Fixtures** are JSON files that store sample API responses.
* `cy.intercept()` can return fixture data instead of contacting the server.
* Mocking makes tests **fast, reliable, repeatable, and independent of backend availability**.
* It is especially useful for testing **success**, **empty**, **error**, and **loading** scenarios that are difficult to reproduce with a live API.

## Practice Exercises

### Exercise 1: Mock Employee List

Create a fixture named `employees.json`:

```json
[
    {
        "id": 1,
        "name": "Ananya Rao",
        "department": "QA"
    },
    {
        "id": 2,
        "name": "Rohan Mehta",
        "department": "Development"
    }
]
```

Write a Cypress test that:

* Intercepts `GET /employees`
* Returns `employees.json`
* Waits for the request
* Verifies the status code is `200`

---

### Exercise 2: Test Empty Results

Mock:

```json
[]
```

Verify that the application displays **"No Employees Found"**.

---

### Exercise 3: Test Server Error

Mock:

```javascript
{
    statusCode: 500,
    body: {
        message: "Server Error"
    }
}
```

Verify that the application displays an appropriate error message.

---

This lesson prepares students for more advanced Cypress topics such as **modifying requests and responses dynamically**, **simulating authentication flows**, **testing loading states**, and **handling complex network conditions** using `cy.intercept()`.







Sure. Here's the simplest way to think about `cy.intercept()`.

## Imagine this situation

Your web page loads employee data.

```text
Browser ---------------------> Server
         "Give me employees"

Browser <--------------------- Server
         Employee JSON
```

This happens very quickly.

---

## Without `cy.intercept()`

Your test does this:

```javascript
cy.visit("/employees")

cy.get("table").should("be.visible")
```

Problem:

Sometimes the server is still sending the data.

The table isn't ready.

❌ Test fails.

---

## With `cy.intercept()`

First, tell Cypress:

> "Watch for the employee API."

```javascript
cy.intercept("GET", "/employees").as("employees")
```

Then visit the page.

```javascript
cy.visit("/employees")
```

Now wait for that API to finish.

```javascript
cy.wait("@employees")
```

Only then check the table.

```javascript
cy.get("table").should("be.visible")
```

---

## Think of it like ordering pizza 🍕

Without waiting:

```text
Order Pizza

↓

Immediately open the door

↓

No pizza

↓

FAIL
```

With waiting:

```text
Order Pizza

↓

Wait until delivery arrives

↓

Open the door

↓

SUCCESS
```

`cy.wait("@employees")` means:

> **"Don't continue until the employee API has finished."**

---

## The three lines you'll use most often

```javascript
cy.intercept("GET", "/employees").as("employees")

cy.visit("/employees")

cy.wait("@employees")
```

Meaning:

1. 👀 Watch the API.
2. 🌐 Open the page.
3. ⏳ Wait until the API finishes.

Then continue with your test.

---

## One-line definition for students

> **`cy.intercept()` tells Cypress to watch (or even fake) API requests made by the application. Combined with `cy.wait()`, it makes tests more reliable by waiting for the API response before continuing.**

# Example 2

Here's a simple example that students can easily understand.

### Scenario

When the user clicks the **Load Employees** button, the application calls:

```text
GET /employees
```

We want Cypress to:

1. Watch the API call.
2. Wait until it finishes.
3. Verify that employees are displayed.

```javascript
describe("Employee List", () => {

    it("Loads employees successfully", () => {

        // Watch the API request
        cy.intercept("GET", "/employees").as("getEmployees")

        // Open the application
        cy.visit("http://localhost:3000")

        // Click the button that loads employees
        cy.get("#loadEmployees").click()

        // Wait for the API to finish
        cy.wait("@getEmployees")

        // Verify the employees are displayed
        cy.get("table tbody tr")
          .should("have.length.greaterThan", 0)

    })

})
```

---

## What each line does

```javascript
cy.intercept("GET", "/employees").as("getEmployees")
```

➡️ Start watching the **GET /employees** API.

---

```javascript
cy.visit("http://localhost:3000")
```

➡️ Open the application.

---

```javascript
cy.get("#loadEmployees").click()
```

➡️ User clicks **Load Employees**.

---

```javascript
cy.wait("@getEmployees")
```

➡️ Wait until the API response comes back.

---

```javascript
cy.get("table tbody tr")
  .should("have.length.greaterThan", 0)
```

➡️ Verify that at least one employee is displayed.

---

### Flow Diagram

```text
Open Application
        │
        ▼
Start Watching API
        │
        ▼
Click "Load Employees"
        │
        ▼
GET /employees
        │
        ▼
Server Returns Data
        │
        ▼
cy.wait("@getEmployees")
        │
        ▼
Verify Employee Table
```

This is probably the **most common real-world use** of `cy.intercept()` in Cypress end-to-end testing: **wait for the backend API to complete before verifying the UI.**

