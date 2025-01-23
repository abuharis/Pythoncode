"""
In Python, a module is a file containing Python code (functions, variables, and classes) that can be imported and reused in other scripts. 
This promotes code reusability and organization.
"""

"""
1. Types of Modules in Python
Python provides two types of modules:

Built-in Modules : Pre-installed modules that come with Python (e.g., math, os, random).
User-Defined Modules : Custom modules created by users for specific applications.
"""

"""
2. Using Modules in Python
Importing Modules
You can import modules in several ways:"""

import math  # Import the whole module
from math import sqrt  # Import specific function
import math as m  # Import with alias


#3. Creating a User-Defined Module

#Step 1: Create a module (my_module.py)
# my_module.py
def greet(name):
    return f"Hello, {name}!"

pi_value = 3.14159

#Step 2: Use the module in another script
import my_module

print(my_module.greet("Alice"))
print("Pi value is:", my_module.pi_value)

#4. Common Built-in Modules and Use Cases

#1. math – Mathematical Operations
#Use Case: Scientific calculations, complex number operations.
import math

print(math.sqrt(25))  # Square root
print(math.factorial(5))  # Factorial
print(math.pi)  # Pi constant

#2. random – Random Number Generation
#Use Case: Games, simulations, cryptography.
import random

print(random.randint(1, 100))  # Random number between 1 and 100
print(random.choice(["apple", "banana", "cherry"]))  # Random choice from list

#3. datetime – Working with Dates and Time
#Use Case: Time-stamping events, scheduling, logs.
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

#4. os – Operating System Operations
#Use Case: File handling, process management, directory navigation.
import os

print(os.getcwd())  # Get current working directory
os.mkdir("new_folder")  # Create new directory

#5. sys – System-Specific Functions
#Use Case: Command-line argument handling, interpreter control.
import sys

print("Python version:", sys.version)
print("Script arguments:", sys.argv)

#6. json – Working with JSON Data
#Use Case: Web data exchange, API responses.
import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)  # Convert dictionary to JSON string
print(json_str)

parsed_data = json.loads(json_str)  # Convert JSON string back to dictionary
print(parsed_data["name"])

#7. re – Regular Expressions
#Use Case: Pattern matching, text validation (e.g., email validation).
import re

pattern = r"\b[A-Za-z]+@\w+\.\w{2,3}\b"
email = "test@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


#8. requests – Handling HTTP Requests (Third-Party Module)
#Use Case: API interactions, web scraping.
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())  # Get JSON response

#9. csv – Handling CSV Files
#Use Case: Reading and writing structured data.
import csv

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#10. time – Handling Time Delays and Performance Measurement
#Use Case: Execution delay, benchmarking.
import time

print("Start")
time.sleep(2)  # Pause execution for 2 seconds
print("End")

#5. Finding Installed Modules
help("modules")

"""
6. Practical Use Cases for Modules

Web Scraping: Using requests and beautifulsoup to extract website data.
Data Analysis: Using pandas and numpy for large-scale data processing.
Automation: Using os and shutil to automate file operations.
Machine Learning: Using scikit-learn for predictive modeling.
Network Programming: Using socket for building network applications.
Security: Using hashlib for data encryption.
"""

try:
    import non_existent_module
except ImportError:
    print("Module not found. Please install it using 'pip install'.")



