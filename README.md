#Student Management System:
The Student Management System is a Python-based program designed to manage student records.
It allows users to:--

1)Add new student records.
2}View all existing student records.
3}Update details of an existing student.
4)Delete student records.
5)Search for a specific student by their Roll Number.
The program ensures persistent storage of data by utilizing a CSV file (students.csv).

#Features:-
1)Add Student:
Allows the user to add a new student record by entering their Roll Number, Name, Age, and Course.
Ensures no duplicate Roll Numbers are added.

2)View All Students:
Displays a list of all student records stored in the CSV file.

3)Update Student:
Lets the user modify an existing student's details (Name, Age, or Course) by specifying their Roll Number.

4)Delete Student:
Enables the user to remove a student record by entering their Roll Number.

5)Search Student:
Searches for and displays a student's details based on their Roll Number.

6)Persistent Storage:
All data is saved in students.csv, ensuring data is not lost between program runs.

Run the program:

python student_management_system.py
Follow the menu options:
Select the desired operation (Add, View, Update, Delete, or Search).
Enter the required inputs as prompted.
Exit the program by selecting option 6.

Project Structure:-

Student-Management-System/
├── students.csv                # CSV file for storing student data
├── student_management_system.py # Main Python script
├── README.md                   # Project documentation
└── .gitignore                  # Ignored files and directories

Example Usage

Adding a Student

Enter your choice: 1
Enter Roll Number: 101
Enter Name: John Doe
Enter Age: 20
Enter Course: Computer Science
Student John Doe added successfully!

Viewing All Students

Enter your choice: 2
Roll No: 101, Name: John Doe, Age: 20, Course: Computer Science

Updating a Student

Enter your choice: 3
Enter Roll Number to Update: 101
New Name (current: John Doe): Johnathan Doe
New Age (current: 20): 21
New Course (current: Computer Science): Data Science
Student with Roll No 101 updated successfully!


