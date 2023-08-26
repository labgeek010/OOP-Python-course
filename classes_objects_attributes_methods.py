class PsVita ():
    title = "Ps Vita"
    brand = "Sony"
    model = "1001"
    color = "black"


consolePsVita = PsVita()
print(consolePsVita.brand)

#***********************************#

class PsVita:
    def __init__(self, title, brand, model, color):
        self.title = title
        self.brand = brand
        self.model = model
        self.color = color
    
    def play(self):
        print(f'You are playing with a: {self.model} ')

    def turnOff(self):
        print(f"Your {self.model} if shutting off")

vitaConsole1 = PsVita("PsVita Fat Black In Box", "Sony","Fat Ps Vita", "Black" )
vitaConsole2 = PsVita("PsVita Slim Snow White In Box", "Sony", "Slim Ps Vita", "Snow White")


print(vitaConsole2.color)
vitaConsole1.play()
vitaConsole2.play()
vitaConsole2.turnOff()
