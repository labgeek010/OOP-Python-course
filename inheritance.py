class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def speak(self):
        print(f"Hello, this is {self.name} speaking")

class Artist:
    def __init__(self,skill):
        self.skill = skill
    
    def show_skill(self):
        print(f"My skill is: {self.skill}")

class Employee(Person):
    def __init__(self, name, age, country, position, salary):
        super().__init__(name,age,country)
        self.position = position
        self.salary = salary


class EmployeeArtist(Person,Artist):
    def __init__ (self, name, age, country, skill, employer, salary):
        Person.__init__(self, name, age, country)
        Artist.__init__(self,skill)
        self.employer = employer
        self.salary = salary

    def show_skill(self):
        print("I don't have any lols")

    def selfPresent(self):
        return f'{super().show_skill()}'    



Robert = EmployeeArtist("Robert", 30,"Argentina","singing", "Developer", 100000)

Robert.selfPresent()

