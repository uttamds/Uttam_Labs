
# Session 5

A much better way to teach this is through a **single real-world scenario** instead of isolated command demos.

---

# Use Case: Student Management Portal

Suppose you're testing the **Admin Portal** of an engineering college.

After students register, the admin sees the following table.

| Roll No | Name  | Department | Semester | Status   | Action |
| ------- | ----- | ---------- | -------- | -------- | ------ |
| 101     | Rahul | CSE        | 6        | Active   | Edit   |
| 102     | Priya | ISE        | 6        | Inactive | Edit   |
| 103     | Amit  | ECE        | 5        | Active   | Edit   |
| 104     | Sneha | ME         | 7        | Active   | Edit   |
| 105     | Kiran | CSE        | 5        | Inactive | Edit   |

Your job as a QA Engineer is to verify different aspects of this table.


html file

--------------------------
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Management</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f5f5f5;
        }

        h2 {
            text-align: center;
        }

        table {
            width: 80%;
            margin: auto;
            border-collapse: collapse;
            background: white;
        }

        th {
            background: #007bff;
            color: white;
            padding: 12px;
        }

        td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }

        tr:nth-child(even) {
            background: #f2f2f2;
        }

        button {
            padding: 6px 14px;
            cursor: pointer;
        }
    </style>

</head>

<body>

    <h2>Student Management Portal</h2>

    <table id="studentTable">

        <thead>
            <tr>
                <th>Roll No</th>
                <th>Name</th>
                <th>Department</th>
                <th>Semester</th>
                <th>Status</th>
                <th>Action</th>
            </tr>
        </thead>

        <tbody>

            <tr>
                <td>101</td>
                <td>Rahul</td>
                <td>CSE</td>
                <td>6</td>
                <td>Active</td>
                <td><button>Edit</button></td>
            </tr>

            <tr>
                <td>102</td>
                <td>Priya</td>
                <td>ISE</td>
                <td>6</td>
                <td>Inactive</td>
                <td><button>Edit</button></td>
            </tr>

            <tr>
                <td>103</td>
                <td>Amit</td>
                <td>ECE</td>
                <td>5</td>
                <td>Active</td>
                <td><button>Edit</button></td>
            </tr>

            <tr>
                <td>104</td>
                <td>Sneha</td>
                <td>ME</td>
                <td>7</td>
                <td>Active</td>
                <td><button>Edit</button></td>
            </tr>

            <tr>
                <td>105</td>
                <td>Kiran</td>
                <td>CSE</td>
                <td>5</td>
                <td>Inactive</td>
                <td><button>Edit</button></td>
            </tr>

        </tbody>

    </table>

</body>

</html>
-------------------------

---

# Cypress Test

```javascript
describe("Student Management Table", () => {

    beforeEach(() => {

        cy.visit("https://example.com/student-management")

    })

    it("Validate Student Table", () => {

        //---------------------------------------------------
        // 1. Verify the table has 5 students
        //---------------------------------------------------

        cy.get("table tbody tr")
            .should("have.length", 5)

        //---------------------------------------------------
        // 2. Verify the first student is Rahul
        //---------------------------------------------------

        cy.get("table tbody tr")
            .first()
            .should("contain", "Rahul")

        //---------------------------------------------------
        // 3. Verify the last student is Kiran
        //---------------------------------------------------

        cy.get("table tbody tr")
            .last()
            .should("contain", "Kiran")

        //---------------------------------------------------
        // 4. Verify the third student belongs to ECE
        //---------------------------------------------------

        cy.get("table tbody tr")
            .eq(2)
            .should("contain", "ECE")

        //---------------------------------------------------
        // 5. Read the Department column of second student
        //---------------------------------------------------

        cy.get("table tbody tr")
            .eq(1)
            .find("td")
            .eq(2)
            .should("contain", "ISE")

        //---------------------------------------------------
        // 6. Print all student names
        //---------------------------------------------------

        cy.get("table tbody tr").each(($row) => {

            let studentName = $row.find("td").eq(1).text()

            cy.log(studentName)

        })

        //---------------------------------------------------
        // 7. Count Active students
        //---------------------------------------------------

        let activeCount = 0

        cy.get("table tbody tr").each(($row) => {

            let status = $row.find("td").eq(4).text()

            if (status == "Active") {

                activeCount++

            }

        }).then(() => {

            cy.log("Total Active Students : " + activeCount)

            expect(activeCount).to.equal(3)

        })

        //---------------------------------------------------
        // 8. Click Edit for Sneha
        //---------------------------------------------------

        cy.get("table tbody tr").each(($row) => {

            let student = $row.find("td").eq(1).text()

            if (student == "Sneha") {

                cy.wrap($row)
                    .contains("Edit")
                    .click()

            }

        })

    })

})
```

---

# What Students Learn

| Requirement                  | Cypress Command         |
| ---------------------------- | ----------------------- |
| Count students               | `should("have.length")` |
| First row                    | `first()`               |
| Last row                     | `last()`                |
| Third row                    | `eq()`                  |
| Specific column              | `find()`                |
| Loop every row               | `each()`                |
| Conditional logic            | `if()`                  |
| Click button in matching row | `wrap()` + `contains()` |

---

# Even Better Demo (Feels Like Real Testing)

Instead of only checking values, give them a **story**.

> **Scenario:** The Placement Officer wants to verify the list of eligible students before a campus drive.

### Test Cases

### ✅ Test Case 1

Verify exactly **5 students** are listed.

---

### ✅ Test Case 2

Verify **Rahul** is the first student in the list.

---

### ✅ Test Case 3

Verify the last student is **Kiran**.

---

### ✅ Test Case 4

Print all student names in the Cypress log.

Expected Output

```
Rahul
Priya
Amit
Sneha
Kiran
```

---

### ✅ Test Case 5

Verify there are **3 Active** students.

---

### ✅ Test Case 6

Find **Sneha** and click **Edit**.

---

### ✅ Test Case 7

Verify every student has a non-empty department.

```javascript
cy.get("tbody tr").each(($row)=>{

    let department = $row.find("td").eq(2).text()

    expect(department).to.not.equal("")

})
```

---

### ✅ Test Case 8

Verify every semester is between **1 and 8**.

```javascript
cy.get("tbody tr").each(($row)=>{

    let semester = Number($row.find("td").eq(3).text())

    expect(semester).to.be.within(1,8)

})
```

---

## Why this approach works

Rather than teaching `first()`, `last()`, `eq()`, `find()`, and `each()` as unrelated commands, the students experience them as tools to solve realistic QA tasks:

* **`first()` / `last()`** – Validate boundary records.
* **`eq()`** – Access a specific row or column.
* **`find()`** – Drill into cells within a row.
* **`each()`** – Iterate through records to validate or search.
* **Conditional logic** – Perform actions only when a matching record is found.

This mirrors how Cypress is used in real-world applications, making the concepts easier to understand and remember.


Since your students have just completed forms, assertions, and navigation, **tables are the perfect next topic**. The idea is to teach them **how to locate rows and columns and perform actions based on table data**, rather than memorizing Cypress commands.

---

# Session Plan (55 minutes)

| Time       | Activity                     |
| ---------- | ---------------------------- |
| 5 min      | Quick recap                  |
| **30 min** | **Working with HTML Tables** |
| 15 min     | Hands-on Exercise            |
| 5 min      | Q&A                          |

---

# 30-Minute Coverage – Working with Tables

## Part 1 (5 min) – Why Tables?

Start with real-world examples.

> Where do we see tables?

* Student marks
* Employee list
* Amazon orders
* Bank transactions
* Hospital appointments
* Admin dashboards

Explain:

> Automation engineers rarely test only forms.
> Most applications display data in **tables**.
> We often need to locate one row and perform an action.

Example:

```
ID    Name      City      Status

101   Rahul     Pune      Active
102   Priya     Mysore    Inactive
103   Amit      Delhi     Active
```

Question:

> Click Edit for Rahul.

This becomes today's objective.

---

# Part 2 (5 min) – Understanding HTML Tables

Show a simple table.

```html
<table>

<tr>
<th>ID</th>
<th>Name</th>
<th>City</th>
</tr>

<tr>
<td>101</td>
<td>Rahul</td>
<td>Pune</td>
</tr>

<tr>
<td>102</td>
<td>Priya</td>
<td>Mysore</td>
</tr>

</table>
```

Explain

```
table
   tr  -> row
      td -> column
```

Then inspect using DevTools.

---

# Part 3 (15 min) – Cypress Commands

## 1. Count Rows

```javascript
cy.get("table tbody tr")
```

How many rows?

```javascript
cy.get("table tbody tr")
.should("have.length",3)
```

---

## 2. first()

Get first row.

```javascript
cy.get("table tbody tr")
.first()
```

Verify

```javascript
cy.get("table tbody tr")
.first()
.should("contain","Rahul")
```

---

## 3. last()

```javascript
cy.get("table tbody tr")
.last()
.should("contain","Amit")
```

---

## 4. eq()

Explain indexing.

```
0
1
2
3
```

Example

```javascript
cy.get("table tbody tr")
.eq(1)
.should("contain","Priya")
```

Ask:

What will eq(2) return?

---

## 5. each()

The most useful command.

```javascript
cy.get("table tbody tr").each(($row)=>{

    cy.wrap($row).contains("Active")

})
```

Explain

```
each()

↓

Row 1

↓

Row 2

↓

Row 3
```

Then print text.

```javascript
cy.get("table tbody tr").each(($row)=>{

    cy.log($row.text())

})
```

Students love seeing logs.

---

## 6. find()

Find a specific cell.

```javascript
cy.get("table tbody tr")
.eq(1)
.find("td")
.eq(2)
```

Explain visually

```
Row 2

ID
Name
City

↓

Find td

↓

Take index 2

↓

City
```

---

# Part 4 (5 min) – Real-world Demo

Use a table like:

| ID  | Name  | City   | Status   | Action |
| --- | ----- | ------ | -------- | ------ |
| 101 | Rahul | Pune   | Active   | Edit   |
| 102 | Priya | Delhi  | Inactive | Edit   |
| 103 | Amit  | Mumbai | Active   | Edit   |

Tasks:

### Demo 1

Print every student's name.

```javascript
cy.get("tbody tr").each(($row)=>{

    cy.log($row.find("td").eq(1).text())

})
```

---

### Demo 2

Verify Priya exists.

```javascript
cy.contains("td","Priya")
.should("exist")
```

---

### Demo 3

Click Edit for Rahul.

```javascript
cy.contains("td","Rahul")
.parent()
.contains("Edit")
.click()
```

Students immediately understand why `parent()` is useful.

---

### Demo 4

Count Active students.

Use `each()` and an `if` condition.

```javascript
let count = 0

cy.get("tbody tr").each(($row)=>{

    if($row.text().includes("Active"))
        count++

}).then(()=>{

    cy.log(count)

})
```

Introduce simple logic inside Cypress tests.

---

# 15-Minute Hands-on Exercise

Provide students with a table of 5 students:

| ID  | Name  | Marks | City      | Status   |
| --- | ----- | ----- | --------- | -------- |
| 101 | Rahul | 80    | Pune      | Active   |
| 102 | Priya | 95    | Delhi     | Active   |
| 103 | Amit  | 60    | Mumbai    | Inactive |
| 104 | Kiran | 88    | Bangalore | Active   |
| 105 | Sneha | 72    | Chennai   | Inactive |

### Challenge 1

Print all student names.

---

### Challenge 2

Verify there are exactly 5 rows.

---

### Challenge 3

Verify the first student is Rahul.

---

### Challenge 4

Verify the last student is Sneha.

---

### Challenge 5

Print only the Active students.

---

### Challenge 6 (Bonus)

Click the **Edit** button for **Kiran** (if an Action column is included).

---

## Key Takeaway Slide

By the end of this session, students should be able to:

* Identify table rows (`tr`) and cells (`td`) using browser DevTools.
* Count rows and verify table contents with `have.length`.
* Access specific rows using `first()`, `last()`, and `eq()`.
* Iterate through all rows using `each()`.
* Locate cells within a row using `find()`.
* Build practical automation scenarios such as searching for a record, validating data, and clicking an action button in the correct row.

This keeps the session interactive, realistic, and closely aligned with tasks automation engineers perform on web applications.


# Session 4


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
