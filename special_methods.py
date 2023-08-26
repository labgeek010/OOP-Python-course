class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person(name={self.name}, age={self.age} )'
    
    def __repr__(self):
        return f'Person("{self.name}", {self.age})'
    
    def __add__(self, other):
        new_value = self.age + other.age
        return Person(self.name + other.name, new_value)
    

labgeek010 = Person("Dan", 28)
labgeek011 = Person("John", 25)
labgeek012 = Person("Marie", 22)

new_person = labgeek010igual  + labgeek012
print(new_person.name)