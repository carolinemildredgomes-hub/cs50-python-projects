
---

---

# 📘 3) `working` Project README

```markdown
# ⏰ Time Format Converter (WORKING)

A CS50-style Python project based on **Regular Expressions, Helper Functions, and Exception Handling**.

This project converts **12-hour time format** into **24-hour military time**.

---

## 📌 Project Objective

Convert input like:

```text
9 AM to 5 PM


into:

09:00 to 17:00


📌 Supported Formats
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
9:00 AM to 5:00 PM


📌 Features
optional minutes support
AM/PM conversion
leading zero formatting
helper function modularity
raises ValueError
full pytest tests


📌 Concepts Used
re.fullmatch()
optional regex groups
helper functions
ValueError
pytest.raises()


📌 How It Works
Extracts both times using regex
Validates hour and minute range
Converts AM/PM to 24-hour format
Returns formatted output


📌 Run Project
python working.py

📌 Run Tests
pytest test_working.py

📌 Example
Hours: 10:30 PM to 8 AM
22:30 to 08:00


📌 Learning Outcome

This project strengthens:

advanced regex
helper function design
error handling
time conversion logic

