from fastapi import APIRouter, status
from datamodel.product import ProductDetails
from datamodel.response import GenericResponse
from service.productsvc import ProductService

# This is the API router similar to Springboot controller
product_router = APIRouter(prefix="/product-ms", tags= ["products"])

product_service = ProductService()

# Get product by Id
@product_router.get("/v1/product/{id}", description="Get by Product Id")
async def get_by_product_id(id: int) -> GenericResponse[ProductDetails]:
    product = product_service.get_by_id(id)
    return GenericResponse.success(product)

# Get all products
@product_router.get("/v1/products", description="Get all Products")
async def get_all_products() -> GenericResponse[list[ProductDetails]]:
    products = product_service.get_all()
    return GenericResponse.success(products)

# Create product
@product_router.post("/v1/product", description="Create Product", status_code = status.HTTP_201_CREATED)
async def create_product(product: ProductDetails) -> GenericResponse[ProductDetails]:
    product = product_service.create(product)
    return GenericResponse.success(product)

# Update product
@product_router.put("/v1/product", description="Update Product")
async def update_product(product: ProductDetails) -> GenericResponse[ProductDetails]:
    product = product_service.update(product)
    return GenericResponse.success(product)

# Delete product by Id
@product_router.delete("/v1/product/{id}", description="Delete by Product Id")
async def delete_by_product_id(id: int) -> GenericResponse[bool]:
    product_service.delete_by_id(id)
    return GenericResponse.success(True)

# Add quantity of the Product
@product_router.post("/v1/product/{id}/add/{quantity}", description="Add quantity")
async def add_quantity(id: int, quantity: int) -> GenericResponse[ProductDetails]:
    product = product_service.add_quantity(id, quantity)
    return GenericResponse.success(product)

# Substract quantity of the Product
@product_router.post("/v1/product/{id}/substract/{quantity}", description="Substract quantity")
async def substract_quantity(id: int, quantity: int) -> GenericResponse[ProductDetails]:
    product = product_service.substract_quantity(id, quantity)
    return GenericResponse.success(product)