class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def study(self):
        print("Styding...")

name = input("Type if your name:")
age = input("Provide your age:")
grade = input("By last, enter your grade:")

student = Student(name, age, grade)

print(f""" 
        STUDENT'S INFORMATION: \n\n
        Name: {student.name} \n
        Age: {student.age} \n
        Grade: {student.grade} \n

""")

while True:
    study = input()
    if (study.lower() == "study"):
        student.study()