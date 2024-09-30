import json
from os import path
from order import Customer, Order, Address

def readFileJson(path):
    if path is not None:
        with open(path, 'r') as content:
            order = json.load(content)
            print(order["orderID"])
            
def writeFileJson(order, path):
    if path is not None:
        with open(path, 'w') as file:
            json.dump(order.dict(), file, indent = 4)
            
def convertJsonToObject(path):
    if path is not None:
        with open(path, 'r') as content:
            json_data = json.load(content)
            
        order = Order(**json_data)
        print(order.orderID)
        print(order.customer.address)
            
            
if __name__ == "__main__":
    path = "./FPT_Python/8th_python/order.json"
    
    order = Order (
        orderID = "100",
        customer = Customer (
            customerID = "15",
            name = "Tung",
            email = "blabla@gmail.com",
            phone = "0986098532",
            address = Address (
                street = "Hanoi",
                city = "HN",
                state = "HN",
                postalCode = "100000",
                country = "Vietnam"
            )
        )
    )
    
    readFileJson(path)
    
    writeFileJson(order, path)
    
    readFileJson(path)
    
    

    