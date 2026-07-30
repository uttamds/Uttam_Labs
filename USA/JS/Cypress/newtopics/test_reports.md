## Topic: Generate Execution Reports, Screenshots, and Videos for Test Results (Cypress)

### Learning Objectives

By the end of this session, students will be able to:

* Understand why execution reports are important.
* Automatically capture screenshots on test failures.
* Record execution videos.
* Generate professional HTML reports.
* Share reports with developers and managers.

---

# 1. Why Do We Need Test Reports?

Ask students:

> "If your automation runs 500 test cases overnight, how do you know what passed and what failed?"

Without reports:

* ❌ Need to open Cypress manually
* ❌ Difficult to identify failures
* ❌ Cannot share results with stakeholders

With reports:

* ✔ Pass/Fail summary
* ✔ Error messages
* ✔ Screenshots
* ✔ Execution time
* ✔ Easy sharing

---

# 2. Cypress Execution Flow

```
Run Tests
     │
     ▼
Test Executes
     │
     ├── Passed
     │
     └── Failed
             │
             ├── Screenshot
             ├── Video
             └── HTML Report
```

---

# 3. Default Cypress Outputs

Cypress provides several outputs automatically.

| Feature                | Automatic?        |
| ---------------------- | ----------------- |
| Console logs           | ✔                 |
| Screenshots on failure | ✔                 |
| Videos                 | ✔ (if enabled)    |
| HTML reports           | ❌ Requires plugin |

---

# 4. Screenshots

## Purpose

Helps identify exactly what the application looked like when the test failed.

Example:

```
Expected:

Login Successful

Actual:

Invalid Password
```

Instead of guessing...

You see this screenshot.

```
-------------------------
 Username
 Password

 Invalid Password

 [Login]
-------------------------
```

Immediately obvious what happened.

---

## Automatic Screenshot on Failure

No code required.

Simply run:

```bash
npx cypress run
```

If any test fails:

```
cypress/
    screenshots/
        login.cy.js/
            Invalid login (failed).png
```

---

## Manual Screenshot

Sometimes you want screenshots even when the test passes.

```javascript
it("Take Screenshot", () => {

    cy.visit("https://example.com")

    cy.screenshot("Homepage")

})
```

Result:

```
Homepage.png
```

---

## Capture Specific Element

```javascript
cy.get("#loginForm").screenshot("Login Form")
```

Only that element is captured.

---

# 5. Videos

Videos record the entire execution.

Useful when:

* Animation issues
* Timing issues
* Random failures
* CI/CD execution

---

## Enable Video

In `cypress.config.js`

```javascript
const { defineConfig } = require("cypress")

module.exports = defineConfig({

    video: true

})
```

Run:

```bash
npx cypress run
```

Videos saved in:

```
cypress/videos/
```

Example:

```
login.cy.mp4
```

---

## Why Videos?

Suppose the login button disappears for only 1 second.

Screenshot:

```
Shows only failure.
```

Video:

```
Shows exactly how it disappeared.
```

Huge advantage.

---

# 6. HTML Reports

Managers usually don't read terminal output.

Instead they prefer:

```
---------------------------------

Regression Execution Report

Passed : 98

Failed : 2

Execution Time : 8 mins

---------------------------------
```

Professional looking reports.

---

# 7. Mochawesome Reporter

One of the most popular Cypress reporting plugins.

Install:

```bash
npm install --save-dev mochawesome
```

Configure reporter:

```javascript
module.exports = defineConfig({

    reporter: "mochawesome"

})
```

Run

```bash
npx cypress run
```

Generated report:

```
mochawesome-report/

    index.html
```

Open:

```
index.html
```

You get

* Test summary
* Pass/Fail
* Duration
* Stack trace

---

# 8. Sample Report Structure

```
Regression Report

Total Tests : 15

Passed : 13

Failed : 2

Skipped : 0

Duration : 4 min 12 sec

---------------------------------

Login Test
PASS

Add Product
PASS

Checkout
FAIL

Error:
Expected "Order Placed"
Received "Server Error"

---------------------------------
```

---

# 9. Real Project Scenario

Imagine Amazon's nightly regression suite.

```
1,500 Test Cases
```

Morning report:

```
Passed : 1487

Failed : 13
```

Developer opens report.

Clicks failed test.

Sees:

* Screenshot
* Video
* Error message

Issue fixed quickly.

---

# 10. Folder Structure After Execution

```
cypress/

    screenshots/

        login.cy.js/

            Invalid Login.png

    videos/

        login.cy.mp4

reports/

    mochawesome.html
```

---

# 11. Best Practices

* Capture screenshots only when useful.
* Keep videos enabled for CI/CD or nightly runs.
* Archive reports for regression history.
* Include screenshots in failure reports.
* Share HTML reports with stakeholders instead of console logs.
* Clean old reports regularly to save disk space.

---

# 12. Mini Demo Flow (10 Minutes)

### Demo 1

Run a passing test.

```bash
npx cypress run
```

Show:

* No screenshots
* Video generated

---

### Demo 2

Intentionally fail a test.

```javascript
cy.contains("Logout").click()
```

(when Logout doesn't exist)

Show:

* Screenshot automatically captured
* Failure message

---

### Demo 3

Open

```
cypress/screenshots/
```

Display the captured image.

---

### Demo 4

Open

```
cypress/videos/
```

Play the recorded execution.

---

### Demo 5

Generate the Mochawesome report and open the HTML file to show:

* Total tests
* Passed/Failed counts
* Duration
* Failure details

---

# Key Takeaways

* **Screenshots** capture the application state at the moment of failure (or manually when requested).
* **Videos** record the complete execution, making it easier to investigate timing or intermittent issues.
* **HTML reports** provide a professional summary of the execution that can be shared with developers, testers, and managers.
* Together, reports, screenshots, and videos make debugging faster and provide clear evidence of test results.
