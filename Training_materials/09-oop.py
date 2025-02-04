"""
Key OOP Concepts

Class: A blueprint for creating objects (defines attributes and methods).
Object: An instance of a class.

Features of OOP

Encapsulation: Bundling of data and methods within a class.
Abstraction: Hiding complex implementation details and exposing only the necessary parts.
Inheritance: Reusing code by creating new classes from existing ones.
Polymorphism: Using a single interface to represent different types.
"""

#Step 1: Defining a Simple Class
class Person:
    pass  # Empty class for now

#Stripping Down the __init__ Method
#The __init__ method is a special method (constructor) that runs automatically when an object is created. It is used to initialize the object's attributes.
class Person:
    def __init__(self, name, age):  
        # 'self' refers to the instance of the class
        self.name = name  # Instance variable
        self.age = age    # Instance variable

"""
self refers to the specific instance of the class.
name and age are attributes assigned to the instance.
The constructor method runs once when an object is instantiated.
"""

# Creating an object of a class
person1 = Person("Alice", 25)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 25

"""
Why do we use __init__?

The __init__ method is not required for every class, but it is commonly used to initialize instance attributes when an object is created.

The __init__ method allows you to:
1. Automatically set up attributes when an object is created.
2. Ensure each object starts with the correct initial values.
3. Avoid manually assigning values after object creation. 
"""

"""
Is it required in every class?
No, if your class does not require any attributes to be initialized when an object is created, you can skip the __init__ method.
"""

"""
Class Attributes vs. Instance Attributes
Class Attributes:

Shared across all instances of a class.
Defined directly in the class, outside any methods.
Changing a class attribute affects all instances unless specifically overridden in an instance.
Instance Attributes:

Unique to each instance of the class.
Defined inside the __init__ method using self.
Changing an instance attribute only affects that specific object."""
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model  # Instance attribute

# Accessing attributes
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

#Methods in a Class
#A method is a function defined inside a class that operates on its objects.
class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def display_info(self):  # Method to print details
        print(f"Student: {self.name}, Grade: {self.grade}")


#Other Commonly Used Methods in Classes

#1. Instance Methods
#Methods that operate on the instance (self) and can modify object properties.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

student1 = Student("John", 85)
student1.update_marks(90)  # Updating marks
print(student1.marks)  # Output: 90

#Class Methods (@classmethod)
"""Used to work with class-level attributes (shared among all instances).
Defined with @classmethod and takes cls as the first parameter.
"""
class Employee:
    company_name = "Tech Corp"  # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_company(cls, new_name):
        cls.company_name = new_name

emp1 = Employee("Alice")
emp2 = Employee("Bob")

Employee.update_company("New Tech Corp")

print(emp1.company_name)  # Output: New Tech Corp
print(emp2.company_name)  # Output: New Tech Corp
