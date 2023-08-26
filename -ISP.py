from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
        
    @abstractmethod
    def eat(self):
        pass

class Sleeper(ABC):

    @abstractmethod
    def sleep(self):
        pass
        
class Human(Worker, Sleeper, Eater):

    def work(self):
        print("The human is sleeping")

    def eat(self):
        print("The human is eating")

    def sleep(self):
        print("The human is sleeping")

class Robot(Worker):

    def work(self):
        print("The robot is working")

robot1 = Robot()
robot1.work()
