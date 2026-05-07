from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    
    
    
    
    
    
    
products = [
    {"id": 1, "name": "Espresso", "price": 2.5},
    {"id": 2, "name": "Latte", "price": 3.5},
    {"id": 3, "name": "Cappuccino", "price": 3.0},
    {"id": 4, "name": "Mocha", "price": 4.0},

]