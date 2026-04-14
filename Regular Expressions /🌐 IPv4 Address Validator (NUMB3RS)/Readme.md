# 🌐 IPv4 Address Validator (NUMB3RS)

A CS50-style Python project focused on **Regular Expressions, String Parsing, and Input Validation**.

This project validates whether a given string is a **valid IPv4 address**.

---

## 📌 Project Objective

The goal of this project is to check whether a user-provided IP address follows the correct **IPv4 format**.

A valid IPv4 address must:

- contain exactly **4 numeric parts**
- be separated by **dots (`.`)**
- each number must be between **0 and 255**
- must not contain **leading zeros**

Example:

```text
127.0.0.1 → Valid
275.3.6.28 → Invalid


📌 Features
Regex-based format checking
Dot-separated value validation
Range checking (0–255)
Leading zero detection
Pytest test coverage

📌 Concepts Used
re.fullmatch()
string splitting
loops
conditionals
integer validation
pytest unit testing

📌 How It Works
Validates basic IPv4 pattern using regex
Splits the address by dots
Checks there are exactly 4 parts
Ensures every part is numeric
Validates range 0–255
Rejects leading zeros

📌 Run Project
python numb3rs.py

📌 Run Tests
pytest test_numb3rs.py

📌 Example
IPv4 Address: 127.0.0.1
True


📌 Learning Outcome

This project strengthens understanding of:

regex validation
structured input parsing
test-driven development
