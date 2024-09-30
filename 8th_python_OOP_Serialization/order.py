from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    postalCode : str
    country: str
    
class Customer(BaseModel):
    name: str
    email: str
    phone: str
    address: Address
    
class Order(BaseModel):
    orderID: str
    customer: Customer