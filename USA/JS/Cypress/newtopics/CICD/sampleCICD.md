For beginners, I would keep the CI/CD demo to **15–20 minutes** and avoid explaining YAML in detail. The objective should be:

> **"Whenever a developer pushes code to GitHub, GitHub automatically runs Cypress tests."**

That's enough for their first CI/CD experience.

---

# Architecture

```
VS Code
   │
   ▼
Git
   │
git push
   │
   ▼
GitHub Repository
   │
GitHub Actions (CI)
   │
   ▼
Installs Node
Installs dependencies
Runs Cypress
   │
   ▼
✔ Pass / ✘ Fail
```

---

# Step 1 - Create a tiny Cypress test

Create

```
cypress/e2e/google.cy.js
```

```javascript
describe("Google Test", () => {

    it("opens Google", () => {

        cy.visit("https://www.google.com")

        cy.title().should("contain", "Google")

    })

})
```

Run locally

```
npx cypress run
```

Students already know this.

---

# Step 2 - Push to GitHub

```bash
git add .

git commit -m "Added Cypress test"

git push
```

Nothing new for them.

---

# Step 3 - GitHub Actions

Inside VS Code create

```
.github
    workflows
        cypress.yml
```

Students don't need to understand YAML yet.

Just explain:

> GitHub automatically looks inside `.github/workflows`.

---

# Step 4 - Paste this file

```yaml
name: Cypress Test

on:
  push:

jobs:
  cypress-run:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - run: npm install

      - run: npx cypress run
```

Don't explain every line.

Only say:

* checkout → download project
* setup-node → install Node
* npm install → install packages
* cypress run → execute tests

---

# Step 5 - Commit

```bash
git add .

git commit -m "Added CI"

git push
```

---

# Step 6 - Open GitHub

Open the repository.

Click

```
Actions
```

Students immediately see

```
Running...
```

After a minute

```
✔ Success
```

or

```
❌ Failed
```

This is the "wow" moment.

---

# Step 7 - Break the test

Change

```javascript
cy.title().should("contain", "Google")
```

to

```javascript
cy.title().should("contain", "Microsoft")
```

Commit again

```bash
git add .

git commit -m "Broken test"

git push
```

GitHub now shows

```
❌ Failed
```

Open the logs.

Students can see

```
Expected:

Microsoft

Received:

Google
```

Now explain:

> Nobody had to manually run Cypress. GitHub did it automatically after every push.

---

# What students should learn

1. Write Cypress test in VS Code.
2. Commit changes.
3. Push to GitHub.
4. GitHub automatically runs the tests.
5. Green ✔ means all tests passed.
6. Red ✘ means something is broken.

---

# Teaching Flow (20 minutes)

| Time  | Activity                         |
| ----- | -------------------------------- |
| 5 min | Create one simple Cypress test   |
| 3 min | Push to GitHub                   |
| 5 min | Add GitHub Actions workflow      |
| 3 min | Watch CI run automatically       |
| 4 min | Break the test and watch CI fail |

This is probably the simplest end-to-end CI demo. It avoids deployment (CD), Docker, cloud services, and complex pipelines while giving students a realistic introduction to Continuous Integration.
