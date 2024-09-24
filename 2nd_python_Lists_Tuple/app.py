# Class Work

from prettytable import PrettyTable

# 1.

def cars_dict():

    Cars = {
        'car1': {
            'brand': 'BMW',
            'model' : '320d',
            'year' : 2011,
            'color': 'black'
        },
        'car2': {
            'brand': 'BMW',
            'model' : '228i',
            'year' : 2012,
            'color': 'white'
        },
        'car3': {
            'brand': 'BMW',
            'model' : '320d',
            'year' : 2012,
            'color': 'blue'
        },
        'car4': {
            'brand': 'BMW',
            'model' : '320d',
            'year' : 2021,
            'color': 'black'
        },
        'car5': {
            'brand': 'BMW',
            'model' : '280i',
            'year' : 2015,
            'color': 'white'
        },
        'car6': {
            'brand': 'BMW',
            'model' : 'X3',
            'year' : 2021,
            'color': 'red'
        },
        'car7': {
            'brand': 'BMW',
            'model' : 'iX3',
            'year' : 2024,
            'color': 'orange'
        },
        'car8': {
            'brand': 'BMW',
            'model' : 'M850i',
            'year' : 2024,
            'color': 'blue'
        },
        'car9': {
            'brand': 'BMW',
            'model' : 'M440i',
            'year' : 2023,
            'color': 'black'
        },
        'car10': {
            'brand': 'BMW',
            'model' : 'Z4',
            'year' : 2023,
            'color': 'purple'
        }
    }
    
    print(Cars)
    print("\n")
    
    brand = input("Please enter a Brand name: ")
    model = input("Please enter the Model name: ")
    year = int(input("Please input the production Year: "))
    color = input("Please enter the color: ")
    
    Cars['car11'] = {}
    
    Cars['car11']['brand'] = brand
    Cars['car11']['model'] = model
    Cars['car11']['year'] = year
    Cars['car11']['color'] = color
    
    print(Cars)
    print("\n")
    
    
    sorted_cars = dict(sorted(Cars.items(), key = lambda item : item[1]['year']))


    sorted_cars = cars_dict()

    for car, details in sorted_cars.items():
        print(f"{car}: {details}")
        print("\n")
    
def students_dict():
    
    Students = {
        'student_1': {
            'id' : 1,
            'name' : 'Luong Thanh Tung',
            'st_class' : 'T2308M',
            'first_grade' : 8,
            'second_grade' : 7
        },
        'student_2' : {
            'id' : 2,
            'name' : 'Luong Thanh Hai',
            'st_class' : 'T2308M',
            'first_grade' : 10,
            'second_grade' : 9
        },
        'student_3' : {
            'id' : 3,
            'name' : 'Nguyen Phuc Lam',
            'st_class' : 'T2308M',
            'first_grade' : 9,
            'second_grade' : 5
        },
        'student_4' : {
            'id' : 4,
            'name' : 'Do Minh Duc',
            'st_class' : 'T2308M',
            'first_grade' : 5,
            'second_grade' : 5
        },
        'student_5' : {
            'id' : 5,
            'name' : 'Nguyen Thi Thanh Mai',
            'st_class' : 'T2308M',
            'first_grade' : 10,
            'second_grade' : 10
        },
        'student_6' : {
            'id' : 6,
            'name' : 'Nguyen Hai Nam',
            'st_class' : 'T2308M',
            'first_grade' : 3,
            'second_grade' : 5
        },
        'student_7' : {
            'id' : 7,
            'name' : 'Do Nguyen Lam',
            'st_class' : 'T2308M',
            'first_grade' : 2,
            'second_grade' : 3
        }
    }
    
    # print("{:<5} {:<25} {:<10} {:<10} {:<10}".format('TT', 'Ho Ten', 'Lop', 'Diem 1', 'Diem 2'))
    
    # for key, value in Students.items():
    #     id = value['id']
    #     name = value['name']
    #     st_class = value['st_class']
    #     first_grade = value['first_grade']
    #     second_grade = value['second_grade']
    #     print("{:<5} {:<25} {:<10} {:<10} {:<10}".format(id, name, st_class, first_grade, second_grade))
        
    def calculate_grade(first_grade, second_grade):
        
        total = 0.3 * first_grade + 0.7 * second_grade
        return total
    
    def assign_letter_grade(total_grade):
        
        if total_grade < 4.0:
            return 'F'
        elif 4.0 <= total_grade < 5.5:
            return 'D'
        elif 5.5 <= total_grade < 6.5:
            return 'C'
        elif 6.5 <= total_grade < 8.5:
            return 'B'
        else:
            return 'A'
        
    for key, value in Students.items():
        total_grade = calculate_grade(value['first_grade'], value['second_grade'])
        letter_grade = assign_letter_grade(total_grade)
        value['grade_letter'] = letter_grade
        
    print("{:<5} {:<25} {:<10} {:<10} {:<10} {:<10}".format('TT', 'Ho Ten', 'Lop', 'Diem 1', 'Diem 2', 'Diem TK'))
    
    for key, value in Students.items():
        id = value['id']
        name = value['name']
        st_class = value['st_class']
        first_grade = value['first_grade']
        second_grade = value['second_grade']
        grade_total = value['grade_letter']
        print("{:<5} {:<25} {:<10} {:<10} {:<10} {:<10}".format(id, name, st_class, first_grade, second_grade, grade_total))

if __name__ == "__main__":
    # students_dict()
    cars_dict()