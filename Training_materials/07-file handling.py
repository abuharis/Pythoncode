"""
File management in Python allows you to read, write, update, and delete files efficiently. 
Python provides built-in functions to handle files with different modes of access.
"""

"""
1. Opening and Closing Files
Before working with a file, you must open it using the open() function and close it when done using close().
"""

#Syntax
file = open("filename.txt", "mode")
file.close()

"""
File Opening Modes

'r'	Read (default mode, file must exist)
'w'	Write (overwrites file, creates if not exist)
'a'	Append (adds to existing file, creates if not exist)
'x'	Exclusive creation (fails if file exists)
'b'	Binary mode (used with images, etc.)
't'	Text mode (default, for text files)
"""

#1. Writing to a File
#You can write data to a file using the write() method.
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Welcome to Python file handling.")

#2. Reading from a File
#You can read data from a file using various methods such as read(), readline(), and readlines().
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


#2.1 Reading Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

#2.2 Using readlines() to get a list of lines
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

#3. Appending to a File
#To add content without overwriting the existing file data, use the append mode 'a'.
with open("example.txt", "a") as file:
    file.write("\nThis is an additional line.")


#4. Using with Statement
#The with statement is recommended for file operations as it automatically closes the file after the block execution.
with open("example.txt", "r") as file:
    print(file.read())

#5. Checking if a File Exists Before Opening
#Using os.path to check file existence before performing operations.
import os

if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File does not exist.")

#6. File Deletion
#You can delete files using the os.remove() function.
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")

#7. Renaming Files
#The os.rename() function can rename a file.
import os

os.rename("example.txt", "renamed_file.txt")


#8. Working with File Paths
#Using os.path to work with file paths.
import os

file_path = "example.txt"
print("Absolute path:", os.path.abspath(file_path))
print("File exists:", os.path.exists(file_path))
print("File size:", os.path.getsize(file_path), "bytes")


#9. Exception Handling in File Operations
#Handling errors like missing files.
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")

#10. Writing and Reading CSV Files
#Using Python to handle CSV files.
import csv

with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Los Angeles"])


#11. Reading from json files
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

#12. Copying Files
#Using shutil to copy files.
import shutil

shutil.copy("data.json", "backup_data.json")


#13. Counting Lines, Words, and Characters in a File
with open("example.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")
    words = content.split()
    characters = len(content)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)


#14. Searching for a Word in a File
with open("example.txt", "r") as file:
    content = file.read()
    if "Python" in content:
        print("Word found!")
    else:
        print("Word not found.")