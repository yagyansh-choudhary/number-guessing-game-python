# 🎯 Number Guessing Game

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)](LICENSE)
[![VS Code](https://img.shields.io/badge/IDE-VS%20Code-blue.svg)](https://code.visualstudio.com/)

A fun, interactive, and beginner-friendly console-based number guessing game built with Python. This project was developed as part of the **Computer Science Fundamentals & Career Pathways (ETCCCP105)** course at K.R. Mangalam University.

---

## 📖 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [How to Play](#-how-to-play)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Git Workflow](#-git-workflow)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)

---

## 📝 Description

The **Number Guessing Game** is an engaging console-based game where the computer randomly selects a secret number between 1 and 100, and the player attempts to guess it. After each guess, the game provides intelligent hints indicating whether the guess was "Too High" or "Too Low," guiding the player toward the correct answer.

This project demonstrates fundamental programming concepts including:
- Random number generation
- User input handling and validation
- Conditional logic and control flow
- Loop structures
- Error handling with try-except blocks
- Function-based code organization

The game also features a **performance rating system** that evaluates the player based on the number of attempts taken, encouraging players to improve their guessing strategy.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎲 **Random Number Generation** | Generates a cryptographically random number between 1-100 using Python's random module |
| 💡 **Smart Hint System** | Provides "Too High" or "Too Low" feedback after each guess |
| 🔢 **Attempt Counter** | Tracks and displays the total number of guesses made |
| ⭐ **Performance Rating** | Rates player performance (Excellent/Good/Keep Practicing) based on attempts |
| 🔄 **Replay Functionality** | Option to play multiple rounds without restarting the program |
| ✅ **Input Validation** | Robust error handling for invalid inputs (non-numeric, out of range) |
| 🎨 **User-Friendly Interface** | Clean, decorated console output with emojis and visual separators |
| 🛡️ **Error Handling** | Graceful handling of unexpected inputs using try-except blocks |

---

## 🎬 Demo

```
==================================================
       WELCOME TO THE NUMBER GUESSING GAME
==================================================

I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too High! Try again.

Enter your guess: 25
Too Low! Try again.

Enter your guess: 37
Too High! Try again.

Enter your guess: 31
Too Low! Try again.

Enter your guess: 34

🎉 Congratulations! You guessed it!
The number was 34
Total attempts: 5
Rating: Excellent! 🌟

--------------------------------------------------
Do you want to play again? (yes/no): no

Thank you for playing! Goodbye! 👋
```

---

## 🛠️ Installation

### Prerequisites

Before running this game, ensure you have the following installed:

- **Python 3.x** (Download from [python.org](https://www.python.org/downloads/))
- **Git** (Download from [git-scm.com](https://git-scm.com/downloads))
- **Visual Studio Code** (Recommended IDE - [code.visualstudio.com](https://code.visualstudio.com/))

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/[your-username]/number-guessing-game.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd number-guessing-game
   ```

3. **Verify Python installation**
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

4. **No additional dependencies required!**
   This game uses only Python's built-in `random` module.

---

## 🚀 Usage

### Running the Game

**On Windows:**
```bash
python main.py
```

**On macOS/Linux:**
```bash
python3 main.py
```

### Running from VS Code

1. Open the project folder in VS Code
2. Open `main.py`
3. Press `F5` or click the "Run" button
4. Select "Python File" as the debug configuration
5. The game will start in the integrated terminal

---

## 🎮 How to Play

1. **Launch the game** by running `main.py`
2. **Read the welcome message** - The computer has selected a secret number between 1 and 100
3. **Enter your guess** when prompted
4. **Receive feedback:**
   - `Too High!` - Your guess is greater than the secret number
   - `Too Low!` - Your guess is less than the secret number
5. **Keep guessing** until you find the correct number
6. **View your results:**
   - Total number of attempts
   - Performance rating based on attempts
7. **Choose to play again** or exit the game

### Performance Rating System

| Attempts | Rating |
|----------|--------|
| 1-5 | 🌟 Excellent! |
| 6-10 | 👍 Good! |
| 11+ | 💪 Keep Practicing! |

### Tips for Better Performance

- Start with 50 (middle of the range)
- Use binary search strategy - always guess the middle of the remaining range
- Optimal solution can be achieved in 7 or fewer guesses using binary search

---

## 📸 Screenshots

### Game Welcome Screen
```
==================================================
       WELCOME TO THE NUMBER GUESSING GAME
==================================================
```
*The welcoming interface that greets players when they start the game*

### Gameplay in Progress
```
Enter your guess: 50
Too High! Try again.

Enter your guess: 25
Too Low! Try again.
```
*The hint system guiding the player toward the correct answer*

### Victory Screen
```
🎉 Congratulations! You guessed it!
The number was 34
Total attempts: 5
Rating: Excellent! 🌟
```
*The celebration screen shown when player guesses correctly*

### Play Again Option
```
--------------------------------------------------
Do you want to play again? (yes/no): 
```
*Option to continue playing or exit*

---

## 📁 Project Structure

```
number-guessing-game/
│
├── 📄 main.py                      # Main game source code
├── 📄 README.md                    # Project documentation (this file)
├── 📄 .gitignore                   # Git ignore configuration
│
└── 📁 docs/                        # Documentation folder
    ├── 📄 project_overview.md      # Detailed project overview
    ├── 📄 development_process.md   # Development methodology
    └── 📄 future_improvements.md   # Planned enhancements
```

### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Contains the complete game logic and is the entry point of the application |
| `README.md` | Comprehensive project documentation with installation and usage instructions |
| `.gitignore` | Specifies files and directories that Git should ignore |
| `docs/project_overview.md` | High-level overview of the project objectives and scope |
| `docs/development_process.md` | Detailed explanation of how the project was built |
| `docs/future_improvements.md` | Roadmap for future features and enhancements |

---

## 🔧 Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Programming Language | 3.x |
| ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white) | Integrated Development Environment | Latest |
| ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) | Version Control System | 2.x |
| ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white) | Repository Hosting | - |

### Python Modules Used

- `random` - For generating random numbers (built-in module)

---

## 📊 Git Workflow

### Commit History

This project follows meaningful commit practices with descriptive messages:

| # | Commit Message | Description |
|---|----------------|-------------|
| 1 | `Initial commit: Project structure setup` | Created basic project structure |
| 2 | `Add random number generation and basic game loop` | Implemented core game logic |
| 3 | `Implement user input validation and error handling` | Added try-except blocks |
| 4 | `Add hint system and attempt counter` | Implemented feedback system |
| 5 | `Add play again feature and performance rating` | Added replay functionality |
| 6 | `Add README.md and documentation` | Created comprehensive docs |
| 7 | `Add .gitignore and finalize project` | Cleaned up repository |

### Git Commands Used

```bash
# Initialize repository
git init

# Stage changes
git add .

# Commit with message
git commit -m "Your descriptive message"

# Connect to remote repository
git remote add origin https://github.com/[username]/number-guessing-game.git

# Push to GitHub
git push -u origin main

# View commit history
git log --oneline
```

---

## 🔮 Future Enhancements

### Short-term Goals
- [ ] Add difficulty levels (Easy/Medium/Hard)
- [ ] Implement high score tracking
- [ ] Add time-based challenges

### Medium-term Goals
- [ ] Create GUI using Tkinter
- [ ] Add sound effects
- [ ] Implement multiplayer mode

### Long-term Goals
- [ ] Convert to web application
- [ ] Add database for leaderboards
- [ ] Create mobile version

See [docs/future_improvements.md](docs/future_improvements.md) for detailed roadmap.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes and commit**
   ```bash
   git commit -m "Add: your feature description"
   ```
4. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation if needed

---

## 👨‍💻 Author

**[Yagyansh Singh Ahlawat]**

- 🎓 **Program:** B.Tech CSE (Specialization in AI & Robotics)
- 🏫 **University:** K.R. Mangalam University
- 📧 **Email:** [your.email@example.com]
- 🔗 **GitHub:** [github.com/your-username](https://github.com/your-username)
- 💼 **LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## 🙏 Acknowledgements

- **Faculty:** Prof. Rajesh Kumar - For guidance and course instruction
- **Course:** ETCCCP105 - Computer Science Fundamentals & Career Pathways
- **Institution:** School of Engineering & Technology, K.R. Mangalam University
- **Resources:**
  - [Python Official Documentation](https://docs.python.org/3/)
  - [Git Documentation](https://git-scm.com/doc)
  - [GitHub Guides](https://guides.github.com/)
  - [Visual Studio Code Docs](https://code.visualstudio.com/docs)

---

## 📄 License

This project is created for **academic purposes** as part of the ETCCCP105 coursework at K.R. Mangalam University.

**© 2025 [Yagyansh Singh Ahlawat]. All Rights Reserved.**

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check the documentation** in the `docs/` folder
2. **Open an issue** on GitHub
3. **Contact the author** via email

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

Made with ❤️ by [Yagyansh Singh Ahlawat]

</div>
