class Car:
    
    def __init__(self, model, year, brand, seats):
        
        self.model = model
        self.year = year
        self.brand = brand
        self.seats = seats
        self.is_running = True
        
    def start(self):
        
        if self.is_running:
            print(f"The {self.model} is already running.")
        else:
            self.is_running = True
            print(f"The {self.model} has been started. ")
            
    def accelerate(self):
        
        if self.is_running:
            print(f"The {self.model} is accelerating.")
        else:
            print(f"Please start the {self.model} first, before trying to accelerate.")
    
    def stop(self):
        
        if self.is_running:
            print(f"The {self.model} has been stopped.")
        else:
            print(f"The {self.model} hasn't been started yet.")
            

car1 = Car("Honda Camry", 2023, "Honda", 4)
car1.start()
car1.accelerate()
car1.stop()