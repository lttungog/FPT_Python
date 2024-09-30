from animals import Animal

class Cat (Animal):
    
    def __init__(self, name, speak) -> None:
        super().__init__(name)
        self.speak = speak
        
    def speak(self):
        return self.speak
    
    def set_speak(self, speak):
        self.speak = speak
        
    def display(self):
        super().display()
        print(f"The {self.name} sounds like so: {self.speak}")