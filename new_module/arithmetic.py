balance = 1000
def check_balance():
    print(f"Current balance: {balance} INR.")

    

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks

student1 = Student("John", 85)
student1.update_marks(90)  # Updating marks
print(student1.marks)  # Output: 90

variable_name = "Abuharis"
#fucntion, class, variable
