from datamodel.product import ProductDetails
from exception.customexception import ProductException
from log.logger import logger

class ProductService:

    def __init__(self):
        """This class use a dictionary where the Key is the id and the Value is the ProductDetails object"""
        self.product_storage: dict[int, ProductDetails] = {}
        self.pre_existing_records()

    def pre_existing_records(self):
        logger.debug("Initializing pre existing records")
        self.product_storage[1001] = ProductDetails(
            id=1001, 
            name='Moto g60', 
            details='Moto g60 8GB 128GB Snapdragon 8A', 
            available_qty=10
        )
        self.product_storage[1002] = ProductDetails(
            id=1002, 
            name='One Plus Nord 4', 
            details='One Plus Nord 4 12GB 256GB Snapdragon 7C', 
            available_qty=8
        )
        self.product_storage[1003] = ProductDetails(
            id=1003, 
            name='iPhone 15', 
            details='iPhone 15 8GB 128GB Apple A16', 
            available_qty=4
        )

    # --- GET ---
    def get_by_id(self, id: int) -> ProductDetails:
        """Return a product found by Id"""
        if id not in self.product_storage:
            raise ProductException("E001", f"No Product found for the id '{id}'", 400)
        return self.product_storage.get(id)
    
    # --- GET ALL ---
    def get_all(self) -> list[ProductDetails]:
        """Returns a list of all products."""
        return list(self.product_storage.values())

    # --- CREATE ---
    def create(self, product: ProductDetails) -> ProductDetails:
        """Creates product and persist into the memory"""
        if product.id in self.product_storage:
            raise ProductException("E002", f"Product with id '{product.id}' already exists.", 400)
        
        self.product_storage[product.id] = product
        logger.info("Product created: %s", product.model_dump_json())
        return product
    
    # --- UPDATE ---
    def update(self, updated_info: ProductDetails) -> ProductDetails:
        """Update product and persist into the memory"""
        id = updated_info.id
        if id not in self.product_storage:
            raise ProductException("E001", f"No Product found for the id '{id}'", 400)

        self.product_storage[id] = updated_info
        logger.info("Product updated: %s", updated_info.model_dump_json())
        return updated_info

    # --- DELETE ---
    def delete_by_id(self, id: int) -> bool:
        """Delete product by Id"""
        if id in self.product_storage:
            del self.product_storage[id]
            logger.info("Product deleted with id '%s'", id)
            return True
        return False
    
    def add_quantity(self, id: int, quantity: int) -> ProductDetails:
        """Add more quantity and return updated product details"""
        product = self.get_by_id(id)
        product.available_qty += quantity
        # Lazy formatting inside logger
        logger.info("Adding %d quantity to product id '%d'. Current quantity: %s", quantity, id, product.available_qty)
        return self.update(product)
    
    def substract_quantity(self, id: int, quantity: int) -> ProductDetails:
        """Substract quantity and return updated product details"""
        product = self.get_by_id(id)
        if quantity > product.available_qty:
            raise ProductException("E003", f"Can't dispence {quantity} quantity from product id '{id}'. Available quantity: {product.available_qty}", 400)
        product.available_qty -= quantity
        # Eager formatting using string formatter
        logger.info(f"Reducing {quantity} qyantity from product id '{id}'. Current quantity: {product.available_qty}")
        return self.update(product)
    