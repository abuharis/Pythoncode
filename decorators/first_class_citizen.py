# 1. Assigning function to a variable

def plus_one(number):
    print(number + 1) 

add_one = plus_one

add_one(2)

# 2. Defining function inside a function. Relevant to understand the decorator

def plus_one(num):
    def add_one(num):
        print(num + 1)
    
    result = add_one(num)
    print(result)

plus_one(4)


# 3. Passing function as arguments to other functions

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    print(function(number_to_add))

function_call(plus_one)

# 4. Functions returning other functions. ie Nested function

def hello_function():   #Enclosing Function
    def say_hello():    #Nested Function
        print("Hi")

    return say_hello

hello = hello_function()
hello()


# 5. Nested function have access to the Enclosing Functions's Variable Scope

def print_message(message): 
    "Enclosing Function"
    def message_function():
        "Nested Function"
        print(message)

    message_function()

print_message("Say this is Bramayugam")

