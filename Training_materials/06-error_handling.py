"""
Error handling in Python is done using try, except, and finally blocks. 
It allows you to manage exceptions (errors) gracefully, ensuring your program doesn't crash unexpectedly.

Here are some error handling examples to illustrate how it works:
"""

#1. Handling Division by Zero Error
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers.")

"""
Explanation:

ZeroDivisionError is caught when trying to divide by zero.
ValueError is caught if the user enters non-integer values.
"""

#2. Handling File Not Found Error
try:
    file_name = input("Enter the file name to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file you are trying to open does not exist.")

"""
Explanation:

FileNotFoundError is handled when the user tries to open a file that doesn't exist.
"""

#3. Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    print(f"The number is: {num}")
    result = 10 / num
    print(f"10 divided by {num} is {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

"""
Explanation:

This code handles both ValueError (if the user doesn't enter a valid number) and ZeroDivisionError (if the user enters 0).
The as e captures the exception message.
"""

#4. Handling File Operation with Finally Block
try:
    file_name = input("Enter the file name to open: ")
    file = open(file_name, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("No file to close.")


"""
Explanation:

The finally block ensures that even if an error occurs while opening the file, the file gets closed properly if it was opened successfully.
NameError handles the case where the file isn't opened at all.
"""

#5. Raising Custom Errors
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    else:
        print("Age is valid.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    print(f"Error: {ve}")


"""
Explanation:

This function raises a ValueError if the age is less than 18, and the exception is caught and displayed.
"""

#6. Try-Except with Else Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print(f"Result is {result}")


"""
Explanation:

The else block is executed if no exception occurs in the try block.
If no error occurs, the result of the division is printed.
"""

#7. Using assert for Simple Validation
def check_positive_number(num):
    assert num > 0, "Number must be positive!"
    print(f"The number is: {num}")

try:
    check_positive_number(-5)
except AssertionError as ae:
    print(f"AssertionError: {ae}")

#FileNotFoundError
try:
    filename = input("file name: ")
    file = open(filename, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File is not present")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("No file to close.")

"""
Explanation:

assert is used to check that the number is positive.
If the condition fails, an AssertionError is raised.
"""

"""
Key Takeaways:
1. Try-Except: Handle expected and unexpected errors.
2. Finally: Always executed, regardless of whether an error occurs.
3. Else: Runs when no exceptions occur.
4. Raise: Allows you to throw custom exceptions for better error handling
"""

"""
Practice:
Project: Bank Account Management System (Without OOP)
In this project:

The user can check the balance.
Deposit or withdraw money.
The program will handle exceptions like insufficient funds, invalid input, etc.
"""

# Initial bank account balance
balance = 10000  # Starting balance in INR

# Function to deposit money
def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than 0.")
    balance += amount
    print(f"Deposited {amount} INR. New balance: {balance} INR.")

# Function to withdraw money
def withdraw(amount):
    global balance
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than 0.")
    if amount > balance:
        raise ValueError("Insufficient funds! Unable to withdraw.")
    balance -= amount
    print(f"Withdrew {amount} INR. New balance: {balance} INR.")

# Function to check the balance
def check_balance():
    print(f"Current balance: {balance} INR.")

# Main function to run the system
def bank_account_system():
    global balance
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                withdraw(amount)
            elif choice == 4:
                print("Exiting the system. Thank you!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the bank account system
bank_account_system()

"""
Explanation of the Code:
Global Balance:
The balance variable holds the current balance of the account, starting with 10,000 INR.

Functions for Operations:

deposit(amount): Adds money to the account, but raises a ValueError if the amount is not positive.
withdraw(amount): Removes money from the account, and raises an error if the withdrawal exceeds the balance or if the amount is not positive.
check_balance(): Displays the current balance.
Main Program Flow:

The program presents a menu with 4 options: Check Balance, Deposit Money, Withdraw Money, and Exit.
Error Handling:
ValueError is raised for invalid input (e.g., negative numbers or non-numeric values).
Exception handles any unexpected errors, ensuring that the program doesn’t crash unexpectedly.
User Input:

The program asks for the user's choice and responds accordingly, performing the requested operation.
It uses try-except blocks to catch input errors (e.g., invalid options, incorrect amount types).
"""
