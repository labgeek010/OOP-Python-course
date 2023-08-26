class Animal:
    def eat(self):
        print("The Animal is eating")

class Bird(Animal):
    def fly(self):
        print("The Bird is flying")

class Mammal(Animal):
    def breastFeed(self):
        print("The Mammal is breast-feeding")

class Bat(Mammal, Bird):
    pass

bat = Bat()

bat.eat()
bat.breastFeed()
bat.fly()