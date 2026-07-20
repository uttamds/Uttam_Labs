Excellent question. This is actually **the reason `cy.intercept()` exists**.

Imagine you're testing Amazon.

When the Home page loads, it automatically requests products.

```text
Browser
    │
    ▼
GET /api/products
    │
    ▼
Server
    │
    ▼
Returns 100 products
```

As a tester, you're **not interested in the request itself**. You're interested in verifying that the application behaves correctly.

There are three main reasons to intercept.

---

# 1. Verify the Request (Observation)

Suppose the requirement says:

> "When the Home page opens, the application should request the latest products."

You can verify that.

```javascript
cy.intercept("GET", "**/api/products").as("products")

cy.visit("https://amazon.com")

cy.wait("@products")
```

Now you've confirmed:

* ✅ The page actually made the request.
* ✅ It didn't forget to call the API.

---

# 2. Verify the Response

Maybe the API should return **HTTP 200**.

```javascript
cy.wait("@products")
  .its("response.statusCode")
  .should("eq", 200)
```

Or maybe you want to check that the response contains products.

```javascript
cy.wait("@products").then((interception) => {
    expect(interception.response.body.products.length).to.be.greaterThan(0)
})
```

You're verifying that the backend responded correctly.

---

# 3. Make Your Test Stable (The Biggest Reason)

Imagine the product API takes **8 seconds**.

Without intercept:

```javascript
cy.visit(...)

cy.get(".product-card")
    .should("have.length",20)
```

Sometimes this fails because the products haven't arrived yet.

With intercept:

```javascript
cy.intercept("GET","**/products").as("products")

cy.visit(...)

cy.wait("@products")

cy.get(".product-card")
    .should("have.length",20)
```

Now Cypress waits until the API completes before checking the page.

This makes the test much more reliable.

---

# 4. Mock the API (Later Topic)

Suppose Amazon's server is down.

Normally:

```text
Browser
     │
     ▼
Server
     │
     ▼
500 Error
```

Your UI test fails even though the UI code is fine.

Instead, Cypress can pretend to be the server.

```text
Browser
     │
     ▼
Cypress
     │
Fake Response
```

Now you can test the UI even if the backend is unavailable.

This is called **API mocking**.

---

# Real Amazon Scenario

Suppose you're testing the search feature.

You search for:

```text
Laptop
```

The browser sends:

```text
GET /api/search?q=laptop
```

You may want to verify:

* Was the correct search term sent?
* Did the request happen?
* Was the status code 200?
* Did the server return products?
* Did the UI display those products?
* What happens if the server returns no products?
* What happens if the server returns a 500 error?

All of these are enabled by `cy.intercept()`.

---

## A simple sentence for students

I often summarize it like this:

> **"We don't intercept because we want to stop the request. We intercept because, as testers, we want to observe it, verify it, wait for it, or replace it with our own response."**

That one sentence captures the four core uses of `cy.intercept()`:

1. **Observe** the request.
2. **Verify** the request or response.
3. **Wait** for the request to complete before continuing the test.
4. **Mock** the response when needed.
