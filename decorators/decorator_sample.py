# Lets create a decorator. We do this by defiing a wrapper inside an enclosed function.
"Very Similar to function inside a function"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        print(make_uppercase)
    
    return wrapper

'''Since our decorator functiuon takes a function as an argument, we shall define a funciton to pass.
Now I am assigning the function to a variable
'''

def say_hi():
    return "hello abuharis"

decorate = uppercase_decorator(say_hi)
decorate()

'''This is quite complex and requires additional lines of code.
But Python has a very simple syntax to decorate it by using an @ symmbol.
'''

@uppercase_decorator
def say_hello():
    return "hi abuharis this is too much"

say_hello()