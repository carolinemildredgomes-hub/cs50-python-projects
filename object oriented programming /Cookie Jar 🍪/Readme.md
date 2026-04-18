# Cookie Jar 🍪

**CS50 Python — Object-Oriented Programming Project**

This project implements a cookie jar system using Python classes. It demonstrates how to manage state within an object, enforce constraints, and verify behavior with automated tests.

---

## Features

* Customizable capacity for the jar
* Deposit cookies (with overflow protection)
* Withdraw cookies (with underflow protection)
* Visual representation using 🍪 emojis
* Clean error handling with `ValueError`
* Automated tests using `pytest`

---

## How It Works (Conceptual)

* A **Jar** object maintains two key pieces of state:

  * **capacity** (maximum allowed cookies)
  * **size** (current number of cookies)
* Depositing increases the size but must never exceed capacity.
* Withdrawing decreases the size but must never go below zero.
* Converting the jar to a string shows one 🍪 per cookie currently stored.

---

## Example

```text
🍪🍪🍪
```

---

## Project Structure

```text
jar.py
test_jar.py
README.md
```

---

## Setup

Install dependencies (only needed for tests):

```bash
pip install pytest
```

---

## Run Tests

```bash
pytest test_jar.py
```

---

## Testing Strategy

Tests validate:

* Initialization with default and custom capacity
* Rejection of invalid capacity values
* Correct string representation as cookies are added
* Proper handling of deposits (including overflow errors)
* Proper handling of withdrawals (including underflow errors)

---

## Concepts Used

* Object-Oriented Programming (classes, instances, state)
* Encapsulation via properties
* Input validation and exception handling
* Unit testing with `pytest`

---

## Author

**Caroline Mildred Gomes**

---

## Notes

Code for this project is maintained in `jar.py` and `test_jar.py`. This README focuses on usage, structure, and concepts.
