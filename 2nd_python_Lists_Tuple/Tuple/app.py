# Tuples

def tuple_example():
    print("Tuple exmaple:")
    tuple_examp = (1, 2, 3)
    print(f"{tuple_examp}")
    
    for i in tuple_examp:
        print(f"Element i {i}")
        
    tuple_examp_mix = ("Xin chao", "cac ban", 123)
    print(f"Mixed Tuple example: {tuple_examp_mix}")
    
def tuple_example_01():
    tuple_examp = (1, 2, 3, 1)
    print(f"The number of 1s in the tuple is: {tuple_examp.count(1)}")



if __name__ == "__main__":
    # tuple_example()
    tuple_example_01()