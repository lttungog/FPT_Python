# Lists

def list_example():
    print("List example")
    print("\n")
    list_examp = [1, 2, 3]
    print(f"The list: {list_examp}")
    print(f"First item in list: {list_examp[0]}")
    print(f"Last item in list: {list_examp[-1]}")
    print(f"Third item in list: {list_examp[2]}")
    
    list_str = ["Xin chao", "cac ban"]
    print(f"List of strings: {list_str}")
    
    list_mix = ["Xin chao", "cac ban", 123]
    print(f"List of strings and numbers mixed: {list_mix}")
    
    
def list_example_01():
    list_examp = [1, 2, 3]
    for i in list_examp:
        print(f"Element i: {i}")
        
def list_example_02_while():
    list_examp = [123, 212, 341, 464]
    list_length = len(list_examp)
    
    i = 0
    while i < len(list_examp): # could make len(list_examp) a separate variable too - list_length
        print(f"Element {i} is {list_examp[i]}")
        i += 1

def list_example_03():
    list_examp = [100, 22, 333]
    num = int(input("Please enter a number: "))
    num_insert = int(input("Please enter a number: "))
    
    list_examp.append(num)
    list_examp.insert(1, num_insert)
    list_examp.remove(100)
    
    for i in list_examp:
        print(f"Element i: {i}")

    
if __name__ == "__main__":
    # list_example()
    # list_example_01()
    # list_example_02_while()
    list_example_03()
    
    
    