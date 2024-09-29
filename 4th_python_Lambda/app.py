import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "fpt_sem3_python"
    )
    
def add_student():
    
    while True:
        name = input("Enter student Name: ")
        age = int(input("Enter student Age: "))
        stud_class = input("Enter student Class: ")
        connection = connect_to_db()
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO students (name, age, class) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, age, stud_class))
        
        connection.commit()
        print(f"\nStudent {name} added!")
        
        cursor.close()
        connection.close()
        
        choice = input("\nWould you like to add another Student? (yes/no)").lower()
        print("\n")
        
        if choice != 'yes':
            break
        
    print("Returning to main menu...")

def get_all_students():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    sql = "SELECT * FROM students"
    
    cursor.execute(sql)
    
    results = cursor.fetchall()
    
    for x in results:
        print(f"ID: {x[0]}, Name: {x[1]}, Age: {x[2]}, Class: {x[3]}, Grade: {x[4]}") 
        
    cursor.close()
    connection.close()

def find_student():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    while True:
        try:
            student_id = int(input("Please enter the ID of the student you wish to find: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
            
        
        sql = "SELECT * FROM students WHERE id = %s"
        
        cursor.execute(sql, (student_id,))
        
        myresult = cursor.fetchall()

        if myresult:
            
            for x in myresult:
                print(f"Student with ID {student_id} found!")
                print(f"\nName: {x[1]}, Age: {x[2]}, Class: {x[3]}, Grade: {x[4]}")
            break
        
        else:
            print(f"No Student with ID {student_id} found.")
            break
        
    cursor.close()
    connection.close()

def delete_student():
    
    connection = connect_to_db()
    cursor = connection.cursor()

    get_all_students()
    print("\n")
    
    student_id = int(input("Please enter the ID of the student you wish to delete: "))
    
    sql = "DELETE FROM students WHERE id = %s"
    
    cursor.execute(sql, (student_id,))
    
    connection.commit()
    
    print(f"\nStudent with ID {student_id} has been removed!\n")
    
    get_all_students()
    
    cursor.close()
    connection.close()

def edit_student():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    get_all_students()
    
    student_id = int(input("Please enter the ID of the student you wish to edit: "))
        
    class_edit = input("Please enter the new Class for the student: ")
    sql_class_edit = "UPDATE students SET class = %s WHERE id = %s"
    cursor.execute(sql_class_edit, (class_edit, student_id,))
    
    connection.commit()
    
    print(cursor.rowcount, "student(s) affected")
    
    cursor.close()
    connection.close()
    print("Returning to main menu...")
    
def add_grade():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    get_all_students()
    
    print("\n")
    student_id_grade = int(input("Please enter the ID of the Student which you want to append a Grade: "))
    grade = input("Please enter the Student's Grade: ")
    
    sql_grade_append = "UPDATE students SET grade = %s WHERE id = %s"
    cursor.execute(sql_grade_append, (grade, student_id_grade,))
    
    connection.commit()
    
    print(cursor.rowcount, "student(s) affected")
    
    cursor.close()
    connection.close()
    print("Returning to main menu...")

def filter_stud_by_class():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    sql_classes = "SELECT * FROM subjects"
    
    cursor.execute(sql_classes)
    
    classes = cursor.fetchall()
    
    for x in classes:
        print(f"Class Name: {x[1]}")
    
    try:
        subject_name = input("\nPlease enter one of the Classes above: ")
    except ValueError:
        print("Please enter a Subject")
    
    query = """
        SELECT s.name
        FROM students s
        JOIN student_subjects ss ON s.id = ss.student_id
        JOIN subjects sub ON ss.subject_id = sub.id
        WHERE sub.subject_name = %s
    """
    
    cursor.execute(query, (subject_name,))
    
    students_in_math = cursor.fetchall()
    
    print(f"\nThe Students attending the {subject_name} Classes are:")
    for student in students_in_math:
        print(student[0])
        
    cursor.close()
    connection.close()

def menu():
    
    exit = True
    
    while exit:
        
        print("\n")
        print("===== MENU =====")
        print("1. Add a Student")
        print("2. Retrieve all Student Data")
        print("3. Find a Student")
        print("4. Remove a Student")
        print("5. Update Student Class Information")
        print("6. Add Student Grade")
        print("7. Filter Students by Class")
        print("8. Exit")
        print("\n")
        
        try:
            choice = int(input("Please select one of the options above: "))
            print("\n")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7. ")
            continue

        
        match choice:
            case 1:
                add_student()
            case 2:
                get_all_students()
            case 3:
                find_student()
            case 4:
                delete_student()
            case 5:
                edit_student()
            case 6:
                add_grade()
            case 7:
                filter_stud_by_class()
            case 8:
                exit = False
            case _:
                print("Please enter one of the available choices.")
    
    
if __name__ == '__main__':
    # add_student()
    # edit_student()
    # get_all_students()
    # delete_student()
    menu()