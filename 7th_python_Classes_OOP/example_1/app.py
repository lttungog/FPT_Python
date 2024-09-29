# Clear previous code
import os
os.system("cls")

from cat import Cat
from dog import Dog
from person import Person

if __name__ == '__main__':
    cat = Cat("Cat", "Meow")
    cat.display()
    
    print("\n")
    dog = Dog("Dog", "Woof woof")
    dog.display()
    
    print("\n")
    person = Person("Lam", "Nigga Nigga Nigga")
    person.display()