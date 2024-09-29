from tabulate import tabulate
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "fpt_sem3_python"
    )
    
def get_student_info():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # Retrieve all students from the database
    select_query = "SELECT `id`, `name`, `age`, `class` FROM students"
    cursor.execute(select_query)
    
    # Fetch all the rows and print them out in a table format
    students = cursor.fetchall()
    
    print("Students' Information:")
    headers = ["ID", "Name", "Age", "Class"]
    print(tabulate(students, headers=headers))
    
    cursor.close()
    connection.close()
    
def add_student():
    
    get_student_info()
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    try:
        name = input("Please enter the Student's Name: ")
        while True:
            try:
                age = int(input("Please enter the Student's Age: "))
            except ValueError:
                print("Please enter a valid number.")
            else:
                break
        class_name = input("Please enter the Student's Class Name: ")
        
        insert_student_query = "INSERT INTO students (name, age, class) VALUES (%s, %s, %s)"
        cursor.execute(insert_student_query, (name, age, class_name))
        
        connection.commit()
        print(f"\nStudent {name} has been added successfully!\n")
            
        cursor.close()
        connection.close()
    except:
        connection.rollback()
        print("Failed adding the new Student!")
        
        cursor.close()
        connection.close()
        
    get_student_info()

def edit_student():
    
    get_student_info()
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    while True:
        try:
            student_id_edit = int(input("Please enter the ID of the Student you wish to edit: "))
        except ValueError:
            print("Please enter a valid ID number!")
        else:
            break

    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id_edit,))
    student = cursor.fetchone()
    
    if student:
        print(f"Student with ID: {student_id_edit} found!")
        
        fields_to_edit = []
        new_values = {}
        
        if input("Would you like to edit the student's name? (y/n): ").lower() == 'y':
            new_name = input("Please enter the new Name: ")
            fields_to_edit.append("name")
            new_values["name"] = new_name
            
        if input("Would you like to edit the student's age? (y/n): ").lower() == 'y':
            new_age = input("Please enter the new Age: ")
            fields_to_edit.append("age")
            new_values["age"] = new_age
        
        if input("Would you like to edit the student's class? (y/n): ").lower() == 'y':
            new_class = input("Please enter the new Class: ")
            fields_to_edit.append("class")
            new_values["class"] = new_class
            
        if not fields_to_edit:
            print("No changes made.")
            return
        
        edit_student_query = "UPDATE students SET " + ", ".join(f"{field} = %s" for field in fields_to_edit) +  " WHERE id = %s"

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Add new Student")
        print("2. Update Student with ID")
        print("3. Delete Student with ID")
        print("4. Find Student with ID")
        
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            find_student()
        else: 
            print("Please enter choice again !!")

if __name__ == "__main__":
    # menu()
    # get_student_info()
    add_student()