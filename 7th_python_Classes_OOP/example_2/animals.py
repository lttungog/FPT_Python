class Animal:

    def __init__(self, name) -> None:
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def speak(self):
        pass
        
    def display(self):
        print(f"This is a {self.name}")