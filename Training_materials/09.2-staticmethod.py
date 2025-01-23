"""
What is a staticmethod?
A static method is just a function inside a class that does not use any class or object data.

Its like a normal function, but it's placed inside a class for better organization.

Why do we need it?
Use a static method when:

You don't need to use self (which refers to an object).
You don't need to use cls (which refers to the class itself).
You just want to perform a task related to the class but don't need any instance-specific details
"""

#Let's consider a use case without using staticmethod and see why using staticmethod could be helpful.

#Without Static Method Example:
#Imagine we have a class Rectangle that calculates the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Using the class with instance methods
rect = Rectangle(10, 5)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30

"""
In this case, the area and perimeter methods rely on instance data (self.length and self.width) to calculate values. 
This is fine when you are dealing with instance-specific data, and we need to create an object to call these methods.
"""

""""
Use Case Where a Static Method Would Be Helpful:
Now, imagine you want a helper function in the Rectangle class that calculates the area of a rectangle without needing to create an instance of Rectangle. 
This function doesn't need any self data or object-specific attributes — it only requires the length and width.
"""
class Rectangle:
    @staticmethod
    def calculate_area(length, width):
        return length * width

# Call the static method directly using the class name
print(Rectangle.calculate_area(10, 5))  # Output: 50


"""
Key Differences:
Without staticmethod:
You would need to create an instance (rect = Rectangle(10, 5)) just to calculate the area, even though you don't need any instance-specific data.

With staticmethod:
You can call Rectangle.calculate_area(10, 5) without creating an instance because the method doesnt rely on any object data (like self). 
It simply works like a standalone function, but it is organized inside the class.
"""

