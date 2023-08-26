class Animal ():
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Miau"
    
class dog(Animal):
    def sound(self):
        return "Woof"
    
cat = Cat()    