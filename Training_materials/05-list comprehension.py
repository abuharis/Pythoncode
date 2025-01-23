"""
List Comprehensions as an Alternative to Loops
Python provides a concise way to use loops inside list comprehensions.

Use Case: Generating Discounted Prices (E-Commerce Example)
"""
prices = [100, 200, 300]
discounted_prices = [price * 0.9 for price in prices]
print(discounted_prices)

"""
Explanation:

This applies a 10% discount to all prices in the list.
Useful for bulk price calculations in retail businesses.
"""

#With a condition
numbers = [1, 5, 10, 15, 20, 10, 25]
filtered_numbers = [num for num in numbers if num != 10]

print(filtered_numbers)

"""
Key Takeaways from Loop Use Cases:
Automate repetitive tasks, such as sending emails or processing payments.
Efficient data processing, such as analyzing sales data or stock levels.
Control flow effectively, using break and continue to handle specific conditions.
Enhance decision-making, by iterating through user inputs or event-based systems.
"""

"""
Python Practice Task: Student Management System
Objective:
Create a simple Student Management System using functions, arbitrary arguments, loops, conditional statements, and dictionary CRUD operations.

Task Description:

You need to implement a system to manage student records that allows users to:

Add a new student with details such as name, age, and grades.
View all student records.
Search for a student by name.
Update a student's grade if the student exists.
Delete a student record.
Exit the system.

Task Requirements (What the Students Need to Do):
Define functions to handle each operation:

add_student(name, age, *grades)
view_students()
search_student(name)
update_grade(name, new_grade)
delete_student(name)
Use loops to continuously prompt the user to perform actions.

Include conditions to check for the existence of students before updating/deleting records.

Use dictionary CRUD operations to manipulate student data.

Ensure the program exits gracefully when the user chooses to do so.
"""

# Student data dictionary
students = {
    "Alice": {"age": 20, "grades": [85, 90, 78]},
    "Bob": {"age": 22, "grades": [88, 76, 92]},
}

# Function to add a new student
def add_student(name, age, *grades):
    if name in students:
        print("Student already exists.")
    else:
        students[name] = {"age": age, "grades": list(grades)}
        print(f"Student {name} added successfully.")

# Function to view all students
def view_students():
    if not students:
        print("No students found.")
    else:
        for name, details in students.items():
            print(f"{name} -> Age: {details['age']}, Grades: {details['grades']}")

# Function to search for a student by name
def search_student(name):
    if name in students:
        details = students[name]
        print(f"Name: {name}, Age: {details['age']}, Grades: {details['grades']}")
    else:
        print(f"Student {name} not found.")

# Function to update the grades of an existing student
def update_grade(name, new_grade):
    if name in students:
        students[name]["grades"].append(new_grade)
        print(f"Grade updated for {name}. New Grades: {students[name]['grades']}")
    else:
        print(f"Student {name} not found.")

# Function to delete a student
def delete_student(name):
    if name in students:
        del students[name]
        print(f"Student {name} has been removed.")
    else:
        print(f"Student {name} not found.")

# Main menu to run the system
def student_management_system():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Grade")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grades = list(map(int, input("Enter grades (space-separated): ").split()))
            add_student(name, age, *grades)

        elif choice == "2":
            view_students()

        elif choice == "3":
            name = input("Enter student name to search: ")
            search_student(name)

        elif choice == "4":
            name = input("Enter student name to update grade: ")
            new_grade = int(input("Enter new grade: "))
            update_grade(name, new_grade)

        elif choice == "5":
            name = input("Enter student name to delete: ")
            delete_student(name)

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the student management system
student_management_system()


"""
Explanation of the Code:
Functions used:

add_student(name, age, *grades): Adds a student to the dictionary.
view_students(): Displays all students' details.
search_student(name): Searches and displays a student by name.
update_grade(name, new_grade): Adds a new grade to an existing student.
delete_student(name): Removes a student from the dictionary.
Loop in student_management_system()

Provides a menu-driven interface for users.
Keeps running until the user chooses to exit.
Condition checks:

Prevents duplicate entries.
Validates if a student exists before updating or deleting.
"""

