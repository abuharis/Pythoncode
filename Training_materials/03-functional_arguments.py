"""
When defining and calling functions, arguments allow us to pass data into functions to make them more flexible and reusable. 
Python provides different ways to pass arguments, including positional arguments, keyword arguments, and flexible arguments like *args and **kwargs.
"""

"""
1. Positional Arguments
Positional arguments are the most common type and are assigned based on their position in the function call.
Example:
"""

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)  # Output: Hello, Alice! You are 25 years old.
greet(25, "Alice")  # Wrong order, may produce unexpected results.

"""When to Use:
When the order of arguments is clear and consistent.
For simple functions with a few parameters.
"""


"""
Keyword Arguments
Keyword arguments allow you to pass values using parameter names, making the function call more readable and flexible.
"""

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Bob")  # Output: Hello, Bob! You are 30 years old.

"""
Advantages of Keyword Arguments:
Order of arguments does not matter.
Improves readability of the code.
Useful when functions have many parameters.
"""

"""
Default Arguments
Default arguments allow setting default values for parameters, which will be used if no value is provided during the function call.
"""

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")  # Output: Hello, Alice! You are 18 years old.
greet("Bob", 25)  # Output: Hello, Bob! You are 25 years old.


"""
When to Use:
When a function parameter should have a sensible default.
To make function calls shorter and more convenient.
"""

"""
Arbitrary Arguments (*args)
*args allows passing multiple positional arguments to a function as a tuple.
"""

def add_numbers(*args):
    total = sum(args)
    print(f"Total sum: {total}")

add_numbers(10, 20, 30)  # Output: Total sum: 60
add_numbers(5, 15)       # Output: Total sum: 20


"""
When to Use:
When the number of arguments is unknown.
Useful for functions like sum(), min(), max(), etc.
"""

"""
Arbitrary Keyword Arguments (**kwargs)
**kwargs allows passing multiple keyword arguments as a dictionary.
"""

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=22, course="Python")
# Output:
# name: Alice
# age: 22
# course: Python


"""
When to Use:
When dealing with optional parameters.
Useful in situations where additional named parameters might be passed.
"""

"""
Combining Different Types of Arguments
You can mix different types of function parameters, but the order should be:

Positional arguments
*args (arbitrary positional arguments)
Keyword arguments
**kwargs (arbitrary keyword arguments)
"""

def show_details(name, *args, age=18, **kwargs):
    print(f"Name: {name}, Age: {age}")
    print("Subjects:", args)
    print("Additional Info:", kwargs)

show_details("Alice", "Math", "Science", age=20, city="NY", grade="A")


"""
Why Use Arguments and Keyword Arguments?
Flexibility: Allows writing reusable functions that can handle various inputs.
Readability: Keyword arguments improve readability by specifying parameter names.
Maintainability: Default values help reduce the need for multiple function overloads.
Scalability: *args and **kwargs help build functions that accept an arbitrary number of parameters.
"""

"""
Practices
1. Write a function to calculate the total cost of items with optional tax percentage using default arguments.
2. Create a function that takes multiple student names using *args and prints them.
3. Design a function to accept personal details (name, age, country) and additional info using **kwargs.
"""



