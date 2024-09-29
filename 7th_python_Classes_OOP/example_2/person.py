class Person():
    
    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
        
    def walk(self):
        print(f"{self.name} aged {self.age} whose address is {self.address} is walking.")
    