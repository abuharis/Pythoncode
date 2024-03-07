import functools

"""
Sometimes we might need to define a decorator that accepts arguments. 
We achieve this by passing the arguments to the wrapper function. 
The arguments will then be passed to the function that is being decorated at call time.
"""

def decorator_with_args(function):
    def wrapper_with_args(args1, args2):
        print(f"The arguments are {args1} & {args2}")
        function(args1, args2)

    return wrapper_with_args


@decorator_with_args
def func_with_args(a, b):
    print("The is the part of the decorated function")


func_with_args("Abu", "haris")


"""
What if the decorator itself requires to accept arguments.
In order to achieve this, we define a decorator maker that accepts arguments then define a decorator inside it.
"""

def decorator_maker_with_arguments(dec_arg1, dec_arg2, dec_arg3):
    def decorator(function):
        #@functools.wraps(function)                 
        "functool preserves the meta data of the decorated function, not the wrapper."
        def wrapper(func_args1, func_arg2, func_arg3):
            "This is the wrapper function"
            print(f"The wrapper can access all the variable\n"
                  f"\t- from the decorator maker: {dec_arg1}, {dec_arg2} & {dec_arg3}\n"
                  f"\t- from the function call: {func_args1} & {func_arg2}")
            
        return wrapper
    
    return decorator
    
@decorator_maker_with_arguments("Pandas", "Numpy", "Sci-Kit-learn")
def decorated_func_with_args(func_args1, func_arg2, func_arg3):
    print("This is the decorated function")


decorated_func_with_args("MIlk", "Apple", "Orange")

print(decorated_func_with_args.__name__)
print(decorator_maker_with_arguments.__doc__)


def connect():
    a = "hai"
    return a

def test(a):
    print(a)


def final():
    con = connect

    if con is not None:
        test(con)

final()