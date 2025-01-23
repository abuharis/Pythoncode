"""
Loops in Python allow us to execute a block of code multiple times. The two primary types of loops in Python are:

for loop : Used when we know the number of iterations.
while loop : Used when the condition controls the loop execution.
"""

"""
or Loop with Real Use Cases
Use Case 1: Processing a List of Orders (E-Commerce Example)
"""

orders = ["Laptop", "Mobile", "Tablet"]

for order in orders:
    print(f"Processing order for: {order}")


"""
while Loop with Real Use Cases
Use Case 1: User Login Attempts (Authentication System)
"""
correct_password = "Python123"
user_input = ""
attempts = 0

while user_input != correct_password and attempts < 3:
    user_input = input("Enter password: ")
    attempts += 1

if user_input == correct_password:
    print("Access Granted")
else:
    print("Too many failed attempts, try again later.")


"""
Nested Loops with Real Use Case
Use Case: Generating a Sales Report (Retail Business Example)
"""
sales_data = {
    "January": [1000, 1500, 1200],
    "February": [1300, 1100, 1400]
}

for month, sales in sales_data.items():
    print(f"Sales report for {month}:")
    for sale in sales:
        print(f"  - Sale amount: {sale}")


"""
Using break and continue with Real Use Cases
Use Case 1: Finding the First Defective Product (Manufacturing Example)
"""
products = ["good", "good", "defective", "good"]

for product in products:
    if product == "defective":
        print("Defective product found! Stopping inspection.")
        break
    print(f"Product status: {product}")

items = ["In stock", "Out of stock", "In stock"]

#Skipping Out-of-Stock
for item in items:
    if item == "Out of stock":
        print("Skipping unavailable item.")
        continue
    print(f"Processing: {item}")
