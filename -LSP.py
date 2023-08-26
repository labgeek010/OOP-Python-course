# class Bird:
#     def fly (self):
#         return "I am flying"
    
# class Penguin(Bird):
#     def fly(self):
#         return "I can't fly"
    
# def make_fly(bird = Bird):
#     return bird.fly()

# print(make_fly(Penguin()))

class Bird:
    pass

class FlyingBird(Bird):
    def fly (self):
        return "I am flying."
    
class NonFlyingBird(Bird):
    pass
        