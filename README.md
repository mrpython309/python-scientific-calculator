# 🧮 Interactive Scientific Calculator & Math Engine

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![UI](https://img.shields.io/badge/UI-Desktop%20%26%20Web-purple.svg)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)

An advanced multi-mode **Scientific Calculator Application** built using **Python 3**. Supports arithmetic, logarithmic, and trigonometric calculations using Python's standard `math` module, robust mathematical error handling, string expression evaluation, and offers both a **Modern Web UI** and a **Desktop Dark-Mode GUI**.

---

## ✨ Features

- **Dual Interfaces**: Sleek **Desktop Tkinter Dark-Mode UI** + Responsive **Web Browser Interface**.
- **Scientific Operations**: Trigonometry (`sin`, `cos`, `tan`), Logarithms (`log10`), Exponentiation (`a^b`), and Square Root (`√x`).
- **Mathematical Error Protection**: Prevents runtime crashes with structured exception handling for `ZeroDivisionError` and negative domain inputs.
- **Session History Logging**: Tracks calculation history in memory.
- **Zero External Dependencies**: Powered purely by standard Python libraries (`math`, `http.server`, `tkinter`).
- **Unit Tested**: Full test suite built with `unittest`.

---

## 🚀 Quick Start & Usage

### 1️⃣ Run the Web UI Application (Recommended)
Launch a local Web Server that opens the interactive web calculator in your browser:
```bash
python app.py
```
> Access at: `http://localhost:5001`

### 2️⃣ Run the Desktop Dark-Mode GUI
Launch the desktop Tkinter application:
```bash
python gui_calculator.py
```

---

## 🧪 Running Unit Tests

```bash
python -m unittest test_calculator.py
```

---

## 📂 Project Architecture

```
python-scientific-calculator/
│
├── app.py                  # Web Server & REST API backend (HTML/CSS/JS frontend)
├── gui_calculator.py       # Desktop Tkinter Dark-Mode UI application
├── calculator.py           # Core OOP calculation engine
├── test_calculator.py      # Unit Test suite
└── README.md               # Project documentation
```

---

## 👤 Author

**Anees Shaikh**
- **GitHub**: [@mrpython309](https://github.com/mrpython309)
- **LinkedIn**: [Anees Shaikh](https://linkedin.com/in/anees-shaikh-a7451a295)
- **Email**: shaikhanees841@gmail.com
