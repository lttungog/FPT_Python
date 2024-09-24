# creating the functions:
def sum(a, b):
    total = a + b
    print(f"The sum of the 2 numbers is: {total}")
    
def sub(a, b):
    result = a - b
    print(f"The subtraction of the 2 numbers {a} and {b} gives us: {result}")
    
def multiplication(a, b):
    multi = a * b
    print(f"The multiplication of the 2 numbers {a} and {b} gives us: {multi}")

def div(a, b):
    result = a / b
    print(f"The division of the 2 numbers {a} and {b} gives us: {result}")
    
def sum_array(a):
    total = 0
    for i in range(a):
        total = total + i
    print(f"The sum of the array is: {total}")
    
def loop_example():
    for i in range(10, 5, -2):
        print(f"i = {i}")
        
def loop_example_01():
    x = 0
    while (x < 10):
        x = x + 1
        print(f"x = {x}")
    print("This is the end of the loop.")
    
def loop_example(x):
    match x:
        case 1:
            print("This is case number 01")
        case 2:
            print("This is the second case")
        case 3:
            print("This is case number 03")
        case _:
            print("Default case")
       

def select_choice():
    while True:
        try:
            print("\n")
            choice = int(input("Please enter your choice: "))
            if (choice == 1):
                a = int(input("Please enter a number: "))
                b = int(input("Please enter another number: "))
                sum(a, b)
            elif (choice == 2):
                a = int(input("Please enter a number: "))
                b = int(input("Please enter another number: "))
                sub(a, b)
            elif (choice == 3):
                a = int(input("Please enter a number: "))
                b = int(input("Please enter another number: "))
                multiplication(a, b)
            elif (choice == 4):
                a = int(input("Please enter a number: "))
                b = int(input("Please enter another number: "))
                div(a, b)
            elif (choice == 5):
                a = int(input("Please enter the number of values in the array: "))
                sum_array(a)
            elif (choice == 6):
                loop_example()
            elif (choice == 7):
                loop_example_01()
            elif (choice == 8):
                a = int(input("Please enter the number of the case: "))
                loop_example(a)
            elif (choice == 9):
                print("Exiting...")
                return False
            else:
                print("Invalid choice, please try again!")
                return True
        except:
            print("Please enter a number!")
        
# def menu():
#     while True:
#         print("===== Simple Menu =====")
#         print("1. Sum of 2 numbers")
#         print("2. Subtraction of 2 numbers")
#         print("3. Multiplication of 2 numbers")
#         print("4. Division of 2 numbers")
#         print("5. Sum of Array of 2 numbers")
#         print("6. Loop Example 1")
#         print("7. Loop Example 2")
#         print("8. Loop Example 3")
#         print("9. ")
#         print("10. Exit")
#         select_choice()
#         print("\n")

# calling the functions:   
if __name__ == '__main__':
    # sum(2, 5)
    # multiplication(2, 4)
    # menu()
    select_choice()