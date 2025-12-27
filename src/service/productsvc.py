from typing import Optional
from datamodel.product import ProductDetails
from exception.customexception import ProductException

class ProductService:

    def __init__(self):
        """This class use a dictionary where the Key is the id and the Value is the ProductDetails object"""
        self.product_storage: dict[int, ProductDetails] = {}

    def get_by_id(self, id: int) -> Optional[ProductDetails]:
        """Return a product found by Id"""
        return self.product_storage.get(id)
    
    def get_all(self) -> list[ProductDetails]:
        """Returns a list of all products."""
        return list(self.product_storage.values())

    # --- CREATE ---
    def create(self, product: ProductDetails) -> ProductDetails:
        if product.id in self.product_storage:
            raise ProductException(f"Product with Id {product.id} already exists.", 400)
        
        self.product_storage[product.id] = product
        return product
    
    # --- UPDATE ---
    def update(self, updated_info: ProductDetails) -> Optional[ProductDetails]:
        if updated_info.id in self.product_storage:
            self.product_storage[updated_info.id] = updated_info
            return updated_info
        return None

    # --- DELETE ---
    def delete_by_id(self, id: int) -> bool:
        if id in self.product_storage:
            del self.product_storage[id]
            return True
        return False
    