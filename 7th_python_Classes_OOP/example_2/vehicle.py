class Vehicle():
    
    def __init__(self, model, year, brand, seats) -> None:
        self.model = model
        self.year = year
        self.brand = brand
        self.seats = seats
        
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year
    
    def get_brand(self):
        return self.brand
    def set_brand(self, brand):
        self.brand = brand
    
    def get_seats(self):
        return self.seats
    def set_seats(self, seats):
        self.seats = seats
    
    def start(self):
        print(f"Vehicle: {self.model} - {self.year} - {self.brand} - {self.seats} - is starting.")
            
    def accelerate(self):
        print(f"Vehicle: {self.model} - {self.year} - {self.brand} - {self.seats} - is accelerating")
        
    def stop(self):
        print(f"Vehicle: {self.model} - {self.year} - {self.brand} - {self.seats} - is stopping.")