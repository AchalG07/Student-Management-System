from ast import Name
import csv
import os

# File where data is stored
FILE_NAME = "students.csv"

# Check if the file exists and create it if not
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Age", "Course"])

# Add a new student
def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    # Check if student already exists
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll_no:
                print("Student with this Roll Number already exists!")
                return

    # Add student to CSV
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, age, course])
    print(f"Student {Name}added successfully!")

# View all students
def view_students():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        students_found = False
        for row in reader:
            print(f"Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
            students_found = True
        if not students_found:
            print("No students found!")

# Update student details
def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    # Check if student exists
    updated = False
    students = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        students.append(header)
        for row in reader:
            if row[0] == roll_no:
                name = input(f"New Name (current: {row[1]}): ") or row[1]
                age = input(f"New Age (current: {row[2]}): ") or row[2]
                course = input(f"New Course (current: {row[3]}): ") or row[3]
                students.append([roll_no, name, age, course])
                updated = True
            else:
                students.append(row)

    if updated:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print(f"Student with Roll No {roll_no} updated successfully!")
    else:
        print("Student not found!")

# Delete a student
def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    # Check if student exists
    students = []
    deleted = False
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        students.append(header)
        for row in reader:
            if row[0] != roll_no:
                students.append(row)
            else:
                deleted = True

    if deleted:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print(f"Student with Roll No {roll_no} deleted successfully!")
    else:
        print("Student not found!")

# Search a student
def search_student():
    roll_no = input("Enter Roll Number to Search: ")
    found = False
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row[0] == roll_no:
                print(f"Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
                found = True
                break
    if not found:
        print("Student not found!")

# Menu options
def menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

# Main function
def main():
    create_file()
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
