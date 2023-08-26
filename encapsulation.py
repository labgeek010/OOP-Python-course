class myClass:
    def __init__(self):
        self._private_attribute = "value"

    def _speak(self):
        print("Hey, how are you?")    

object = myClass()
print(object._speak())

################################################

class Person:
    def __init__(self,name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

labgeek = Person("Daniel", 25)        

name = labgeek.get_name()
print(name)

labgeek.set_name("DanyBoy")

name = labgeek.get_name()
print(name)