Phone: 7760870005

**So, what is JavaScript? And where do we use it?**

JavaScript, often called **JS**, is a programming language that makes web pages interactive.

Imagine a website without JavaScript.

You open a page... you click a button... nothing happens.
You type your username... nothing checks it.
You press "Submit"... no response.

Not very exciting, right?

JavaScript brings life to websites.

We use JavaScript for:

* Showing messages
* Handling button clicks
* Validating forms
* Creating games
* Building web applications
* Creating mobile apps
* Even backend development

Now let me ask you:

**If HTML builds the house, and CSS paints the house... what does JavaScript do?**

JavaScript makes the house *work*.

It turns on the lights, opens the doors, and makes things move.

---

**Let's write our first JavaScript code.**

```javascript
console.log("Hello World");
```

What does this do?

`console.log()` displays output in the console.

Think of it as JavaScript speaking to us.

Output:

```text
Hello World
```

Now let's change it.

```javascript
console.log("My name is Ravi");
```

Output:

```text
My name is Ravi
```

Question:

What happens if I change Ravi to Priya?

Correct.

The output changes too.

---

Now suppose I want JavaScript to remember something.

Maybe a student's name.

For that we use **variables**.

```javascript
let studentName = "Ravi";

console.log(studentName);
```

Output:

```text
Ravi
```

Think of a variable as a box.

The box has a name:

**studentName**

Inside the box:

**Ravi**

Let's change it.

```javascript
let studentName = "Priya";

console.log(studentName);
```

Output:

```text
Priya
```

Question:

Can a box store numbers too?

Yes.

```javascript
let age = 20;

console.log(age);
```

Output:

```text
20
```

---

Now let's make JavaScript do some math.

```javascript
let a = 10;
let b = 5;

console.log(a + b);
```

Output:

```text
15
```

Try guessing before running:

```javascript
console.log(a - b);
```

Output?

Correct:

```text
5
```

What about:

```javascript
console.log(a * b);
```

Output:

```text
50
```

---

Now imagine asking JavaScript a question.

"Is Ravi an adult?"

```javascript
let age = 20;

console.log(age >= 18);
```

Output:

```text
true
```

Try another one:

```javascript
let age = 12;

console.log(age >= 18);
```

Output:

```text
false
```

JavaScript can answer questions with:

* `true`
* `false`

---

So today we learned:

✔ What JavaScript is
✔ Where it is used
✔ `console.log()`
✔ Variables
✔ Numbers and text
✔ Basic calculations
✔ Simple conditions

And now a small challenge:

Predict the output before running:

```javascript
let x = 5;
let y = 3;

console.log(x + y);
console.log(x * y);
console.log(x > y);
```

Let's see who gets all three correct!

Got it. Replacing with American names:

### JS Variables

* Variables are used to **store values/data** in JavaScript.
* Think of a variable as a **container or box** that holds information.
* Variable names should be meaningful.

Example:

```javascript
let studentName = "John";
let age = 20;
```

Here:

* `studentName` stores text
* `age` stores a number

---

### JS Data Types (General)

JavaScript can store different kinds of data.

**String** → Text values

```javascript
let name = "John";
```

**Number** → Numeric values

```javascript
let marks = 95;
```

**Boolean** → True or False values

```javascript
let isPassed = true;
```

**Undefined** → Variable declared but no value assigned

```javascript
let city;

console.log(city);
```

**Null** → Intentionally empty value

```javascript
let phone = null;
```

---

### JS Arrays

* Arrays store **multiple values in a single variable**.
* Array elements are stored using **index positions**.
* Index starts from **0**.

Example:

```javascript
let fruits = ["Apple", "Mango", "Orange"];

console.log(fruits[0]);
console.log(fruits[1]);
```

Output:

```text
Apple
Mango
```

---

### The `var` Keyword

* `var` was the older way of creating variables in JavaScript.
* Nowadays `let` and `const` are preferred.
* `var` can be **redeclared**, which can sometimes create confusion.

Example:

```javascript
var name = "John";

var name = "Emma";

console.log(name);
```

Output:

```text
Emma
```

Modern approach:

```javascript
let name = "John";
const country = "USA";
```

* `let` → value can change
* `const` → value should not change
* `var` → older style, generally avoided in modern JavaScript development.

