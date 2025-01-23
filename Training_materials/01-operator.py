""""Operators perform operations on data types. There are mainly 4 data types in Python:
1. String: represented by single, double or tripple quotes.
2. Integer: whole numbers.
3. Float: decimal numbers.
4. Boolean: True or False.

Operators are used to perform operations on these data types.
Every operation requires operands (one or more operands).
The outcome of an operation will be a data type or data structure.

The data structures are:
List: Mutable data type. Can contain different data types.
Tuple: Immutable data type. Can contain different data types.
Dictionary: Mutable data type. Can contain different data types.
Set: Mutable data type. Can contain different data types.

The operations are:
Arithmetic operators: +, -, *, /, %, **, //   : on numbers
Assignment operators: =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=, ~= : on variables: retruns the value
Comparison operators: ==, !=, >, <, >=, <= : on numbers and strings: retruns a bool
Logical operators: and, or, not :returns a bool
Membership operators: in, not in: returns a bool
Identity operators: is, is not: returns a bool
"""

#Examples

#Boolean operators (and, or, not)

#Checking user access
user = input("Enter your username: ")
password = input("Enter your password: ")

if user == "abuharis" and password == "1234":
    print("Access granted")
else:
    print("Access denied")

#Membership operators (in, not in)

#List
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)

#String
my_string = "Hello world"
print("world" in my_string)
print("World" not in my_string)

#Identity operators (is, is not)

#Checking if two variables are the same object. Also if the object in memory is the same
x = 5
y = 5
print(x is y)
print(x is not y)

#Comparison operators (==, !=, >, <, >=, <=)

#Checking if two variables are equal
x = 5   
y = 6
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Practice task from real use cases
# Create a program that checks if a user is an admin or not.
# Create a program that checks if a user is logged in or not.   
# Create a program that checks if a user is logged in and is an admin or not.  
     