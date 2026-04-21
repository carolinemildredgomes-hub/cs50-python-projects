import json

FILE_NAME = "students.json"


def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            student_id = input("ID: ")
            gpa = float(input("GPA: "))
            add_student(name, student_id, gpa)

        elif choice == "2":
            students = load_students()
            for s in students:
                print(s)

        elif choice == "3":
            keyword = input("Search name: ")
            result = search_student(keyword)
            print(result)

        elif choice == "4":
            student_id = input("Enter ID to delete: ")
            delete_student(student_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def add_student(name, student_id, gpa):
    students = load_students()
    students.append({"name": name, "id": student_id, "gpa": gpa})
    save_students(students)


def search_student(keyword):
    students = load_students()
    return [s for s in students if keyword.lower() in s["name"].lower()]


def delete_student(student_id):
    students = load_students()
    students = [s for s in students if s["id"] != student_id]
    save_students(students)


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


if __name__ == "__main__":
    main()
