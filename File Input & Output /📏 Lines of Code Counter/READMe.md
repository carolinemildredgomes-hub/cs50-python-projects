# 📏 Lines of Code Counter

A CS50-style Python project designed to strengthen **file I/O, command-line arguments, exception handling, and string processing**.

This project counts the **number of actual lines of code (LOC)** in a Python file while excluding:

- blank lines
- whitespace-only lines
- comment lines beginning with `#`

It helps measure code size and introduces the concept of **basic static code analysis**.

---

## 📌 Project Objective

The goal of this project is to read a Python source file and calculate how many lines contain executable code.

For example:

```python
# Say hello

name = input("What's your name? ")
print(f"hello, {name}")
```

The output should be:

```text
2
```

Because:

- line 1 = comment ❌
- line 2 = blank ❌
- line 3 = code ✅
- line 4 = code ✅

---

## 🛠 Technologies Used

- Python
- `sys`
- File I/O
- Exception Handling
- String Methods

---

## 🧠 Concepts Practiced

- `sys.argv`
- `sys.exit()`
- `try-except`
- `FileNotFoundError`
- `strip()`
- `lstrip()`
- `startswith()`

---

## ▶️ How to Run

```bash
python lines.py filename.py
```

Example:

```bash
python lines.py hello.py
```

---

## 📂 Features

- validates exact command-line arguments
- checks `.py` file extension
- handles missing files safely
- ignores comments
- ignores blank lines
- prints total LOC

---

## 🎯 Learning Outcome

This project builds strong understanding of:

- reading files line-by-line
- text filtering
- basic code parsing
- writing robust CLI tools

---

## 👩‍💻 Author

**Caroline Mildred Gomes**
