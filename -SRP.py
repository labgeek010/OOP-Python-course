class Auto():
    def __init__(self, tank):
        self.position = 0
        self.tank = tank

    def move(self, distance):
        if self.tank.obtain_fuel() >= distance /2:
            self.position += distance
            self.tank.use_fuel(distance /2) 
            print("You successfully moved the car.")
        else:
            print("There's no fuel.")
    
    def obtain_position(self):
        return self.position

class FuelTank ():
    def __init__(self):
        self.fuel = 100

    def add_fuel(self,quantity):
        self.fuel += quantity
    
    def obtain_fuel(self):
        return self.fuel
    
    def use_fuel(self, quantity):
        self.fuel -= quantity

tank1 = FuelTank()
car1 = Auto(tank)

print(car1.obtain_position())
print(car1.move(10))

print(car1.obtain_position())
print(car1.move(20))

print(car1.obtain_position())
print(car1.move(60))

print(car1.obtain_position())
print(car1.move(100))
