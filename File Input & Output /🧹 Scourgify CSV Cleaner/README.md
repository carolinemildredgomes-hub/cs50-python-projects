# 🧹 Scourgify CSV Cleaner

A CS50-style Python project designed to strengthen **CSV processing, file transformation, and data cleaning skills**.

This project reformats student data from a CSV file by splitting full names into separate **first** and **last** name columns.

---

## 📌 Project Objective

Input file format:

```csv
name,house
"Potter, Harry",Gryffindor
"Malfoy, Draco",Slytherin
```

Output file format:

```csv
first,last,house
Harry,Potter,Gryffindor
Draco,Malfoy,Slytherin
```

This project simulates a real-world **data cleaning and preprocessing task**.

---

## 🛠 Technologies Used

- Python
- `csv`
- `sys`
- File I/O
- Exception Handling

---

## 🧠 Concepts Practiced

- `csv.DictReader`
- `csv.DictWriter`
- `writeheader()`
- dictionaries
- string splitting
- file writing
- exception handling

---

## ▶️ How to Run

```bash
python scourgify.py before.csv after.csv
```

---

## 📂 Features

- reads structured CSV data
- splits full names into separate columns
- writes clean CSV output
- preserves house data
- validates file existence
- handles incorrect arguments

---

## 🎯 Learning Outcome

This project teaches:

- structured data transformation
- CSV parsing
- practical data cleaning
- preprocessing for real-world applications

---

## 👩‍💻 Author

**Caroline Mildred Gomes**
