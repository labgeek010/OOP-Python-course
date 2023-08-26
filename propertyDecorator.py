class Person:
    def __init__(self,name, age):
        self.__name = name #the __ turns the name attribute into very private
        #so it prevents direct access and edits
        self._age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name

labgeek = Person("Daniel", 25)        

name = labgeek.name
print(name)