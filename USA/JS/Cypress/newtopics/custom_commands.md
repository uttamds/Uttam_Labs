### Custom Commands in Cypress

As our Cypress test suite grows, we often find ourselves writing the same sequence of steps repeatedly across multiple test cases. For example, almost every test may require logging into the application, navigating to a specific page, searching for a product, or filling out the same form. Writing these steps over and over again makes the test scripts longer, more difficult to read, and harder to maintain. If a step changes (for example, the login process is updated), we would have to modify every test containing that code.

To solve this problem, **Cypress provides Custom Commands**. A Custom Command is a reusable function that encapsulates a set of frequently used Cypress commands into a single, meaningful command. Once created, it becomes available throughout the entire Cypress project and can be called using the `cy` object, just like built-in Cypress commands such as `cy.visit()` or `cy.click()`.

Instead of repeatedly writing the implementation details, we write the logic once and simply invoke the custom command wherever it is needed.

---

### How Are Custom Commands Created?

Custom Commands are typically created in the **`cypress/support/commands.js`** (or **`commands.ts`** for TypeScript projects) file. Cypress automatically loads this file before running your test cases.

To create a Custom Command, we use the following syntax:

```javascript
Cypress.Commands.add("commandName", () => {

    // Cypress commands go here

})
```

For example, to create a reusable login command:

```javascript
Cypress.Commands.add("login", (username, password) => {

    cy.get("#username").type(username)
    cy.get("#password").type(password)
    cy.get("#loginBtn").click()

})
```

Once this command is defined, it becomes available in every Cypress test and can be called just like any other Cypress command:

```javascript
cy.login("admin", "admin123")
```

---

### Example without a Custom Command

Every test that requires login would contain the same code:

```javascript
cy.get("#username").type("admin")
cy.get("#password").type("admin123")
cy.get("#loginBtn").click()
```

If ten test cases require login, these same three lines would be repeated ten times.

---

### Example with a Custom Command

After creating a reusable login command:

```javascript
cy.login("admin", "admin123")
```

The implementation is hidden inside the custom command, making the test much shorter and easier to understand. The test now focuses on **what** it is doing (logging in) rather than **how** it is doing it.

---

### Why Use Custom Commands?

Imagine an application has **100 test cases**, and every one of them starts by logging in.

Without Custom Commands:

* The login code is repeated in all 100 test cases.
* If the login page changes (for example, the username field ID changes), every test must be updated.
* This increases development time and the possibility of introducing errors.

With Custom Commands:

* The login logic is written only once.
* All tests simply call `cy.login()`.
* If the login page changes, only the custom command needs to be updated.
* Every test automatically benefits from the change.

This follows the software engineering principle of **"Write Once, Reuse Many Times."**

---

### Benefits of Custom Commands

* **Reduce code duplication** by writing common steps only once.
* **Improve readability** by replacing multiple lines of code with meaningful command names.
* **Simplify maintenance** since updates are made in one location instead of every test file.
* **Promote reusability** by allowing the same command to be used across multiple test cases.
* **Improve consistency** because every test performs the same operation in the same way.
* **Make tests easier to understand**, allowing testers to focus on the business scenario rather than low-level implementation details.
* **Reduce development effort** when creating new test cases, as common actions are already available as reusable commands.
* **Support scalable test automation**, making large Cypress projects easier to organize and maintain.

Once students understand **how to create custom commands**, it's best to show them a **real-world scenario** where custom commands make tests cleaner and reusable.

## Use Case: E-commerce Website (Amazon/Flipkart Style)

Suppose your application has a login page, and **every test requires the user to log in** before performing any action.

Instead of repeating the login steps in every test, create a custom command.

---

## Project Structure

```text
cypress/
│
├── e2e/
│   ├── addToCart.cy.js
│   ├── checkout.cy.js
│   └── wishlist.cy.js
│
└── support/
    ├── commands.js
    └── e2e.js
```

---

# Step 1: Create a Custom Command

**commands.js**

```javascript
Cypress.Commands.add("login", (email, password) => {

    cy.visit("https://www.demoblaze.com")

    cy.contains("Log in").click()

    cy.get("#loginusername").type(email)

    cy.get("#loginpassword").type(password)

    cy.contains("button", "Log in").click()

    cy.contains("Welcome").should("be.visible")

})
```

Now, **`cy.login()`** behaves like a built-in Cypress command.

---

# Step 2: Use It in Different Tests

### Test 1 – Add Product to Cart

```javascript
describe("Shopping Cart", () => {

    it("Adds a laptop to cart", () => {

        cy.login("testuser", "Password123")

        cy.contains("Laptops").click()

        cy.contains("Sony vaio i5").click()

        cy.contains("Add to cart").click()

        cy.on("window:alert", (msg) => {

            expect(msg).to.equal("Product added")

        })

    })

})
```

---

### Test 2 – Checkout

```javascript
describe("Checkout", () => {

    it("Places an order", () => {

        cy.login("testuser", "Password123")

        cy.contains("Cart").click()

        cy.contains("Place Order").click()

        cy.get("#name").type("Rahul")

        cy.get("#country").type("India")

        cy.contains("Purchase").click()

    })

})
```

---

### Test 3 – Logout

```javascript
describe("Logout", () => {

    it("Logs out successfully", () => {

        cy.login("testuser", "Password123")

        cy.contains("Log out").click()

        cy.contains("Log in").should("be.visible")

    })

})
```

Notice that the login code appears **only once**.

---

# Why is this better?

Without a custom command, every test would contain the same login steps:

```javascript
cy.visit(...)
cy.contains("Log in").click()
cy.get(...).type(...)
cy.get(...).type(...)
cy.contains("Log in").click()
```

This repetition:

* Increases maintenance effort.
* Makes tests longer and harder to read.
* Requires updates in multiple places if the login page changes.

With a custom command:

```javascript
cy.login("testuser", "Password123")
```

the test immediately communicates its intent, while the implementation remains in one place.

---

# A More Advanced Example

Real projects often need to verify whether a user has successfully logged in.

**commands.js**

```javascript
Cypress.Commands.add("verifyLoggedInUser", (username) => {

    cy.contains(`Welcome ${username}`)
        .should("be.visible")

})
```

Use it like this:

```javascript
cy.login("testuser", "Password123")

cy.verifyLoggedInUser("testuser")
```

---

# Another Practical Command

Suppose many pages display a loading spinner.

```javascript
Cypress.Commands.add("waitForLoader", () => {

    cy.get(".loading-spinner")
        .should("not.exist")

})
```

Usage:

```javascript
cy.login("testuser", "Password123")

cy.waitForLoader()

cy.contains("Orders").click()
```

---

# Key Teaching Point

A custom command should represent a **business action**, not just a single Cypress command.

Good examples:

* `cy.login()`
* `cy.logout()`
* `cy.addProductToCart()`
* `cy.searchProduct()`
* `cy.placeOrder()`
* `cy.waitForLoader()`
* `cy.verifyLoggedInUser()`

Avoid creating custom commands for one-line wrappers such as:

```javascript
cy.clickButton()
cy.typeText()
cy.pressEnter()
```

These add little value because Cypress already provides clear built-in commands. The greatest benefit comes from encapsulating **multi-step workflows that are reused across many tests**, making the test suite easier to read and maintain.


---

### In Summary

Custom Commands are one of the most useful features in Cypress for building clean and maintainable automation frameworks. They allow us to group commonly used actions into reusable commands, reducing repetitive code and making our test scripts more readable. As automation projects grow, Custom Commands help improve code quality, simplify maintenance, and encourage the reuse of common functionality across the entire test suite.

Once students understand **how to create custom commands**, it's best to show them a **real-world scenario** where custom commands make tests cleaner and reusable.

## Use Case: E-commerce Website (Amazon/Flipkart Style)

Suppose your application has a login page, and **every test requires the user to log in** before performing any action.

Instead of repeating the login steps in every test, create a custom command.

---

## Project Structure

```text
cypress/
│
├── e2e/
│   ├── addToCart.cy.js
│   ├── checkout.cy.js
│   └── wishlist.cy.js
│
└── support/
    ├── commands.js
    └── e2e.js
```

---

# Step 1: Create a Custom Command

**commands.js**

```javascript
Cypress.Commands.add("login", (email, password) => {

    cy.visit("https://www.demoblaze.com")

    cy.contains("Log in").click()

    cy.get("#loginusername").type(email)

    cy.get("#loginpassword").type(password)

    cy.contains("button", "Log in").click()

    cy.contains("Welcome").should("be.visible")

})
```

Now, **`cy.login()`** behaves like a built-in Cypress command.

---

# Step 2: Use It in Different Tests

### Test 1 – Add Product to Cart

```javascript
describe("Shopping Cart", () => {

    it("Adds a laptop to cart", () => {

        cy.login("testuser", "Password123")

        cy.contains("Laptops").click()

        cy.contains("Sony vaio i5").click()

        cy.contains("Add to cart").click()

        cy.on("window:alert", (msg) => {

            expect(msg).to.equal("Product added")

        })

    })

})
```

---

### Test 2 – Checkout

```javascript
describe("Checkout", () => {

    it("Places an order", () => {

        cy.login("testuser", "Password123")

        cy.contains("Cart").click()

        cy.contains("Place Order").click()

        cy.get("#name").type("Rahul")

        cy.get("#country").type("India")

        cy.contains("Purchase").click()

    })

})
```

---

### Test 3 – Logout

```javascript
describe("Logout", () => {

    it("Logs out successfully", () => {

        cy.login("testuser", "Password123")

        cy.contains("Log out").click()

        cy.contains("Log in").should("be.visible")

    })

})
```

Notice that the login code appears **only once**.

---

# Why is this better?

Without a custom command, every test would contain the same login steps:

```javascript
cy.visit(...)
cy.contains("Log in").click()
cy.get(...).type(...)
cy.get(...).type(...)
cy.contains("Log in").click()
```

This repetition:

* Increases maintenance effort.
* Makes tests longer and harder to read.
* Requires updates in multiple places if the login page changes.

With a custom command:

```javascript
cy.login("testuser", "Password123")
```

the test immediately communicates its intent, while the implementation remains in one place.

---

# A More Advanced Example

Real projects often need to verify whether a user has successfully logged in.

**commands.js**

```javascript
Cypress.Commands.add("verifyLoggedInUser", (username) => {

    cy.contains(`Welcome ${username}`)
        .should("be.visible")

})
```

Use it like this:

```javascript
cy.login("testuser", "Password123")

cy.verifyLoggedInUser("testuser")
```

---

# Another Practical Command

Suppose many pages display a loading spinner.

```javascript
Cypress.Commands.add("waitForLoader", () => {

    cy.get(".loading-spinner")
        .should("not.exist")

})
```

Usage:

```javascript
cy.login("testuser", "Password123")

cy.waitForLoader()

cy.contains("Orders").click()
```

---

# Key Teaching Point

A custom command should represent a **business action**, not just a single Cypress command.

Good examples:

* `cy.login()`
* `cy.logout()`
* `cy.addProductToCart()`
* `cy.searchProduct()`
* `cy.placeOrder()`
* `cy.waitForLoader()`
* `cy.verifyLoggedInUser()`

Avoid creating custom commands for one-line wrappers such as:

```javascript
cy.clickButton()
cy.typeText()
cy.pressEnter()
```

These add little value because Cypress already provides clear built-in commands. The greatest benefit comes from encapsulating **multi-step workflows that are reused across many tests**, making the test suite easier to read and maintain.

