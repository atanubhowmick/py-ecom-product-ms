from fastapi import APIRouter
from typing import Optional
from datamodel.product import ProductDetails
from service.productsvc import ProductService

product_router = APIRouter(prefix="/product", tags= ["products"])

product_service = ProductService()

@product_router.get("/v1/product/{id}", description="Get by Product Id")
async def get_by_product_id(id: int) -> Optional[ProductDetails]:
    return product_service.get_by_id(id)

@product_router.get("/v1/products", description="Get all Products")
async def get_all_products() -> list[ProductDetails]:
    return product_service.get_all()

@product_router.post("/v1/product", description="Create Product")
async def create_product(product: ProductDetails) -> ProductDetails:
    return product_service.create(product)

@product_router.put("/v1/product", description="Update Product")
async def update_product(product: ProductDetails) -> Optional[ProductDetails]:
    return product_service.update(product)

@product_router.delete("/v1/product/{id}", description="Delete by Product Id")
async def delete_by_product_id(id: int) -> bool:
    return product_service.delete_by_id(id)