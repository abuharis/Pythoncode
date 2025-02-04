# Store data in variables
"""
variable unpacking allows you to assign values from iterables (like lists, tuples, or dictionaries) to 
multiple variables in a single statement, enhancing code readability and efficiency.

You can unpack a list or tuple into variables directly:

name = "John Doe"
age = 25

#Storing elements from a list into variables
my_list = [1, 2, 3, 4]
a, b, c, d = my_list

#Storing elements from a tuple into variables
my_tuple = (1, 2, 3, 4)
a, b, c, d = my_tuple

#Storing elements from a dictionary into variables
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
a, b, c, d = my_dict

Ensure that the number of variables on 
the left matches the number of elements in the iterable; otherwise, a ValueError will occur.

#Using the Asterisk (*) Operator:

The * operator allows you to capture multiple items during unpacking, 
which is useful when the number of elements is uncertain.

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5

#In this example, middle captures all items between the first and last elements.

#Unpacking in Function Arguments:

Unpacking is also useful when passing arguments to functions.
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

person_info = ("Alice", 30)
greet(*person_info)  # Output: Hello, my name is Alice and I am 30 years old.

#Unpacking Dictionaries:

For dictionaries, the ** operator unpacks key-value pairs.
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

person = {'name': 'Bob', 'age': 25}
display_info(**person)  # Output: Name: Bob, Age: 25

Variable unpacking is a powerful 
feature that, when used appropriately, can make your Python code more concise and readable.
"""