Since you've already covered **Custom Commands**, **POM**, and **cy.intercept()**, this topic naturally fits next. It's also highly practical because almost every real Cypress framework uses environment variables.

---

# Session Plan: Environment Variables in Cypress

**Duration:** 60 Minutes

## Learning Objective

By the end of this session, students will be able to:

* Understand why environment variables are needed.
* Store URLs, usernames, passwords, and API keys outside test scripts.
* Configure multiple environments (Development, QA, Production).
* Access environment variables using `Cypress.env()`.
* Write cleaner and reusable tests.

---

# Session Breakdown

| Time   | Topic                           |
| ------ | ------------------------------- |
| 10 min | Introduction & Need             |
| 10 min | What are Environment Variables? |
| 15 min | Creating Environment Variables  |
| 15 min | Practical Demo                  |
| 10 min | Best Practices & Q&A            |

---

# Part 1 – Introduction (10 mins)

### Ask students:

Imagine your test contains:

```javascript
cy.visit("https://qa.company.com")
```

Later the company asks you to test

```
https://staging.company.com
```

How many test files will you edit?

Students will answer:

> Every file.

Exactly.

Now imagine changing **200 test files**.

That is why Environment Variables exist.

---

# Real-world Example

Suppose your company has

Development

```
https://dev.company.com
```

QA

```
https://qa.company.com
```

Production

```
https://company.com
```

The application changes.

Your test logic doesn't.

Only the URL changes.

Instead of changing hundreds of tests,

you change one configuration.

---

# Part 2 – What are Environment Variables?

Definition:

> Environment Variables are configurable values stored separately from test scripts, allowing the same test to run against different environments without modifying the code.

---

Typical values stored:

* Base URL
* Username
* Password
* API URL
* API Token
* Browser configuration
* Timeout values

---

# Part 3 – Ways to Create Environment Variables

Explain there are multiple ways.

### Method 1 (Most Common)

`cypress.config.js`

```javascript
const { defineConfig } = require("cypress")

module.exports = defineConfig({

  env: {

      username: "admin",

      password: "admin123"

  }

})
```

---

Access it

```javascript
Cypress.env("username")
```

---

Output

```
admin
```

---

### Method 2

Using

```
cypress.env.json
```

```json
{

 "username":"admin",

 "password":"admin123"

}
```

Explain:

Useful because

* different team members
* ignored in Git
* can store local credentials

---

### Method 3

Command Line

```bash
npx cypress run --env username=admin,password=admin123
```

Useful in

CI/CD

GitHub Actions

Jenkins

Azure DevOps

---

# Part 4 – Practical Demo

## Example 1

Without Environment Variables

```javascript
describe("Login", () => {

    it("Login Test", () => {

        cy.visit("https://www.demoblaze.com")

        cy.contains("Log in").click()

        cy.get("#loginusername").type("testuser")

        cy.get("#loginpassword").type("password")

        cy.contains("button","Log in").click()

    })

})
```

Ask students

What's wrong?

Expected answers

* Hardcoded URL
* Hardcoded Username
* Hardcoded Password

---

## Improved Version

### cypress.config.js

```javascript
const { defineConfig } = require("cypress")

module.exports = defineConfig({

  e2e: {

    baseUrl: "https://www.demoblaze.com"

  },

  env: {

      username:"testuser",

      password:"password"

  }

})
```

---

### Test

```javascript
describe("Login", () => {

    it("Login Test", () => {

        cy.visit("/")

        cy.contains("Log in").click()

        cy.get("#loginusername")
          .type(Cypress.env("username"))

        cy.get("#loginpassword")
          .type(Cypress.env("password"))

        cy.contains("button","Log in").click()

    })

})
```

Students immediately notice

No hardcoded values.

---

# Demo 2 – Switching Environment

Today

```javascript
baseUrl:

https://qa.company.com
```

Tomorrow

```javascript
baseUrl:

https://staging.company.com
```

Only change

```javascript
baseUrl
```

Entire test suite now runs on

Staging.

No test modifications.

---

# Demo 3 – Logging Environment Variables

```javascript
it("Print Variables",()=>{

    cy.log(Cypress.env("username"))

    cy.log(Cypress.env("password"))

})
```

---

# Folder Structure

```
cypress

 fixtures

 e2e

 support

cypress.config.js

cypress.env.json
```

Explain where each configuration file fits into a typical Cypress project.

---

# Best Practices

✅ Store URLs in `baseUrl`.

✅ Store credentials using Environment Variables.

✅ Never hardcode passwords in test scripts.

✅ Exclude `cypress.env.json` from version control if it contains sensitive data.

✅ Use different environment values for Development, QA, and Production.

---

# Common Interview Questions

### Q1. Why use Environment Variables?

To avoid hardcoding configuration values and make tests reusable across multiple environments.

---

### Q2. Difference between `baseUrl` and `Cypress.env()`?

**`baseUrl`**

* Specifically stores the application's base URL.
* Used automatically with `cy.visit()`.

**`Cypress.env()`**

* Stores any custom configuration values like usernames, passwords, API keys, feature flags, or environment names.

---

### Q3. Where can Environment Variables be defined?

* `cypress.config.js`
* `cypress.env.json`
* Command line (`--env`)
* CI/CD pipeline variables

---

### Q4. Can Environment Variables improve test maintenance?

Yes. Updating a single configuration value can change the behavior of an entire test suite without modifying individual test files.

---

# Hands-on Exercise (15 Minutes)

**Task:** Refactor an existing login test.

Students should:

1. Create a `baseUrl` in `cypress.config.js`.
2. Add `username` and `password` under `env`.
3. Replace hardcoded values in the test with `cy.visit("/")` and `Cypress.env()`.
4. Run the test successfully.
5. Change the `baseUrl` (or simulate another environment) and observe that only the configuration changes while the test code remains the same.

This exercise reinforces why environment variables are essential in real-world Cypress automation frameworks.
