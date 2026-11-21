# python_pr7


# PR. 7 - Moduler & Packager
## Multi-Utility Toolkit | Python - Data Science

A Python-based menu-driven toolkit that demonstrates the use of **Modules, Packages, `__name__` and `__main__`, and `dir()`**.

This project is built for learning how Python organises code into reusable modules and packages, and how built-in modules like `datetime`, `math`, `random`, and `uuid` can solve real-world problems.

---

## 📁 Project Structure

```
Multi_Utility_Toolkit/
│
├── main.py                  # Main menu-driven program
├── README.md                # Project documentation
│
└── my_toolkit/              # Custom Package
    ├── __init__.py          # Package initializer
    ├── datetime_tools.py    # Datetime & Time operations
    ├── math_tools.py        # Mathematical operations
    ├── random_tools.py      # Random data generation
    ├── uuid_tools.py        # UUID generation
    ├── file_tools.py        # Custom Module - File Operations
    └── convert_tools.py     # Custom Module - Unit Conversions
```

---

## ✨ Features

### 1. Datetime and Time Operations
- Display current date and time in user-friendly format
- Calculate difference between two dates
- Format dates into custom formats using `strftime`
- Simple Stopwatch
- Countdown Timer

### 2. Mathematical Operations
- Factorial using `math` module
- Compound Interest calculation
- Trigonometric calculations - sin, cos, tan, sqrt, log
- Area of Geometric Shapes - Circle, Rectangle, Triangle

### 3. Random Data Generation
- Generate random numbers
- Generate random lists and random sampling
- Create random passwords
- Generate random OTPs
- Dice game simulation

### 4. Generate Unique Identifiers (UUID)
- Generate UUID4 and UUID1
- Invoice ID example - `INV-XXXXXXXX`
- User Session ID example

### 5. File Operations (Custom Module)
- Create a new file
- Write to a file
- Read from a file
- Append to a file

### 6. Unit Conversions (Custom Module)
- Km to Miles
- Celsius to Fahrenheit

### 7. Dynamic Module Exploration
- Explore available attributes of any built-in or custom module using `dir()`
- Example: `math`, `random`, `datetime`, `uuid`

---

## 🚀 How to Run

### Step 1: Open Project
VS Code ma `Multi_Utility_Toolkit` folder kholo.

### Step 2: Run Command
Terminal ma aa command lakho:

```bash
python main.py
```

Jo `python` command na chale to:

```bash
py main.py
```

### Step 3: Use Menu
```
==============================
Welcome to Multi-Utility Toolkit
==============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Unit Conversions (Custom Module)
7. Explore Module Attributes (dir())
8. Exit
==============================
```

---

## 🖥️ Example Console Interaction

### Main Menu:
```
Enter your choice: 1
```

### Datetime Menu:
```
Datetime and Time Operations:
1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu

Enter your choice: 1
Current Date and Time: 2025-01-04 10:15:30

Enter your choice: 2
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days
```

### Maths Menu:
```
Enter your choice: 1
Enter a number: 5
Factorial: 120

Enter your choice: 2
Enter principal amount: 1000
Enter rate of interest (in %): 5
Enter time (in years): 2
Compound Interest: 1102.50
```

### Random Menu:
```
Enter your choice: 3
Enter password length: 8
Generated Password: Kd8@qzP!
```

### UUID:
```
Generated UUID: f47ac10b-58cc-4372-a567-0e02b2c3d479
```

### File Operations:
```
Enter your choice: 1
Enter file name: example.txt
File created successfully!

Enter your choice: 2
Enter file name: example.txt
Enter data to write: This is a sample file.
Data written successfully!
```

### Explore Module:
```
Enter module name to explore: math
Available Attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan', ...]
```

---

## 🧩 Concepts Used

| Concept | Use in Project |
| :--- | :--- |
| **Module** | Ek `.py` file, jem ke `math_tools.py` |
| **Package** | Ghana modules no group, `my_toolkit` folder |
| **`__init__.py`** | Folder ne package banave che |
| **`__name__` and `__main__`** | File direct run thay to j `main()` chale, import thay to na chale |
| **`dir()`** | Koi pan module ma kaya kaya functions che te batave che |
| **Built-in Modules** | `datetime`, `math`, `random`, `uuid`, `time` |
| **Custom Modules** | `file_tools.py`, `convert_tools.py` |

---

## 💼 Example Use Case

A small business owner uses the toolkit to manage daily operations:
- Calculate working hours using the time module
- Generate random passwords for their team
- Assign unique identifiers to invoices using UUID
- Save all logs and outputs into text files via custom module
- Dynamically explore capabilities of toolkit using `dir()`

---

## 🛠️ Requirements

- Python 3.8 or above
- No external library needed - badha built-in modules che
- VS Code / Any Python IDE

---

## 📝 Assumptions

1. User dates `YYYY-MM-DD` format ma nakhse.
2. Password ane OTP demo purpose mate che, real security mate nahi.
3. File operations current folder ma j file banavse.
4. Stopwatch ane Countdown mate user Enter dabavse.

---

## 👨‍💻 Author

**Project:** PR. 7 Moduler & Packager
**Subject:** PYTHON - DATA SCIENCE
**Topic:** Modules, Packages, Custom Modules, `__name__` & `__main__`, `dir()`

---

## 📌 Submission

1. GitHub repository ma aa badhi files upload karo
2. README.md ne repo na main page par rakho
3. Repository link instructor ne submit karo
