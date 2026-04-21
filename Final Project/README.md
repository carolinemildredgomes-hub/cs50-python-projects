# Student Manager CLI Application

#### Video Demo: https://youtu.be/sthyEePb0dY

#### Description:

The Student Manager CLI Application is a Python-based command-line program designed to manage student records efficiently. This project was developed as the final project for CS50P and demonstrates core Python concepts including functions, file handling, data structures, and testing.

The main purpose of this application is to allow users to perform basic student management operations such as adding new students, viewing all stored students, searching for specific students, and deleting student records. The program operates entirely in the terminal, making it lightweight and easy to use without requiring a graphical interface.

## Features:

- Add a new student with name, ID, and GPA
- View all stored student records
- Search for students by name
- Delete a student by ID
- Persistent storage using JSON files

## Project Structure:

- project.py
  This file contains the main logic of the application. It includes the `main()` function, which controls the program flow and user interaction through a menu-driven interface. It also contains helper functions such as:
  - `add_student()` to add new records
  - `search_student()` to find students by name
  - `delete_student()` to remove a student
  - `load_students()` to read data from the JSON file
  - `save_students()` to store data into the JSON file

- test_project.py
  This file contains unit tests for key functions using pytest. It ensures that adding, searching, and deleting students works correctly. Writing tests improves reliability and helps detect errors early.

- requirements.txt
  This file lists any external dependencies required for the project. In this case, no external libraries are needed, so it remains minimal.

## Design Decisions:

One of the key design choices was using a JSON file for data storage instead of a database. JSON is simple, human-readable, and easy to work with in Python. This makes the application more beginner-friendly while still demonstrating file persistence.

Another decision was to use a command-line interface (CLI) rather than a graphical user interface (GUI). This keeps the project focused on core programming concepts and avoids unnecessary complexity.

The program uses a menu-driven approach to improve usability. Users can easily navigate through options without needing to remember commands.

## Challenges Faced:

During development, handling file operations safely was a challenge, especially when the JSON file did not exist. This was solved by using exception handling to return an empty list if the file is not found.

Another challenge was ensuring that data remains consistent after adding or deleting students. This required careful handling of reading and writing data to the file.

## What I Learned:

Through this project, I gained a deeper understanding of:
- Structuring Python programs using multiple functions
- Working with JSON for data storage
- Writing and running tests using pytest
- Handling user input and edge cases
- Organizing a complete Python project

## Future Improvements:

If further developed, this project could include:
- A graphical user interface (GUI)
- Database integration (SQLite)
- User authentication system
- Editing existing student records
- Sorting and filtering features

## Conclusion:

This project demonstrates a complete Python application that integrates multiple programming concepts learned throughout CS50P. It is simple yet functional and serves as a strong foundation for more advanced software development in the future.
