

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
