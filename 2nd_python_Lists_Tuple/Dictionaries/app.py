def dict_example():
    person_dict = {
        "name": "Luong Thanh Tung",
        "age": 29,
        "address": "Ha Noi"
    }, {
        "name": "Luong Thanh Hai",
        "age": 37,
        "address": "Ha Noi"
    }

    print(person_dict)
    print(f"Name: {person_dict[1]["name"]}")
    

if __name__ == "__main__":
    dict_example()