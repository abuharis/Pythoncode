"""
Encapsulation Example
Encapsulation hides the internal details of a class by making attributes private using an underscore _ (convention) or double underscore __ (strict private).
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

"""
Inheritance Example
Inheritance allows creating a new class based on an existing class.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):  # Dog class inherits from Animal
    def make_sound(self):
        return "Bark!"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.make_sound())  # Output: Bark!

"""
Polymorphism Example
Polymorphism allows the same method to have different behaviors based on the object calling it.
"""
class Bird:
    def fly(self):
        return "Birds can fly"

class Ostrich(Bird):
    def fly(self):
        return "Ostriches cannot fly"

birds = [Bird(), Ostrich()]
for bird in birds:
    print(bird.fly())  

# Output:
# Birds can fly
# Ostriches cannot fly
