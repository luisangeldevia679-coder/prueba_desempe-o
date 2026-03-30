
import json
import os

FILE_NAME = "students.json"

# -----------------------------
# DATA PERSISTENCE FUNCTIONS
# -----------------------------

def load_students():
    """Load students from JSON file"""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    """Save students to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# -----------------------------
# CRUD FUNCTIONS
# -----------------------------

def add_student(students):
    """Register a new student"""
    try:
        student_id = input("Enter ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        status = input("Enter status (active/inactive): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Error: Age must be a number.")

def show_students(students):
    """Display all students"""
    if not students:
        print("No students registered.")
        return

    for student in students:
        print(student)

def find_student(students):
    """Find a student by ID"""
    student_id = input("Enter ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print(student)
            return student

    print("Student not found.")
    return None

def update_student(students):
    """Update student information"""
    student = find_student(students)

    if student:
        print("Leave blank to keep current value")

        name = input("New name: ")
        age = input("New age: ")
        course = input("New course: ")
        status = input("New status: ")

        if name:
            student["name"] = name
        if age:
            try:
                student["age"] = int(age)
            except ValueError:
                print("Invalid age. Keeping previous value.")
        if course:
            student["course"] = course
        if status:
            student["status"] = status

        print("Student updated successfully!")

def delete_student(students):
    """Delete a student by ID"""
    student_id = input("Enter ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

# -----------------------------
# MENU FUNCTION
# -----------------------------

def menu():
    """Display menu options"""
    options = (
        "1. Add Student",
        "2. Show Students",
        "3. Find Student",
        "4. Update Student",
        "5. Delete Student",
        "6. Exit"
    )

    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    for option in options:
        print(option)

    return input("Choose an option: ")

# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():
    students = load_students()
    choice = ""

    while choice != "6":
        choice = menu()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            save_students(students)
            print("Data saved. Goodbye!")
        else:
            print("Invalid option. Try again.")

# Run program
main()
            