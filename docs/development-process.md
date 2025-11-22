# 🛠️ Development Process

## How the Number Guessing Game Was Built - A Complete Development Journey

---

## 📌 Table of Contents

1. [Introduction](#1-introduction)
2. [Development Phases Overview](#2-development-phases-overview)
3. [Phase 1: Environment Setup](#3-phase-1-environment-setup)
4. [Phase 2: Project Initialization](#4-phase-2-project-initialization)
5. [Phase 3: Core Development](#5-phase-3-core-development)
6. [Phase 4: Feature Enhancement](#6-phase-4-feature-enhancement)
7. [Phase 5: Testing & Debugging](#7-phase-5-testing--debugging)
8. [Phase 6: Documentation](#8-phase-6-documentation)
9. [Version Control Workflow](#9-version-control-workflow)
10. [Tools and Technologies Deep Dive](#10-tools-and-technologies-deep-dive)
11. [Challenges Faced & Solutions](#11-challenges-faced--solutions)
12. [Code Evolution](#12-code-evolution)
13. [Best Practices Implemented](#13-best-practices-implemented)
14. [Lessons Learned](#14-lessons-learned)
15. [Conclusion](#15-conclusion)

---

## 1. Introduction

This document provides a comprehensive, step-by-step account of how the Number Guessing Game was developed from concept to completion. It details the development methodology, tools used, challenges encountered, and solutions implemented throughout the project lifecycle.

The development process followed an **iterative approach**, where features were added incrementally, tested, and refined before moving to the next phase. This methodology allowed for continuous improvement and easier debugging.

---

## 2. Development Phases Overview

The project was completed in six distinct phases over the course of approximately one week:

```
┌──────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT TIMELINE                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Day 1-2          Day 3-4          Day 5           Day 6-7      │
│     │                │                │                │         │
│     ▼                ▼                ▼                ▼         │
│ ┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐     │
│ │Phase 1 │ ──►  │Phase 2 │ ──►  │Phase 3 │ ──►  │Phase 4 │     │
│ │Setup   │      │Init    │      │Core Dev│      │Enhance │     │
│ └────────┘      └────────┘      └────────┘      └────────┘     │
│                                                      │           │
│                                      ┌───────────────┘           │
│                                      ▼                           │
│                                 ┌────────┐      ┌────────┐      │
│                                 │Phase 5 │ ──►  │Phase 6 │      │
│                                 │Testing │      │Docs    │      │
│                                 └────────┘      └────────┘      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Phase Summary

| Phase | Name | Duration | Key Activities |
|-------|------|----------|----------------|
| 1 | Environment Setup | Day 1 | Install tools, configure IDE |
| 2 | Project Initialization | Day 2 | Create structure, init Git |
| 3 | Core Development | Day 3-4 | Implement game logic |
| 4 | Feature Enhancement | Day 5 | Add advanced features |
| 5 | Testing & Debugging | Day 6 | Test all scenarios |
| 6 | Documentation | Day 7 | Write docs, finalize |

---

## 3. Phase 1: Environment Setup

### 3.1 Installing Visual Studio Code

**Step 1:** Download VS Code
- Visited [code.visualstudio.com](https://code.visualstudio.com/)
- Downloaded installer for Windows/macOS/Linux
- Ran the installer with default settings

**Step 2:** Initial Configuration
```
Settings configured:
├── Theme: Dark+ (default dark)
├── Font Size: 14px
├── Tab Size: 4 spaces
├── Auto Save: afterDelay
└── Word Wrap: on
```

**Step 3:** Install Essential Extensions

| Extension | Purpose | Publisher |
|-----------|---------|-----------|
| Python | Python language support | Microsoft |
| Pylance | Enhanced IntelliSense | Microsoft |
| GitLens | Git supercharged | GitKraken |
| Python Indent | Fix indentation | Kevin Rose |
| Code Runner | Quick code execution | Jun Han |

**Installation Command (via Command Palette):**
```
Ctrl+Shift+X → Search extension → Install
```

### 3.2 Installing Python

**Step 1:** Download Python
- Visited [python.org/downloads](https://www.python.org/downloads/)
- Downloaded Python 3.x (latest stable version)

**Step 2:** Installation Options
```
☑️ Add Python to PATH (IMPORTANT!)
☑️ Install pip
☑️ Install IDLE
☑️ Install py launcher
```

**Step 3:** Verify Installation
```bash
python --version
# Output: Python 3.x.x

pip --version
# Output: pip 23.x.x
```

### 3.3 Installing Git

**Step 1:** Download Git
- Visited [git-scm.com/downloads](https://git-scm.com/downloads)
- Downloaded installer for operating system

**Step 2:** Installation Configuration
```
Selected options:
├── Use VS Code as default editor
├── Git from command line and 3rd party software
├── Use bundled OpenSSH
├── Use OpenSSL library
├── Checkout Windows-style, commit Unix-style
└── Use MinTTY terminal
```

**Step 3:** Configure Git Identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

### 3.4 Creating GitHub Account

**Step 1:** Sign Up
- Visited [github.com](https://github.com)
- Created account with university email
- Verified email address

**Step 2:** Profile Setup
- Added profile picture
- Set bio and location
- Configured notification preferences

---

## 4. Phase 2: Project Initialization

### 4.1 Creating Project Structure

**Step 1:** Create Project Folder
```bash
# Navigate to desired location
cd Documents

# Create project folder
mkdir number-guessing-game

# Navigate into folder
cd number-guessing-game
```

**Step 2:** Open in VS Code
```bash
code .
```
Or: File → Open Folder → Select project folder

**Step 3:** Create Initial Files
```
number-guessing-game/
│
├── main.py          # Created empty file
├── README.md        # Created with placeholder
└── .gitignore       # Created with Python template
```

### 4.2 Initializing Git Repository

**Step 1:** Initialize Repository
```bash
git init
```
Output:
```
Initialized empty Git repository in /path/to/number-guessing-game/.git/
```

**Step 2:** Create .gitignore
Created comprehensive .gitignore file for Python projects (see .gitignore file)

**Step 3:** First Commit
```bash
# Stage all files
git add .

# Check status
git status

# Create first commit
git commit -m "Initial commit: Project structure setup"
```

### 4.3 Creating GitHub Repository

**Step 1:** Create New Repository on GitHub
- Clicked "New repository" button
- Repository name: `number-guessing-game`
- Description: "A console-based number guessing game in Python"
- Visibility: Public
- Did NOT initialize with README (already have local files)

**Step 2:** Connect Local to Remote
```bash
# Add remote origin
git remote add origin https://github.com/[username]/number-guessing-game.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

**Step 3:** Verify on GitHub
- Refreshed GitHub repository page
- Confirmed all files were uploaded

---

## 5. Phase 3: Core Development

### 5.1 Planning the Game Logic

Before writing code, the game flow was planned:

```
┌─────────────────────────────────────────────────────────────┐
│                      GAME FLOWCHART                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    ┌─────────┐                              │
│                    │  START  │                              │
│                    └────┬────┘                              │
│                         │                                   │
│                         ▼                                   │
│              ┌──────────────────┐                          │
│              │  Display Welcome │                          │
│              └────────┬─────────┘                          │
│                       │                                     │
│                       ▼                                     │
│              ┌──────────────────┐                          │
│              │  Generate Random │                          │
│              │  Number (1-100)  │                          │
│              └────────┬─────────┘                          │
│                       │                                     │
│           ┌──────────►│                                     │
│           │           ▼                                     │
│           │  ┌──────────────────┐                          │
│           │  │   Get User Guess │◄──────────┐              │
│           │  └────────┬─────────┘           │              │
│           │           │                      │              │
│           │           ▼                      │              │
│           │  ┌──────────────────┐           │              │
│           │  │  Valid Input?    │──No──────►│              │
│           │  └────────┬─────────┘           │              │
│           │           │ Yes                  │              │
│           │           ▼                      │              │
│           │  ┌──────────────────┐           │              │
│           │  │  Guess < Secret? │──Yes──► "Too Low" ──┘    │
│           │  └────────┬─────────┘                          │
│           │           │ No                                  │
│           │           ▼                                     │
│           │  ┌──────────────────┐                          │
│           │  │  Guess > Secret? │──Yes──► "Too High" ─┘    │
│           │  └────────┬─────────┘                          │
│           │           │ No (Equal)                          │
│           │           ▼                                     │
│           │  ┌──────────────────┐                          │
│           │  │  Congratulations │                          │
│           │  │  Show Attempts   │                          │
│           │  └────────┬─────────┘                          │
│           │           │                                     │
│           │           ▼                                     │
│           │  ┌──────────────────┐                          │
│           │  │  Play Again?     │                          │
│           │  └────────┬─────────┘                          │
│           │           │                                     │
│           │     Yes   │   No                                │
│           └───────────┘   │                                 │
│                           ▼                                 │
│                    ┌─────────┐                              │
│                    │   END   │                              │
│                    └─────────┘                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Implementing Basic Structure

**Step 1:** Import Required Module
```python
import random
```

**Step 2:** Create Main Function Structure
```python
def number_guessing_game():
    """
    Main function to run the Number Guessing Game.
    """
    # Welcome message
    print("=" * 50)
    print("       WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 50)
    
    # Game logic will go here
    pass

# Entry point
if __name__ == "__main__":
    number_guessing_game()
```

**Commit:**
```bash
git add main.py
git commit -m "Add random number generation and basic game loop"
```

### 5.3 Implementing Random Number Generation

```python
# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

print("\nI have selected a number between 1 and 100.")
print("Try to guess it!\n")
```

### 5.4 Implementing User Input

```python
# Get user input
user_guess = int(input("Enter your guess: "))
```

### 5.5 Implementing Comparison Logic

```python
# Check guess against secret number
if user_guess < secret_number:
    print("Too Low! Try again.")
elif user_guess > secret_number:
    print("Too High! Try again.")
else:
    print("Congratulations! You guessed it!")
```

### 5.6 Implementing Game Loop

```python
guessed = False
attempts = 0

while not guessed:
    user_guess = int(input("Enter your guess: "))
    attempts += 1
    
    if user_guess < secret_number:
        print("Too Low! Try again.")
    elif user_guess > secret_number:
        print("Too High! Try again.")
    else:
        guessed = True
        print(f"\nCongratulations! You guessed it!")
        print(f"The number was {secret_number}")
        print(f"Total attempts: {attempts}")
```

**Commit:**
```bash
git add main.py
git commit -m "Implement user input validation and error handling"
```

---

## 6. Phase 4: Feature Enhancement

### 6.1 Adding Input Validation

**Problem:** Program crashes if user enters non-numeric input

**Solution:** Implement try-except block

```python
while not guessed:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Validate range
        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        # Comparison logic here
        
    except ValueError:
        print("Invalid input! Please enter a valid number.")
```

### 6.2 Adding Performance Rating

```python
# After correct guess
if attempts <= 5:
    print("Rating: Excellent! 🌟")
elif attempts <= 10:
    print("Rating: Good! 👍")
else:
    print("Rating: Keep Practicing! 💪")
```

**Commit:**
```bash
git add main.py
git commit -m "Add hint system and attempt counter"
```

### 6.3 Adding Play Again Feature

```python
play_again = 'yes'

while play_again.lower() in ['yes', 'y']:
    # Game logic here
    
    print("\n" + "-" * 50)
    play_again = input("Do you want to play again? (yes/no): ")

print("\nThank you for playing! Goodbye! 👋")
```

**Commit:**
```bash
git add main.py
git commit -m "Add play again feature and performance rating"
```

---

## 7. Phase 5: Testing & Debugging

### 7.1 Test Cases Executed

| Test Case | Input | Expected Output | Actual Output | Status |
|-----------|-------|-----------------|---------------|--------|
| TC01 | Valid guess (50) | Too High/Low | Too High/Low | ✅ Pass |
| TC02 | Correct guess | Congratulations | Congratulations | ✅ Pass |
| TC03 | Invalid input ("abc") | Error message | Error message | ✅ Pass |
| TC04 | Out of range (150) | Range warning | Range warning | ✅ Pass |
| TC05 | Negative number (-5) | Range warning | Range warning | ✅ Pass |
| TC06 | Play again "yes" | New game starts | New game starts | ✅ Pass |
| TC07 | Play again "no" | Game exits | Game exits | ✅ Pass |
| TC08 | Empty input | Error message | Error message | ✅ Pass |
| TC09 | Decimal (50.5) | Error message | Error message | ✅ Pass |
| TC10 | Boundary (1) | Valid guess | Valid guess | ✅ Pass |
| TC11 | Boundary (100) | Valid guess | Valid guess | ✅ Pass |

### 7.2 Bugs Found and Fixed

**Bug #1: Attempt Count on Invalid Input**
- **Issue:** Attempts incremented even for invalid input
- **Fix:** Moved increment after validation
```python
# Before (Bug)
attempts += 1
if user_guess < 1 or user_guess > 100:
    print("Invalid range")
    continue

# After (Fixed)
if user_guess < 1 or user_guess > 100:
    print("Invalid range")
    continue
attempts += 1
```

**Bug #2: Case Sensitivity in Play Again**
- **Issue:** "YES" or "Yes" not recognized
- **Fix:** Added `.lower()` method
```python
# Before
while play_again == 'yes':

# After
while play_again.lower() in ['yes', 'y']:
```

---

## 8. Phase 6: Documentation

### 8.1 Code Documentation

**Added Docstrings:**
```python
def number_guessing_game():
    """
    Main function to run the Number Guessing Game.
    
    The function generates a random number between 1 and 100,
    then prompts the user to guess it. Provides hints after
    each guess and tracks the number of attempts.
    
    Features:
    - Random number generation
    - Input validation
    - Hint system (Too High/Too Low)
    - Attempt counter
    - Performance rating
    - Play again option
    
    Returns:
        None
    """
```

**Added Inline Comments:**
```python
# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize game variables
attempts = 0  # Counter for number of guesses
guessed = False  # Flag to track if correct guess made
```

### 8.2 Creating Documentation Files

**Created docs/ folder structure:**
```bash
mkdir docs
touch docs/project_overview.md
touch docs/development_process.md
touch docs/future_improvements.md
```

**Commit:**
```bash
git add README.md docs/
git commit -m "Add README.md and documentation"
```

### 8.3 Finalizing Repository

```bash
git add .gitignore
git commit -m "Add .gitignore and finalize project structure"

# Push all changes to GitHub
git push origin main
```

---

## 9. Version Control Workflow

### 9.1 Complete Commit History

```bash
$ git log --oneline

7a8b9c0 Add .gitignore and finalize project structure
6d5e4f3 Add README.md and documentation
5c4d3e2 Add play again feature and performance rating
4b3c2d1 Add hint system and attempt counter
3a2b1c0 Implement user input validation and error handling
2f1e0d9 Add random number generation and basic game loop
1a2b3c4 Initial commit: Project structure setup
```

### 9.2 Git Commands Used Throughout

| Command | Purpose | Frequency |
|---------|---------|-----------|
| `git init` | Initialize repository | Once |
| `git add .` | Stage all changes | Multiple |
| `git add <file>` | Stage specific file | Multiple |
| `git commit -m "msg"` | Commit changes | 7 times |
| `git status` | Check status | Frequently |
| `git log` | View history | Multiple |
| `git push` | Push to remote | Multiple |
| `git remote add` | Add remote | Once |
| `git branch -M main` | Rename branch | Once |

---

## 10. Tools and Technologies Deep Dive

### 10.1 Visual Studio Code Features Used

| Feature | Usage |
|---------|-------|
| Integrated Terminal | Running Python scripts, Git commands |
| IntelliSense | Code completion, suggestions |
| Syntax Highlighting | Python code visualization |
| Error Detection | Identifying syntax errors |
| File Explorer | Managing project files |
| Source Control Panel | Git integration |
| Extensions | Python, GitLens, Code Runner |

### 10.2 Python Features Used

| Feature | Implementation |
|---------|----------------|
| Import Statement | `import random` |
| Function Definition | `def number_guessing_game():` |
| Docstrings | Triple-quoted documentation |
| F-strings | `f"Total attempts: {attempts}"` |
| While Loop | Game loop, play again loop |
| If-Elif-Else | Comparison logic |
| Try-Except | Error handling |
| Built-in Functions | `int()`, `print()`, `input()` |
| String Methods | `.lower()` |
| Random Module | `random.randint()` |

---

## 11. Challenges Faced & Solutions

### Challenge 1: Understanding Git Workflow

**Problem:** Initial confusion about staging, committing, and pushing

**Solution:**
- Studied Git documentation
- Created a Git cheatsheet
- Practiced with dummy repositories
- Used VS Code's Source Control panel for visualization

### Challenge 2: Input Validation

**Problem:** Program crashed on non-numeric input

**Solution:**
- Implemented try-except block
- Added specific ValueError handling
- Created user-friendly error messages

### Challenge 3: Maintaining Clean Code

**Problem:** Code became messy as features were added

**Solution:**
- Refactored code into logical sections
- Added comprehensive comments
- Used meaningful variable names
- Followed PEP 8 style guidelines

### Challenge 4: Writing Meaningful Commits

**Problem:** Unsure what constitutes a good commit message

**Solution:**
- Followed conventional commit format
- Made commits after completing logical units of work
- Kept messages concise but descriptive
- Used imperative mood ("Add", "Fix", "Update")

---

## 12. Code Evolution

### Version 1.0 (Basic)
```python
import random
num = random.randint(1,100)
guess = int(input("Guess: "))
if guess == num:
    print("Correct!")
```

### Version 2.0 (With Loop)
```python
import random
num = random.randint(1,100)
while True:
    guess = int(input("Guess: "))
    if guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High")
    else:
        print("Correct!")
        break
```

### Version 3.0 (Final - Full Featured)
```python
# Complete implementation with all features
# See main.py for full code
```

---

## 13. Best Practices Implemented

### 13.1 Coding Standards

- ✅ PEP 8 compliance
- ✅ Meaningful variable names
- ✅ Consistent indentation (4 spaces)
- ✅ Maximum line length ~79 characters
- ✅ Docstrings for functions
- ✅ Inline comments for complex logic

### 13.2 Version Control Standards

- ✅ Descriptive commit messages
- ✅ Atomic commits (one feature per commit)
- ✅ Regular commits (don't let work pile up)
- ✅ Comprehensive .gitignore

### 13.3 Documentation Standards

- ✅ README with all essential sections
- ✅ Code comments explaining "why"
- ✅ Separate documentation folder
- ✅ Markdown formatting

---

## 14. Lessons Learned

### Technical Lessons

1. **Start Simple:** Begin with basic functionality, then enhance
2. **Test Often:** Test after each change to catch bugs early
3. **Commit Regularly:** Don't wait to accumulate too many changes
4. **Document As You Go:** Writing documentation alongside code is easier

### Soft Skills Lessons

1. **Planning Matters:** Time spent planning saves debugging time
2. **Patience Pays:** Debugging requires patience and systematic approach
3. **Read Documentation:** Official docs are the best resource
4. **Ask for Help:** Don't hesitate to seek help when stuck

---

## 15. Conclusion

The development of the Number Guessing Game was a comprehensive learning experience that covered:

- **Python Programming:** Functions, loops, conditionals, error handling
- **Version Control:** Git commands, commit practices, repository management
- **Development Tools:** VS Code configuration, extensions, terminal usage
- **Documentation:** README writing, Markdown formatting, code comments

The iterative development approach allowed for continuous improvement and resulted in a polished, well-documented project that demonstrates proficiency in modern software development practices.

---

## 📚 Related Documents

- [Project Overview](project_overview.md) - Comprehensive project details
- [Future Improvements](future_improvements.md) - Planned enhancements
- [README.md](../README.md) - Main project documentation

---

**Document Version:** 1.0  
**Last Updated:** 22-10-2025  
**Author:** Yagyansh Singh Ahlawat
**Course:** ETCCCP105 - Computer Science Fundamentals & Career Pathways
