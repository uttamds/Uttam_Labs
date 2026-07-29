For a classroom demo, don't build a full database project. Instead, show students the **journey of a `cy.task()` call** with the smallest possible example.

---

## Step 1: Define a Task (Node Side)

`cypress.config.js`

```javascript
const { defineConfig } = require("cypress")

module.exports = defineConfig({

  e2e: {

    setupNodeEvents(on, config) {

      on("task", {

        greet() {
          return "Hello from Node!"
        }

      })

    }

  }

})
```

### Explanation

* `on("task", {...})` registers one or more tasks.
* Here we create a task named **greet**.
* Whatever this function returns is sent back to Cypress.

---

## Step 2: Call the Task (Browser Side)

```javascript
describe("cy.task Demo", () => {

    it("calls a node task", () => {

        cy.task("greet")
            .then(message => {

                cy.log(message)

            })

    })

})
```

### Flow

```text
cy.task("greet")

        │

        ▼

Node executes greet()

        │

returns

"Hello from Node!"

        │

        ▼

.then(message)
```

---

# Passing Data

Node

```javascript
on("task", {

    square(number) {

        return number * number

    }

})
```

Test

```javascript
cy.task("square", 8)
.then(result => {

    expect(result).to.equal(64)

})
```

Here,

* `8` is sent to Node.
* Node calculates.
* `64` comes back.

---

# Passing an Object

Node

```javascript
on("task", {

    fullName(person) {

        return person.first + " " + person.last

    }

})
```

Test

```javascript
cy.task("fullName", {

    first: "John",
    last: "Smith"

})
.then(name => {

    cy.log(name)

})
```

Output

```text
John Smith
```

---

# Simulating a Database

Instead of connecting to a real database, return a JavaScript object.

Node

```javascript
on("task", {

    getEmployee(id) {

        return {

            id: id,
            name: "Rahul",
            department: "QA"

        }

    }

})
```

Test

```javascript
cy.task("getEmployee", 101)
.then(employee => {

    expect(employee.id).to.equal(101)

    expect(employee.name).to.equal("Rahul")

})
```

Students now understand the concept without installing MySQL or SQL Server.

---

# Simulating File Reading

Node

```javascript
on("task", {

    readConfig() {

        return {

            url: "https://example.com",
            timeout: 5000

        }

    }

})
```

Test

```javascript
cy.task("readConfig")
.then(config => {

    cy.log(config.url)

})
```

---

# One Important Point

Notice this:

```javascript
cy.task("greet")
```

The string `"greet"` is **not** a function call.

It is simply the **name** of the task.

Cypress searches for a task with that name.

```javascript
on("task", {

    greet() {

        return "Hello"

    }

})
```

These names must match.

---

# What Happens Internally?

```text
Browser

cy.task("square", 8)

        │

        ▼

Node Process

square(8)

        │

return 64

        │

        ▼

Browser

expect(64)
```

---

# Three Rules Students Should Remember

### Rule 1

`cy.task()` always executes in **Node**, **not** in the browser.

---

### Rule 2

A task can receive **one argument** (which can be an object containing multiple values).

```javascript
cy.task("add", {
    a: 10,
    b: 20
})
```

---

### Rule 3

A task should always return something.

```javascript
return result
```

If nothing needs to be returned:

```javascript
return null
```

---

## 5-Minute Classroom Demo

1. Register a task named `greet`.
2. Call it using `cy.task("greet")`.
3. Show that Node returns `"Hello from Node!"`.
4. Modify it to `square(number)`.
5. Pass `8` and receive `64`.
6. Finally, replace `square()` with `getEmployee()` returning a fake employee object.

This progression clearly demonstrates that **`cy.task()` is a bridge between the Cypress test running in the browser and the Node.js process**, without requiring any external setup like databases or file systems.
