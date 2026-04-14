
---

---

# 📘 4) `um` Project README

```markdown
# 🗣️ Word Counter Using Regex (UM)

A CS50-style Python project based on **Regular Expressions and Word Boundary Matching**.

This project counts how many times the word **"um"** appears as a standalone word.

---

## 📌 Project Objective

Count occurrences of `"um"` case-insensitively, only as a whole word.

Example:

```text
"Um, thanks, um..."
→ 2



📌 Features
case-insensitive matching
word boundary detection
ignores substrings inside words
pytest testing


📌 Concepts Used
re.findall()
\b word boundary
re.IGNORECASE


📌 How It Works
Finds all standalone "um" matches
Ignores words like album, yummy
Returns total count

📌 Run Project
python um.py


📌 Run Tests
pytest test_um.py


📌 Example
Text: Um, thanks, um...
2


📌 Learning Outcome

This project builds strong understanding of:

regex boundaries
whole-word matching
counting occurrences

