
# Git

### Local Repository

* A copy of the project stored on your computer.
* Tracks all changes and versions locally.
* Allows working without an internet connection.

### Staging Area (Index)

* Temporary area before committing.
* Used to choose which changes should be included in the next commit.
* Command:

```bash
git add filename
```

### Commit History

* Record of all commits made in the repository.
* Helps track who changed what and when.
* View history:

```bash
git log
```

### Branching

* Creates independent lines of development.
* Allows new features or fixes without affecting the main project.
* Commands:

```bash
git branch feature
git switch feature
```

#### main Branch

* Default and stable branch.
* Contains production-ready code.

#### feature Branch

* Used for developing a new feature or bug fix.
* Later merged into `main`.

---

# GitHub

### Remote Repository

* Online copy of your Git repository.
* Used for backup, collaboration, and sharing code.

### Pull Requests (PR)

* Request to merge one branch into another.
* Used for discussion and approval before merging.

### Code Review

* Team members examine code before it is merged.
* Improves code quality and catches bugs.

### Issues

* Used to report bugs, request features, or track tasks.
* Helps organize project work.

### Actions

* GitHub's automation platform (CI/CD).
* Automatically builds, tests, or deploys code when events occur.

---

# Workflow

### Clone

* Copies a remote repository to your local machine.

```bash
git clone <repository-url>
```

### Add

* Moves modified files to the staging area.

```bash
git add .
```

### Commit

* Saves staged changes into the local repository.

```bash
git commit -m "Meaningful message"
```

### Push

* Uploads local commits to GitHub.

```bash
git push
```

### Pull

* Downloads and merges the latest changes from GitHub.

```bash
git pull
```

### Merge

* Combines changes from one branch into another.

```bash
git merge feature
```

---

## Typical Git & GitHub Workflow

```
Clone Repository
       ↓
Create Feature Branch
       ↓
Edit Files
       ↓
git add
       ↓
git commit
       ↓
git push
       ↓
Create Pull Request
       ↓
Code Review
       ↓
Merge into main
       ↓
Others git pull
```

### One-line Summary

* **Git** → Version control software that tracks code changes locally.
* **GitHub** → Cloud platform that hosts Git repositories and enables team collaboration.
* **Workflow** → The sequence of Git commands developers use to collaborate efficiently.
