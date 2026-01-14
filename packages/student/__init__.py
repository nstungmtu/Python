__version__ = "1.0.0" # version of the student package
print("Package 'student' has been imported.")
__all__ = ["student_functions", "Student"]  # specify the modules to be imported with 'from student import *'

class Student:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def display_info(self):
        print(f"Student Name: {self.name}, Birthday: {self.birthday}")
    
    from ._calculate_age import calculate_age