from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def __init__(self,name,age,genre,activity):
        self.name = name
        self.age = age
        self.genre = genre
        self.activity = activity

    @abstractclassmethod
    def perform_activity(self):
        pass

    def greet(self):
        print(f"Hello!, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self,name,age,genre,activity):
        super().__init__(name,age,genre,activity)
    
    def perform_activity(self):
        print(f"I am styding: {self.activity}")

class Worker(Person):
    def __init__(self,name,age,genre,activity):
        super().__init__(name,age,genre,activity)
    
    def perform_activity(self):
        print(f"I am working as: {self.activity}")
 
labgeekStudent = Student("Daniel", 28,"Male","web developing")
labgeekWorker = Worker("Jose", 28,"Male","web developer")

labgeekStudent.greet()
labgeekStudent.perform_activity()

labgeekWorker.greet()
labgeekWorker.perform_activity()
