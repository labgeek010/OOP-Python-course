class A:
    def speak(self):
        print("Hello from A")

        
class F:
    def speak(self):
        print("Hello from F")  

class B(A):
    def speak(self):
        print("Hello from B")

class C(F):
    def speak(self):
        print("Hello from V")

class D(B,C):
    def speak(self):
        print("Hello from D")                

d = D()

F.speak(d)