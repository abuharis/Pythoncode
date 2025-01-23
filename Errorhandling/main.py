# Handling a Speicific exception
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Handling multiple exceptions
try:
    data = {"key": "value"}
    print(data["wrong_key"])  # Raises KeyError
except (KeyError, IndexError) as e:
    print(f"Error: {e}")

# Else block
try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("Number must be positive")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"You entered {number}, which is positive!")

# Using finally block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up resources.")
    if 'file' in locals():
        file.close()

# Raising exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")

#Custom exception
class NegativeNumberError(Exception):
    pass

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate the square root of a negative number.")
    return number ** 0.5

try:
    result = square_root(-9)
except NegativeNumberError as e:
    print(f"Error: {e}")

