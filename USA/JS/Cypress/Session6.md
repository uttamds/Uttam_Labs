| Topic                                   | Description                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Data-Driven Testing (Fixtures)          | Store and use test data from JSON files to make tests reusable and maintainable.                   |
| REST API Testing (`cy.request()`)       | Perform GET, POST, PUT, PATCH, and DELETE requests and validate API responses.                     |
| Network Interception (`cy.intercept()`) | Capture, monitor, and validate network requests and responses during test execution.               |
| API Mocking                             | Simulate backend responses using fixtures to test applications without relying on live APIs.       |
| Custom Commands                         | Create reusable Cypress commands to eliminate repetitive code and improve readability.             |
| Page Object Model (POM)                 | Organize test code by separating page elements and actions into reusable classes/files.            |
| Environment Variables                   | Manage URLs, credentials, and configuration for different test environments.                       |
| File Upload & Download                  | Automate file upload and validate file download scenarios.                                         |
| Session Management                      | Preserve login sessions and optimize test execution using `cy.session()`.                          |
| Database Validation (Concepts)          | Understand how to verify backend data after UI or API operations (with plugins/tasks).             |
| Reports & Screenshots                   | Generate execution reports, screenshots, and videos for test results.                              |
| Cross-Browser Testing                   | Execute Cypress tests across different supported browsers.                                         |
| CI/CD Integration                       | Run Cypress tests automatically using GitHub Actions, Jenkins, or other CI tools.                  |
| End-to-End Project                      | Build a complete automation framework combining UI, API, fixtures, intercepts, POM, and reporting. |

# ===================================================



# API Testing

That's even better for a beginner class. Keep everything centered around **one employee record** and use only **GET** and **POST**. Students won't get distracted by multiple APIs or datasets.

---

# Problem Statement

### Company: ABC Technologies

You have recently joined **ABC Technologies** as a **QA Automation Engineer**.

The company has developed an **Employee Management System (EMS)**. The frontend website is still under development, but the backend team has already exposed the APIs.

Your task is to verify that the APIs are working correctly before the UI is released.

Today, you will test only two operations:

1. Search an existing employee (**GET**)
2. Add a new employee (**POST**)

---

# Employee JSON

This is the employee information stored in the system.

```json
{
    "id": 101,
    "name": "Rahul Sharma",
    "department": "Engineering",
    "designation": "Software Engineer",
    "salary": 75000,
    "email": "rahul.sharma@abctech.com",
    "phone": "9876543210",
    "city": "Bangalore",
    "status": "Active"
}
```

Explain each field briefly:

| Field       | Meaning                             |
| ----------- | ----------------------------------- |
| id          | Unique employee number              |
| name        | Employee name                       |
| department  | Department where the employee works |
| designation | Job title                           |
| salary      | Monthly salary                      |
| email       | Official company email              |
| phone       | Contact number                      |
| city        | Work location                       |
| status      | Employee status (Active/Inactive)   |

---

# Test Case 1 – GET Employee

### Business Scenario

An HR executive wants to view the details of Employee **101**.

Instead of opening the website and searching manually, we directly test the backend API.

### API

```
GET /employees/101
```

### Cypress Test

```javascript
describe("Employee Management System", () => {

    it("Get Employee Details", () => {

        cy.request("https://jsonplaceholder.typicode.com/users/1")

            .then((response) => {

                expect(response.status).to.equal(200)

                cy.log("Employee Name : " + response.body.name)
                cy.log("Email : " + response.body.email)
                cy.log("Phone : " + response.body.phone)
                cy.log("City : " + response.body.address.city)

            })

    })

})
```

### Teaching Points

* `cy.request()` sends the request directly to the server.
* `response.status` should be **200**.
* `response.body` contains the employee information.
* We can read individual fields from the JSON.

---

# Test Case 2 – POST Employee

### Business Scenario

A new employee has joined ABC Technologies.

HR wants to register the employee in the system.

Instead of filling a web form, we directly call the API.

### API

```
POST /employees
```

### Request Body

```json
{
    "name": "Ananya Rao",
    "department": "QA",
    "designation": "Test Engineer",
    "salary": 60000,
    "email": "ananya.rao@abctech.com",
    "phone": "9876501234",
    "city": "Mysore",
    "status": "Active"
}
```

### Cypress Test

```javascript
describe("Employee Management System", () => {

    it("Add New Employee", () => {

        cy.request({

            method: "POST",

            url: "https://jsonplaceholder.typicode.com/posts",

            body: {

                name: "Ananya Rao",
                department: "QA",
                designation: "Test Engineer",
                salary: 60000,
                email: "ananya.rao@abctech.com",
                phone: "9876501234",
                city: "Mysore",
                status: "Active"

            }

        })

        .then((response) => {

            expect(response.status).to.equal(201)

            cy.log("Employee Created Successfully")
            cy.log("Generated ID : " + response.body.id)
            cy.log("Employee : " + response.body.name)

        })

    })

})
```

---

# Classroom Discussion

Ask these questions after the tests:

1. **Why did the GET request return `200`?**

   * Because we successfully retrieved an existing employee.

2. **Why did the POST request return `201`?**

   * Because a new employee record was created.

3. **Which request only reads data?**

   * GET.

4. **Which request sends new data to the server?**

   * POST.

---

# Summary

| Operation               | Business Activity            | HTTP Method | Expected Status |
| ----------------------- | ---------------------------- | ----------- | --------------- |
| View employee details   | HR searches for Employee 101 | GET         | 200 OK          |
| Register a new employee | HR adds a new employee       | POST        | 201 Created     |

> **Note for students:** Since we're using the free **JSONPlaceholder** service for learning, the URLs (`/users/1` and `/posts`) don't exactly match our Employee Management System story. In a real company, these would typically be endpoints like `/employees/101` and `/employees`. We're using JSONPlaceholder only because it lets us practice API testing without needing to build our own backend first.




# Session 1 – Data-Driven Testing (Highly Recommended)

### Concepts

* What is hardcoding?
* Why use test data?
* JSON files
* Fixtures
* Reading data from JSON
* Reusing test data
* Running the same test with multiple datasets

Example `student.json`

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "city": "Bangalore"
}
```

Example

```javascript
cy.fixture("student").then((student) => {

    cy.get("#name").type(student.name)

    cy.get("#email").type(student.email)

    cy.get("#city").type(student.city)

})
```

Then show multiple students.

```json
[
 {
   "name":"Rahul",
   "city":"Bangalore"
 },
 {
   "name":"Anita",
   "city":"Mysore"
 },
 {
   "name":"Rohit",
   "city":"Mangalore"
 }
]
```

Now students begin to understand scalable testing.

---

# Session 2 – API Testing

This is where students usually become really interested.

No browser.

No clicking.

Just send requests.

Example

```javascript
cy.request("https://jsonplaceholder.typicode.com/users")
```

Verify

```javascript
.should((response)=>{

    expect(response.status).to.equal(200)

})
```

Then explain

```
Browser

↓

Click Login

↓

POST /login

↓

Server

↓

Response

↓

Dashboard
```

Students finally understand what is happening behind the scenes.

---

# Session 3 – REST API

Teach

```
GET

POST

PUT

PATCH

DELETE
```

using a free API like JSONPlaceholder or ReqRes.

Examples

```
Get users

Create user

Update user

Delete user
```

---

# Session 4 – Intercept

This is one of Cypress's standout features.

```javascript
cy.intercept("GET","**/users").as("users")

cy.visit("/")

cy.wait("@users")
```

Then verify

```javascript
cy.wait("@users")
  .its("response.statusCode")
  .should("eq",200)
```

Students love seeing network requests.

---

# Session 5 – Mocking

Instead of calling the server...

```javascript
cy.intercept(
    "GET",
    "**/users",
    {
       fixture:"users.json"
    }
)
```

Now explain

> The backend is down.

No problem.

We fake it.

This is exactly what many QA teams do.

---

# Session 6 – Custom Commands

Create

```javascript
Cypress.Commands.add("login",()=>{

})
```

Use

```javascript
cy.login()
```

Students appreciate how repetitive code can be reduced.

---

# Session 7 – Page Object Model

Instead of

```javascript
cy.get("#username")
```

Create

```javascript
loginPage.enterUsername()
```

Now discuss maintainability and cleaner test design.

---

# Session 8 – Reports

Generate

* Mochawesome
* Screenshots
* Videos

Students like seeing professional-looking reports.

---

# A complete mini project (5–6 hours)

By the end, have them automate a simple **Student Registration Portal**:

* Login
* Read test data from a fixture
* Register three students
* Verify the table
* Call an API to fetch student details
* Intercept the API
* Mock one response
* Generate a report

This ties together UI automation, data-driven testing, API testing, and reporting in one cohesive exercise.

## If you have only **10 more hours** with the students

I'd structure it like this:

1. **Data-Driven Testing with Fixtures** (2 hours)
2. **REST API Testing using `cy.request()`** (2 hours)
3. **Network Intercept and Mocking** (2 hours)
4. **Custom Commands + Page Object Model** (2 hours)
5. **Mini Project + Report Generation** (2 hours)

This sequence gives students exposure to the skills that are most commonly expected in modern Cypress-based QA roles and will make their project work and interviews much stronger than spending additional time on basic UI interactions.

