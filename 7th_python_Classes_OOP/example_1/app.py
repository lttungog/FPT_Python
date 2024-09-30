import os
os.system("cls")

from person import Person
from vehicle import Vehicle

if __name__ == '__main__':
    
    person = Person("Tung", 29, "Hanoi")
    person.walk()
    
    print("\n")
    
    vehicle = Vehicle("Toyota Camry", 2023, "Toyota", 4)
    vehicle.start()
    vehicle.accelerate()
    vehicle.stop()