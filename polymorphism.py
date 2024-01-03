# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#polymorphism: existing in many forms
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def move(self):
        print("driving")
class Plane:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def move(self):
        print("flying")
class Boat:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def move(self):
        print('sailing')
        
        
Car1 = Car("toyota", "red")
Car1.move()
Plane1 = Plane("boeing", "white")
Plane1.move()
Boat1 = Boat("yacht", "white")
Boat1.move()