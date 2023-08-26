class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def show_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_grade(self):
        print(f"Grade: {self.grade}")    


student = Student("Jhon","24","10th grade")
student.show_data()
student.show_grade()


##  https://www.youtube.com/watch?v=HtKqSJX7VoM&list=WL&index=1&t=2449s  at 1hr 25min  ##