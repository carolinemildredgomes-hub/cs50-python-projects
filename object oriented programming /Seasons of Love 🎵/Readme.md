# CS50 Python — Seasons of Love 🎵

## Explanation Only (No Code)

---

# Problem Overview

This problem asks you to build a program that calculates how many **minutes a person has been alive** from their date of birth until today.

The user enters their birth date in the format **YYYY-MM-DD**.

The program then:

* reads the birth date
* checks whether the format is valid
* calculates the difference between that date and today’s date
* converts the total time into **minutes**
* changes that number into **English words**
* prints the final sentence ending with **“minutes”**

The result should look similar to the song *Seasons of Love* from *Rent*, where time is measured in minutes.

---

# Core Idea Behind the Logic

The main concept is based on **date subtraction**.

Python’s built-in date tools allow one date to be subtracted from another.

When today’s date is subtracted from the birth date, Python gives the total number of **days** between them.

After getting the number of days, the next step is to convert days into minutes.

Since:

* 1 day = 24 hours
* 1 hour = 60 minutes

That means:

* 1 day = 1440 minutes

So the total minutes are found by multiplying the number of days by **1440**.

---

# Why This Is Object-Oriented Programming

This problem belongs to the **Object-Oriented Programming** section because it uses Python’s built-in **classes and objects**.

For example, the `date` structure in Python is a class.

When you create a specific date such as a birth date or today’s date, you are creating an **object (instance)** from that class.

Similarly, when two dates are subtracted, Python returns another object called a **timedelta object**.

So this exercise teaches you how to **use already built class objects**, which is a practical use of OOP.

---

# Input Validation

Another important part of this problem is making sure the program does not crash.

If the user enters an invalid date, such as:

* wrong format
* invalid month
* invalid day
* random text

then the program should exit safely.

This is done through **exception handling**.

The idea is to catch invalid input and stop the program cleanly instead of showing an error traceback.

---

# Converting Numbers into Words

After calculating the total minutes, the number must be converted into **English words**.

For example:

* 525600 → Five hundred twenty-five thousand, six hundred

This is done using the `inflect` library.

A very important requirement from CS50 is that the words must be printed **without the word “and.”**

For example, it should be:

* One hundred twenty

not

* One hundred and twenty

This detail is important for passing the test cases.

---

# Testing Concept

The separate test file is used to verify whether the logic works correctly.

Instead of testing the whole program, we test the helper function that performs the minute conversion.

This makes the program easier to debug and more professional.

Some useful test cases include:

* exactly one year
* exactly one day
* multiple leap years
* correct wording format

This is tested using `pytest`.

---

# Learning Outcome

After finishing this problem, you should clearly understand:

* how Python date objects work
* how object instances are used
* date subtraction
* timedelta results
* converting units
* input validation
* testing functions with pytest
* use of external libraries

This problem is excellent for understanding how **real-world OOP concepts work in Python**.

---

# Prepared By

**Caroline Mildred Gomes**
