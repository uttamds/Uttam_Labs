
<img width="1749" height="984" alt="image" src="https://github.com/user-attachments/assets/e0bd8d62-3272-49e1-950c-f6184a9eed73" />

# Step2
<img width="1891" height="963" alt="image" src="https://github.com/user-attachments/assets/095f2f8a-5185-4276-9ece-cebaa9f3e99b" />

# Step3
<img width="1333" height="773" alt="image" src="https://github.com/user-attachments/assets/0ff87c52-c8cc-4681-9aac-a7e9b9544a53" />

# Step 4

<img width="1240" height="710" alt="image" src="https://github.com/user-attachments/assets/4ac799d3-f0f6-4434-97b6-52e655a488c4" />



After installing Cypress, a simple training flow would be:

### 1. Open Cypress

```bash
npx cypress open
```

Choose:

```
E2E Testing
```

Then select a browser (Chrome/Edge) and click:

```
Create Spec
```

---

### 2. Create Your First Test

Create a file:

```text
cypress/e2e/google.cy.js
```

Add:

```javascript
describe('My First Test', () => {

    it('Visits Google', () => {

        cy.visit('https://www.google.com');

    });

});
```

---

### 3. Run the Test

In the Cypress window, click:

```
google.cy.js
```

The browser should open and navigate to Google.

---

### 4. Add an Assertion

```javascript
describe('My First Test', () => {

    it('Checks Page Title', () => {

        cy.visit('https://www.google.com');

        cy.title().should('contain', 'Google');

    });

});
```

---

### 5. Interact with a Page

Example using a demo site:

```javascript
describe('Login Demo', () => {

    it('Types into fields', () => {

        cy.visit('https://the-internet.herokuapp.com/login');

        cy.get('#username').type('tomsmith');

        cy.get('#password').type('SuperSecretPassword!');

        cy.get('button').click();

    });

});
```

---

### 6. Useful Cypress Commands

```javascript
cy.visit('https://example.com');

cy.get('#id');

cy.get('.class');

cy.get('input');

cy.type('Hello');

cy.click();

cy.check();

cy.uncheck();

cy.select('Option 1');

cy.contains('Submit');

cy.title();

cy.url();
```

---

### 7. Recommended First-Day Cypress Topics

1. What is Test Automation?
2. Why Cypress?
3. Installing Node.js
4. Installing Cypress
5. Cypress Folder Structure
6. Creating First Test
7. `describe()`
8. `it()`
9. `cy.visit()`
10. `cy.get()`
11. `cy.type()`
12. `cy.click()`
13. Assertions with `should()`
14. Running Tests
15. Test Runner

This gives students a working test within the first hour.
