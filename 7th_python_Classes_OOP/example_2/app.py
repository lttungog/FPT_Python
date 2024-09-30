# Clear previous code
import os
os.system("cls")

import mysql.connector

from cat import Cat
from dog import Dog
from person import Person

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "fpt_sem3_python"
    )
    
def get_animal_info():
    
    animal_type = input("Please enter animal type (person / cat / dog): ")
    name = input("Please enter name: ")
    speak = input("Please input what the animal says: ")
    return animal_type, name, speak

def store_in_list(animals, animal_type, name, speak):
    animals.append({'type': animal_type, 'name': name, 'speak': speak})
    
def add_info(animal_type, name, speak):
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO animals (animal_type, name, speak) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (animal_type, name, speak))

    connection.commit()
    print(cursor.rowcount, "record inserted.")
    
def display():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    select_query = "SELECT `animal_type`, `name`, `speak` FROM animals"
    cursor.execute(select_query)
    
def display_info(animals):
    for animal in animals:
        if animal['type'] == 'cat':
            animal_obj = Cat(animal['name'], animal['speak'])
        elif animal['type'] == 'dog':
            animal_obj = Dog(animal['name'], animal['speak'])
        elif animal['type'] == 'person':
            animal_obj = Person(animal['name'], animal['speak'])
        else:
            continue

        print(f"Type: {animal['type']}, Name: {animal['name']}, Sound: {animal_obj.speak()}")

if __name__ == '__main__':
    
    # cat = Cat("Cat", "Meow")
    # cat.display()
    
    # print("\n")
    # dog = Dog("Dog", "Woof woof")
    # dog.display()
    
    # print("\n")
    # person = Person("Lam", "Nigga Nigga Nigga")
    # person.display()
    
    animals = []

    while True:
        animal_type, name, speak = get_animal_info()
        store_in_list(animals, animal_type, name, speak)
        add_info(animal_type, name, speak)

        choice = input("Do you want to add more animals? (yes/no): ")
        if choice.lower() != 'yes':
            break

    display_info(animals)