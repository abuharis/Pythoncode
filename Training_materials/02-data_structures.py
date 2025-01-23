"""Data strcutures are defined as follows:
    list = []
    dict = {}
    tuple = ()
    set = {}


    list = [1, 'a', True, 1.0, 5]    # list of data types
    dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}    # dictionary of key-value pairs
    tuple = (1, 'a', True, 1.0, 5)    # tuple of data types
    set = {1, 'a', True, 1.0, 5}    # set of data types

CRUD oparations are Create, Read, Update, Delete
Lets perform it on the data types.
"""

#Create a List (C) 
my_list = [1,2,3,4]

#Read elements (R)
my_list[0]
my_list[-1]

# Step 3: Update elements (U - Update)
my_list[1] = "Brian"  # Updating the second student
print("Updated List:", my_list)

# Step 4: Delete elements (D - Delete)
my_list.remove(2)  # Removing by value
print("After Deletion:", my_list)

# Alternative delete by index
del my_list[0]  # Delete by index
print("After deleting first student:", my_list)

# Additional operations
my_list.append("David")  # Adding a new student
print("After adding a student:", my_list)

my_list.pop()  # Removing the last element
print("After popping last student:", my_list)

"""
Dictionaries in Python (CRUD Operations)
Example: Managing a dictionary of student grades
"""

# Step 1: Create a dictionary (C - Create)
student_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print("Initial Dictionary:", student_grades)

# Step 2: Read values (R - Read)
print("Alice's grade:", student_grades["Alice"])  # Access value by key
print("All student grades:", student_grades)  # Read entire dictionary

# Step 3: Update values (U - Update)
student_grades["Bob"] = 80  # Updating Bob's grade
print("Updated Dictionary:", student_grades)

# Step 4: Delete entries (D - Delete)
del student_grades["Charlie"]  # Remove by key
print("After Deletion:", student_grades)

# Additional operations
student_grades["David"] = 88  # Adding a new student
print("After adding a new student:", student_grades)

student_grades.pop("Bob")  # Remove an entry using pop
print("After popping Bob:", student_grades)


"""
Basic Level:

Create a list of your favorite movies and perform CRUD operations.
Create a dictionary of country-capital pairs and perform CRUD operations.
Intermediate Level:

Write a function to search for a specific student in a list.
Write a function to update the grade of a student if their name exists in the dictionary.
Advanced Level:

Implement a program where users can dynamically add or remove elements from a list or dictionary using input commands.
Create a dictionary with nested lists to store multiple subjects and their grades for each student.
"""

#Practice
#Write a function to update the grade of a student if their name exists in the dictionary
def update_student_grade(student_grades, student_name, new_grade):
    """
    Updates the grade of a student if their name exists in the dictionary.

    Parameters:
        student_grades (dict): Dictionary containing student names and grades.
        student_name (str): The name of the student whose grade needs to be updated.
        new_grade (int or float): The new grade to assign to the student.

    Returns:
        str: Message indicating success or failure.
    """
    if student_name in student_grades:
        student_grades[student_name] = new_grade
        return f"Grade updated for {student_name}: {new_grade}"
    else:
        return f"Student {student_name} not found in the records."

# Example dictionary of student grades
grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# Example usage
print(update_student_grade(grades, "Bob", 82))  # Output: Grade updated for Bob: 82
print(update_student_grade(grades, "David", 90))  # Output: Student David not found in the records.

# Check the updated dictionary
print(grades)


#Also operate barreleye.json data and find a value from the dict.