Here's a **complete Cypress Data-Driven Testing demo** that is ideal for classroom use. It demonstrates one of the most common industry practices: reading multiple sets of test data from a fixture and executing the same test for each dataset.

---

## Folder Structure

```
cypress
│
├── e2e
│     studentRegistration.cy.js
│
├── fixtures
│     students.json
│
└── support
```

---

## students.json

Create this inside **cypress/fixtures/students.json**

```json
[
    {
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "phone": "9876543210",
        "city": "Bangalore"
    },
    {
        "name": "Anita Rao",
        "email": "anita@gmail.com",
        "phone": "9123456789",
        "city": "Mysore"
    },
    {
        "name": "Rohit Kumar",
        "email": "rohit@gmail.com",
        "phone": "9988776655",
        "city": "Mangalore"
    }
]
```

---

## HTML Page Assumption

Assume your page has

```html
<input id="name">
<input id="email">
<input id="phone">
<input id="city">

<button id="submit">Register</button>

<div id="message"></div>
```

---

# Cypress Test

```javascript
describe("Student Registration - Data Driven Testing", () => {

    beforeEach(() => {

        cy.visit("http://127.0.0.1:5500/student.html")

    })

    it("Registers multiple students using fixture data", () => {

        cy.fixture("students").then((students) => {

            students.forEach((student) => {

                cy.log("Registering : " + student.name)

                cy.get("#name")
                    .clear()
                    .type(student.name)

                cy.get("#email")
                    .clear()
                    .type(student.email)

                cy.get("#phone")
                    .clear()
                    .type(student.phone)

                cy.get("#city")
                    .clear()
                    .type(student.city)

                cy.get("#submit").click()

                cy.get("#message")
                    .should("contain", "Registration Successful")

            })

        })

    })

})
```

---

# What students learn

This single test demonstrates:

* `cy.fixture()`
* Reading JSON data
* Arrays in JSON
* `forEach()`
* Reusing one test with multiple datasets
* `clear()`
* `type()`
* `click()`
* `should()`

---

# Expected Console Output

```
Registering : Rahul Sharma

Registration Successful

Registering : Anita Rao

Registration Successful

Registering : Rohit Kumar

Registration Successful
```

---

# Classroom Explanation

You can explain it step by step:

### Step 1

Instead of writing

```javascript
cy.get("#name").type("Rahul")
```

hardcoded values are moved into a JSON file.

---

### Step 2

Cypress reads the JSON file.

```javascript
cy.fixture("students")
```

---

### Step 3

The fixture returns an array.

```
students

↓

[
 Rahul,
 Anita,
 Rohit
]
```

---

### Step 4

`forEach()` picks one student at a time.

```
Iteration 1

Rahul

↓

Fill Form

↓

Submit

↓

Verify
```

```
Iteration 2

Anita

↓

Fill Form

↓

Submit

↓

Verify
```

```
Iteration 3

Rohit

↓

Fill Form

↓

Submit

↓

Verify
```

---

# Bonus Exercise for Students

Ask them to add a fourth student to `students.json`:

```json
{
    "name":"Pooja Nair",
    "email":"pooja@gmail.com",
    "phone":"9000012345",
    "city":"Udupi"
}
```

Then ask:

> **Did we modify the Cypress code?**

**Answer:** No.

Only the data changed.

This reinforces the key idea of **data-driven testing**: the test logic stays the same while the test data changes, making tests easier to maintain and extend.
