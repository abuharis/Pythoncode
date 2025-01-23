#Difference Between Module, Library, and Package in Python
"""
1. Module
A module is a single Python file (with a .py extension) containing functions, variables, and classes. It helps organize code logically and makes it reusable.

Key Points:
A module is a single file.
Used to store reusable code (functions, classes).
Imported using import module_name.
"""

"""
2. Package
A package is a collection of related modules organized into a directory containing a special __init__.py file. 
The presence of __init__.py makes Python treat the directory as a package, allowing for easier module management and importing.
"""

#Step 1: Create a package directory structure:
# mypackage/
# │-- __init__.py  (Required to make it a package)
# │-- math_utils.py
# │-- string_utils.py

#math_utils.py
def add(a, b):
    return a + b

#string_utils.py
def capitalize_text(text):
    return text.capitalize()

#Step 2: Import from the package and use it
from mypackage import math_utils, string_utils

print(math_utils.add(2, 3))  # Output: 5
print(string_utils.capitalize_text("hello"))  # Output: Hello

"""
Key Points:
A package is a directory containing multiple related modules.
The __init__.py file marks the directory as a package.
Allows logical grouping of modules.
"""

"""
3. Library
A library is a collection of pre-written modules and packages that provide specific functionalities. Libraries offer a set of tools and functions that developers can use without writing code from scratch.

Examples of Popular Python Libraries:
NumPy : Numerical computing.
Pandas : Data analysis and manipulation.
Requests : Handling HTTP requests.
Matplotlib : Data visualization.

Key Points:
A library is a collection of multiple packages and modules.
Libraries simplify complex programming tasks.
Installed via pip (e.g., pip install requests).
"""

"""
What is __init__.py and Why is it Important?

The __init__.py file is required to make Python treat a directory as a package.
It can be an empty file or contain initialization code that runs when the package is imported.
It allows package-wide variable definitions and automatic imports.
"""
