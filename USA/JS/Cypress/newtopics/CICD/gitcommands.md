Here are the typical steps to connect a **VS Code project** to a **GitHub repository**.

---

# Step 1: Install Git

Download and install Git from:

* [https://git-scm.com/](https://git-scm.com/)

Verify installation:

```bash
git --version
```

---

# Step 2: Configure Git (One-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Verify:

```bash
git config --list
```

---

# Step 3: Sign in to GitHub from VS Code

1. Open **VS Code**
2. Click the **Accounts** icon (bottom-left or top-right, depending on layout)
3. Select **Sign in to GitHub**
4. Complete the authentication in your browser.
5. Return to VS Code.

---

# Step 4: Open Your Project

```
File
   ↓
Open Folder
```

Select your project folder.

---

# Step 5: Initialize Git (if not already)

Open Terminal:

```bash
git init
```

This creates the hidden `.git` folder.

---

# Step 6: Create a Repository on GitHub

1. Log in to GitHub.
2. Click **New Repository**.
3. Enter a repository name.
4. Click **Create Repository**.

Example:

```
cypress-demo
```

GitHub will display the repository URL, for example:

```
https://github.com/username/cypress-demo.git
```

---

# Step 7: Connect Local Project to GitHub

Copy the repository URL and run:

```bash
git remote add origin https://github.com/username/cypress-demo.git
```

Verify:

```bash
git remote -v
```

Expected output:

```
origin https://github.com/username/cypress-demo.git (fetch)
origin https://github.com/username/cypress-demo.git (push)
```

---

# Step 8: Add Files

```bash
git add .
```

---

# Step 9: Commit

```bash
git commit -m "Initial commit"
```

---

# Step 10: Push to GitHub

For the first push:

```bash
git branch -M main
git push -u origin main
```

After that, future pushes are simply:

```bash
git push
```

---

# Step 11: Verify

Refresh your GitHub repository page.

You should see all your project files.

---

# VS Code Source Control Workflow

Instead of using the terminal:

1. Click the **Source Control** icon.
2. Review changed files.
3. Click **+** to stage changes.
4. Enter a commit message.
5. Click **Commit**.
6. Click **Sync Changes** or **Push**.

---

# Daily Workflow

```text
Modify code
      │
      ▼
git add .
      │
      ▼
git commit -m "Added Login Test"
      │
      ▼
git push
      │
      ▼
GitHub Repository Updated
```

---

## Common Commands

```bash
git status              # Check current status
git add .               # Stage all changes
git commit -m "message" # Commit changes
git push                # Push commits
git pull                # Get latest changes
git remote -v           # Show remote repositories
git log                 # View commit history
```

For a **Cypress project**, these are the only Git commands students typically need to know initially:

* `git init`
* `git status`
* `git add .`
* `git commit -m "..."`
* `git push`
* `git pull`

These six commands cover the most common day-to-day workflow.
