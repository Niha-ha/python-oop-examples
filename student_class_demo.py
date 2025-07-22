# Define a class named 'Student'
class Student:
    # Constructor method to initialize the object with name and roll number
    def __init__(self, name, roll_no):
        self.name = name        # Assign the name parameter to the instance variable
        self.roll_no = roll_no  # Assign the roll_no parameter to the instance variable

    # Method to display the student's details
    def display(self):
        # Print the student's name and roll number
        print(f"Name: {self.name}, Roll: {self.roll_no}")

# Create an instance of the Student class with name "John" and roll number 2
student = Student("John", 2)

# Call the display method to show the student's details
student.display()
