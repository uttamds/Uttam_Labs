In Cypress, **File Upload** and **File Download** are common real-world browser automation tasks. The important distinction is:

* **Upload:** Cypress helps you put a file into an `<input type="file">`.
* **Download:** Cypress can trigger a download and then verify the downloaded file exists and/or inspect its contents.

---

# 1. File Upload

## WHAT?

File upload means automating a webpage where the user selects a file from their computer.

Typical HTML:

```html
<input type="file" id="resume">
```

A user would normally:

> Click **Choose File → Select resume.pdf → Upload**

In Cypress, we automate this without manually opening the Windows file picker.

---

## WHY do we need it?

File upload is very common in applications:

* Resume upload
* Profile picture
* Documents
* Excel/CSV imports
* PDF uploads
* Bulk data uploads
* Assignment submission

For example, imagine a college placement portal:

```text
Student Registration
-------------------------
Name: Rahul
Email: rahul@gmail.com

Upload Resume: [Choose File]

[Submit]
```

We want Cypress to verify that the upload functionality works.

---

# 2. HOW do we upload?

The commonly used Cypress command is:

```javascript
.selectFile()
```

### Basic example

Suppose the application contains:

```html
<input type="file" id="resume">
```

Cypress:

```javascript
cy.get("#resume")
  .selectFile("cypress/fixtures/resume.pdf")
```

That's it.

The file is selected programmatically.

---

# 3. Where should the file be stored?

A very convenient location is:

```text
cypress/
   fixtures/
       resume.pdf
       profile.jpg
       students.xlsx
```

Then:

```javascript
cy.get("#resume")
  .selectFile("cypress/fixtures/resume.pdf")
```

The `fixtures` folder is commonly used for test data and files.

---

# 4. Complete Upload Test

Suppose we have:

```html
<input type="file" id="resume">
<button id="upload">Upload</button>
```

Test:

```javascript
describe("File Upload", () => {

    it("should upload resume", () => {

        cy.visit("http://localhost:5500/upload.html")

        cy.get("#resume")
          .selectFile("cypress/fixtures/resume.pdf")

        cy.get("#upload").click()

    })

})
```

The flow is:

```text
Visit page
     ↓
Find file input
     ↓
Select file
     ↓
Click Upload
     ↓
Verify result
```

---

# 5. Very important: `.selectFile()` vs old Cypress methods

Older Cypress versions commonly used:

```javascript
cy.get('input[type="file"]')
  .attachFile("resume.pdf")
```

That required the **cypress-file-upload** plugin.

Modern Cypress provides:

```javascript
.selectFile()
```

So for current Cypress teaching, I would teach:

```javascript
cy.get("#file").selectFile("cypress/fixtures/resume.pdf")
```

rather than introducing the plugin first.

---

# 6. Upload multiple files

Suppose HTML allows:

```html
<input type="file" id="documents" multiple>
```

Cypress:

```javascript
cy.get("#documents").selectFile([
    "cypress/fixtures/resume.pdf",
    "cypress/fixtures/certificate.pdf"
])
```

This is useful for applications where multiple documents can be uploaded together.

---

# 7. Upload without clicking the file input

There is another interesting option:

```javascript
cy.get("#upload-area").selectFile(
    "cypress/fixtures/resume.pdf",
    { action: "drag-drop" }
)
```

This is useful for applications having a **drag-and-drop upload area**.

For example:

```text
--------------------------------
|                              |
|    Drag & Drop your file     |
|             here             |
|                              |
--------------------------------
```

Cypress can simulate the drag-and-drop interaction.

---

# 8. What should we VERIFY?

Simply selecting a file doesn't necessarily prove that the application successfully uploaded it.

A good test might verify:

```javascript
cy.get("#fileName")
  .should("contain", "resume.pdf")
```

or:

```javascript
cy.get("#successMessage")
  .should("contain", "File uploaded successfully")
```

So the test should ideally be:

```text
SELECT FILE
     ↓
CLICK UPLOAD
     ↓
VERIFY SERVER/UI RESPONSE
```

---

# 9. File Download

Now the opposite scenario.

## WHAT?

Suppose a webpage contains:

```html
<a href="/files/report.pdf">Download Report</a>
```

A user clicks:

```text
Download Report
       ↓
report.pdf
       ↓
Computer
```

Cypress can automate this and verify the downloaded file.

---

# 10. WHY test downloads?

Downloads are also extremely common:

* Download invoice
* Download report
* Export Excel
* Download PDF
* Download CSV
* Generate payslip
* Download certificate

For example:

```text
Student Portal

[Download Marks Card]
```

We need to test:

> Does clicking the button actually produce the expected file?

---

# 11. HOW do we test downloads?

Suppose:

```html
<a href="/downloads/report.pdf">Download Report</a>
```

Cypress:

```javascript
cy.get("#download")
  .click()
```

Then Cypress can check whether the file exists.

The downloaded files normally go into:

```text
cypress/downloads/
```

So we can use:

```javascript
cy.readFile("cypress/downloads/report.pdf")
```

Example:

```javascript
cy.get("#download").click()

cy.readFile("cypress/downloads/report.pdf")
  .should("exist")
```

---

# 12. Download + Verify File Contents

This becomes more interesting with text-based files.

Suppose the application downloads:

```text
students.csv
```

We can do:

```javascript
cy.get("#download").click()

cy.readFile("cypress/downloads/students.csv")
  .should("contain", "Rahul")
```

Or:

```javascript
cy.readFile("cypress/downloads/students.csv")
  .should("contain", "Bangalore")
```

Now we aren't merely checking:

> "Did a file appear?"

We are checking:

> "Did the correct file/data appear?"

---

# 13. Upload vs Download — Very Important Difference

| Operation             | Cypress approach                          |
| --------------------- | ----------------------------------------- |
| Upload file           | `.selectFile()`                           |
| Upload multiple files | `.selectFile([...])`                      |
| Drag & drop upload    | `.selectFile(..., {action: "drag-drop"})` |
| Click download        | `.click()`                                |
| Check downloaded file | `cy.readFile()`                           |
| Check file contents   | `cy.readFile().should(...)`               |
| Download location     | `cypress/downloads/`                      |

---

# 14. A nice classroom demonstration

I'd teach this as **two separate mini demos**.

### Demo 1 — Upload

Create a simple page:

```html
<h2>Student Resume Upload</h2>

<input type="file" id="resume">

<button id="upload">Upload Resume</button>

<p id="message"></p>
```

Then Cypress:

```javascript
it("Upload Resume", () => {

    cy.visit("http://localhost:5500/upload.html")

    cy.get("#resume")
      .selectFile("cypress/fixtures/resume.pdf")

    cy.get("#upload").click()

})
```

Then add an assertion:

```javascript
cy.get("#message")
  .should("contain", "uploaded")
```

---

### Demo 2 — Download

Page:

```html
<h2>Reports</h2>

<a id="download"
   href="downloads/report.pdf"
   download>
   Download Report
</a>
```

Cypress:

```javascript
it("Download Report", () => {

    cy.visit("http://localhost:5500/download.html")

    cy.get("#download").click()

    cy.readFile("cypress/downloads/report.pdf")
      .should("exist")

})
```

---

# 15. The key concept students should remember

I'd summarize it on the board as:

```text
             FILE HANDLING IN CYPRESS
                     |
          -----------------------
          |                     |
       UPLOAD                DOWNLOAD
          |                     |
    selectFile()             click()
          |                     |
          ↓                     ↓
    File → Application    Application → File
                                |
                                ↓
                           readFile()
```

And the two commands to remember are:

### Upload

```javascript
.selectFile()
```

### Download verification

```javascript
.readFile()
```

**One important teaching point:** Cypress is not really "testing Windows File Explorer." It is testing the **web application's file-handling behavior**. That's why we programmatically select files and verify what the application does with them.
