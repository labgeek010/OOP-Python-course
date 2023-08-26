class Character:
    def __init__(self, name, strength, speed):
        self.name = name
        self.strength = strength
        self.speed = speed
    
    def __repr__(self):
        return f"{self.name} (Strength: {self.strength}, Speed: {self.speed})"
    
    def __add__(self, other_cha):
        new_name = self.name + "-" + other_cha.name
        new_strength = round(((self.strength + other_cha.strength)/2)**1.5)
        new_speed = round(((self.speed + other_cha.speed)/2)**1.5)
        return Character(new_name, new_strength, new_speed)
    
Batman = Character("Bruce", 80, 80)
Superman = Character("Clark", 100, 100)
WonderWoman = Character("Diana", 96, 90)

SuperBat = Batman + Superman
WonderSuperBat = SuperBat + WonderWoman

print(SuperBat)
print(WonderSuperBat)