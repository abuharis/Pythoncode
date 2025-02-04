"""
the return keyword is used within a function to exit the function and send a value back to the caller. 
This allows the function to produce a result that can be utilized elsewhere in the code.

Syntax:
def function_name(parameters):
    # function body
    return value

#Returning multiple values
This function returns multiple values as a tuple, which can be unpacked into separate variables.
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

name, age = get_name_and_age()
print(name)  # Output: Alice
print(age)   # Output: 30

#Difference Between return and print:
return: Used inside a function to send a value back to the caller. 
It allows the function's result to be stored in a variable or used in further expressions. 
Once a return statement is executed, the function terminates, and subsequent code within the function is not executed.

print: Used to display information to the console. It outputs the specified message but does not 
affect the flow of the program or return a value that can be used later.

def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

result_print = add_with_print(2, 3)  # Outputs: 5
result_return = add_with_return(2, 3)

print(result_print)   # Outputs: None
print(result_return)  # Outputs: 5

"""