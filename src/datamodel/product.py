from pydantic import BaseModel

class ProductDetails(BaseModel):

    # Pydantic requires fields to be defined as class attributes with type hints
    id: int
    name: str
    details: str
    available_qty: int

    # do not need init method. pydantic will create itself
    #def __init__(self, id: int, name, details, available_qty):
    #    self.id = id
    #    self.name = name
    #    self.details = details
    #    self.available_qty = available_qty
    
    def print(self):
        print(f"Product: id={self.id}, name={self.name}, details={self.details}, available_qty={self.available_qty}")
