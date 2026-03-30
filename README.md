STUDENT MANAGEMENT SYSTEM

DESCRIPTION

This project is a student management system developed in Python that operates through the command line. It allows for the simple and organized management of basic student information.

The system is designed with a modular approach and uses data structures such as lists, dictionaries, and tuples, in addition to implementing data persistence using JSON files.

FEATURES

- Register new students
- Display all students
- Search for students by ID
- Update student information

- Delete students
- Automatically save and load data

DATA STRUCTURE

The system uses:

° *Lists* - to store multiple students
° *Dictionaries* - to represent each student
° *Tuples* - to handle menu options

Example student:

{
"ID": "001",
"Name": "Luis",
"Course": "Python",
"Status": "Active"
}

*EXAMPLE OF USE*
1. Select option 1 to add a student
2. Enter the requested data
3. Use option 2 to view all students
4. Use option 3 to search by ID
5. Use option 4 to update information
6. Use option 5 to delete a student

*Data Persistence*
| Data is stored in the Students.json file
| The system automatically loads the information upon startup
| Changes are saved upon exiting the program.

*Error Handling*
The system includes basic validations such as:

- Error control in data entry (e.g., numerical age)
- Clear messages for the user
- Prevention of crashes that halt the program

*Best Practices Implemented*

° Modular code organized by function
° Separation of responsibilities (services, utilities)
° Clear and descriptive names
° Comments in the code

AUTHOR
Project developed as part of the Performance Test - Module 1 Python