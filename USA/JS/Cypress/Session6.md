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

If they already know how to automate forms, buttons, dropdowns, checkboxes, tables, and basic assertions, then I would **not** spend more time on UI commands. At that point, it's better to introduce concepts that make them feel like they're doing "real automation."

For engineering students, I'd suggest this progression.

| Priority | Topic                                   | Industry Relevance | Difficulty  |
| -------- | --------------------------------------- | ------------------ | ----------- |
| ⭐⭐⭐⭐⭐    | Data-Driven Testing (Fixtures)          | Very High          | Easy        |
| ⭐⭐⭐⭐⭐    | API Testing                             | Very High          | Easy-Medium |
| ⭐⭐⭐⭐⭐    | Network Intercept (`cy.intercept()`)    | Very High          | Medium      |
| ⭐⭐⭐⭐     | Custom Commands                         | High               | Medium      |
| ⭐⭐⭐⭐     | Page Object Model                       | High               | Medium      |
| ⭐⭐⭐      | Environment Variables                   | Medium             | Easy        |
| ⭐⭐⭐⭐     | Reports & Screenshots                   | High               | Easy        |
| ⭐⭐⭐⭐     | CI/CD (GitHub Actions/Jenkins overview) | High               | Medium      |

---

# My recommendation

I would teach **Data-Driven Testing first**, followed immediately by **API Testing**.

Why?

Students usually think automation means:

> Open browser → Click → Type → Verify

When they learn fixtures and APIs, they realize automation is much broader than UI testing.

---

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

