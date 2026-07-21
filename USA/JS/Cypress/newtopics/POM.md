After introducing **Custom Commands**, the natural next topic is **Page Object Model (POM)**, because students will understand why simply putting everything in `commands.js` isn't enough for large projects.

---

# Introduction to Page Object Model (POM)

## The Problem

Imagine you're testing an online shopping website.

Your login page has these elements:

* Username textbox
* Password textbox
* Login button

Suppose **25 different test cases** require logging in.

Without POM, every test repeats:

```javascript
cy.get("#username").type("admin")
cy.get("#password").type("admin123")
cy.get("#loginBtn").click()
```

If tomorrow the developer changes

```text
#loginBtn
```

to

```text
#btnLogin
```

you must update **all 25 test cases**.

This becomes difficult to maintain.

---

# The Solution: Page Object Model (POM)

Page Object Model is a design pattern where **each web page is represented by its own JavaScript class or file**.

Instead of writing element locators in every test, we keep them inside page classes.

The test only describes **what the user is doing**, not **how the page is implemented**.

---

# Real-World Analogy

Imagine driving a car.

You use:

* Steering wheel
* Brake
* Accelerator

You don't know how the engine works internally.

Similarly,

A Cypress test should simply say:

```javascript
loginPage.login("admin", "admin123")
```

The page object knows:

* where the username field is
* where the password field is
* where the login button is

The test doesn't care.

---

# Before POM

```javascript
cy.visit("/login")

cy.get("#username").type("admin")

cy.get("#password").type("admin123")

cy.get("#loginBtn").click()

cy.contains("Welcome").should("be.visible")
```

Every login test repeats these lines.

---

# After POM

```javascript
loginPage.login("admin", "admin123")
```

Much cleaner.

---

# Typical Project Structure

```text
cypress/
│
├── e2e/
│      login.cy.js
│      checkout.cy.js
│      orders.cy.js
│
├── pages/
│      LoginPage.js
│      HomePage.js
│      CartPage.js
│      CheckoutPage.js
│
└── support/
       commands.js
```

Notice that **every important page has its own file**.

---

# Example LoginPage.js

```javascript
class LoginPage {

    visit() {
        cy.visit("/login")
    }

    enterUsername(username) {
        cy.get("#username").type(username)
    }

    enterPassword(password) {
        cy.get("#password").type(password)
    }

    clickLogin() {
        cy.get("#loginBtn").click()
    }

    login(username, password) {

        this.visit()

        this.enterUsername(username)

        this.enterPassword(password)

        this.clickLogin()

    }

}

export default new LoginPage()
```

---

# Using the Page Object

```javascript
import LoginPage from "../pages/LoginPage"

describe("Login", () => {

    it("Valid Login", () => {

        LoginPage.login("admin", "admin123")

        cy.contains("Welcome").should("be.visible")

    })

})
```

Now the test reads almost like English.

---

# What if the Login Button Changes?

Suppose the developer changes

```text
#loginBtn
```

to

```text
#btnLogin
```

Without POM:

❌ Update every login test.

With POM:

✅ Update only one line:

```javascript
clickLogin() {

    cy.get("#btnLogin").click()

}
```

All tests continue to work.

---

# Custom Commands vs POM

Students often confuse these two.

| Custom Commands                                     | Page Object Model                                |
| --------------------------------------------------- | ------------------------------------------------ |
| Stores reusable actions used across the application | Represents a specific web page                   |
| Located in `support/commands.js`                    | Located in the `pages` folder                    |
| Example: `cy.login()`, `cy.waitForLoader()`         | Example: `LoginPage`, `CartPage`, `CheckoutPage` |
| Reusable across multiple pages                      | Focused on one page's elements and actions       |

---

# When to Use Which?

Use **Custom Commands** for common actions that are not tied to a single page, such as:

* Login through an API
* Clearing cookies
* Waiting for loaders
* Selecting a date
* Reading test data

Use **Page Object Model** for page-specific interactions, such as:

* Login Page
* Product Page
* Cart Page
* Checkout Page
* User Profile Page

---

# Key Takeaway

* **Custom Commands** answer: **"What common action can I reuse across my entire project?"**
* **Page Object Model** answers: **"How do I organize the elements and actions of a particular page?"**

In professional Cypress projects, these two patterns are commonly used **together**. A test might call `LoginPage.login()` to interact with the login page, while that page object or the test itself can still use reusable custom commands like `cy.waitForLoader()` or `cy.loginApi()` where appropriate. This combination results in tests that are easier to read, maintain, and scale.
