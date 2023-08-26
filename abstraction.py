class Auto():
    def __init__(self):
        self._state = "off"
    
    def turnOn(self):
        self._state = "running"
        print("The car is running")
    
    def drive(self):
        if self._state == "off":
            self.turnOn()
        print("Driving the car.")

my_car = Auto()
my_car.drive()