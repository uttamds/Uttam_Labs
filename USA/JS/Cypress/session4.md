For **Session 4**, I would make it as practical as possible. By the end of this session, students should be able to automate an actual form and understand the most commonly used Cypress assertions.

---

# 1. Assertions in Depth

### Demo Page

Use Cypress Example Site:

```javascript
cy.visit('https://example.cypress.io/commands/assertions')
```

---

## Text Assertion

```javascript
describe('Text Assertion', () => {

    it('checks text', () => {

        cy.visit('https://example.cypress.io/commands/assertions')

        cy.get('.assertion-table')
            .should('contain', 'Chai')

    })

})
```

---

## Exact Text

```javascript
cy.contains('h4', 'Assertions')
```

---

## Visibility

```javascript
cy.get('.assertion-table')
    .should('be.visible')
```

---

## Exist

```javascript
cy.get('.assertion-table')
    .should('exist')
```

---

## Enabled

```javascript
cy.get('.action-email')
    .should('be.enabled')
```

---

## Disabled

```javascript
cy.get('button:disabled')
    .should('be.disabled')
```

---

## Length

```javascript
cy.get('table tbody tr')
    .should('have.length', 3)
```

---

## Class

```javascript
cy.get('.assertion-table')
    .should('have.class', 'table')
```

---

## Attribute

```javascript
cy.get('.action-email')
    .should('have.attr', 'placeholder', 'Email')
```

---

# 2. Navigation and Links

Use

```
https://example.cypress.io
```

---

### Clicking Links

```javascript
describe('Navigation', () => {

    it('visits another page', () => {

        cy.visit('https://example.cypress.io')

        cy.contains('Commands')
            .click()

        cy.url()
            .should('include', '/commands')

    })

})
```

---

### Verify URL

```javascript
cy.url()
    .should('eq', 'https://example.cypress.io/commands')
```

---

### Verify Partial URL

```javascript
cy.url()
    .should('include', '/commands')
```

---

### Go Back

```javascript
cy.go('back')
```

---

### Go Forward

```javascript
cy.go('forward')
```

---

### Reload

```javascript
cy.reload()
```

---

# 3. Working with Input Flows

Use

```
https://example.cypress.io/commands/actions
```

---

### Enter Name

```javascript
cy.get('.action-email')
    .type('student@test.com')
```

---

### Clear Field

```javascript
cy.get('.action-email')
    .clear()
```

---

### Type Again

```javascript
cy.get('.action-email')
    .type('admin@test.com')
```

---

### Check Checkbox

```javascript
cy.get('[type="checkbox"]')
    .first()
    .check()
```

---

### Select Radio

```javascript
cy.get('[type="radio"]')
    .first()
    .check()
```

---

### Select Dropdown

```javascript
cy.get('.action-select')
    .select('apples')
```

---

### Multiple Select

```javascript
cy.get('.action-select-multiple')
    .select(['apples','oranges'])
```

---

# 4. Hooks Recap

```javascript
describe('Hooks Demo', () => {

    before(() => {

        cy.log('Runs Once')

    })

    beforeEach(() => {

        cy.visit('https://example.cypress.io')

    })

    afterEach(() => {

        cy.log('Completed Test')

    })

    it('Test 1', () => {

        cy.contains('Commands')

    })

    it('Test 2', () => {

        cy.contains('Utilities')

    })

})
```

---

# 5. Mini End-to-End Student Form Test

Create a simple HTML page.

```html
<!DOCTYPE html>
<html>

<head>
    <title>Student Form</title>
</head>

<body>

<h2>Student Registration</h2>

<input id="name" placeholder="Name">

<br><br>

<input id="email" placeholder="Email">

<br><br>

<select id="course">
    <option>Python</option>
    <option>Java</option>
    <option>Cypress</option>
</select>

<br><br>

<input type="checkbox" id="agree">

<label>I Agree</label>

<br><br>

<button id="submit">Submit</button>

<p id="msg"></p>

<script>

document.getElementById("submit").onclick=function(){

const n=document.getElementById("name").value;
const e=document.getElementById("email").value;
const c=document.getElementById("course").value;
const a=document.getElementById("agree").checked;

if(n!="" && e!="" && a){

document.getElementById("msg").innerHTML="Registration Successful";

}else{

document.getElementById("msg").innerHTML="Incomplete Form";

}

}

</script>

</body>
</html>
```

---

## Cypress Test

```javascript
describe('Student Registration', () => {

    beforeEach(() => {

        cy.visit('studentForm.html')

    })

    it('registers student', () => {

        cy.get('#name')
            .type('Rahul')

        cy.get('#email')
            .type('rahul@test.com')

        cy.get('#course')
            .select('Cypress')

        cy.get('#agree')
            .check()

        cy.get('#submit')
            .click()

        cy.get('#msg')
            .should('have.text', 'Registration Successful')

    })

})
```

---

# Suggested 1-Hour Flow

| Time   | Topic                                                                                        |
| ------ | -------------------------------------------------------------------------------------------- |
| 10 min | Quick recap: `before`, `beforeEach`, `afterEach`                                             |
| 15 min | Assertions (`contain`, `visible`, `exist`, `enabled`, `disabled`, `length`, `class`, `attr`) |
| 10 min | Navigation (`click`, `url`, `go`, `reload`)                                                  |
| 15 min | Form automation (typing, clearing, checkboxes, radio buttons, dropdowns)                     |
| 10 min | Mini end-to-end student registration test                                                    |

This progression gives students enough exposure to write their first realistic Cypress test while reinforcing the concepts from earlier sessions.
