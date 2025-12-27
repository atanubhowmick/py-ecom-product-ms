from fastapi import FastAPI
from server.router import product_router
from exception.customexception import ProductException
from exception.handler import product_exception_handler

app = FastAPI()
app.include_router(product_router, prefix="/api")
app.add_exception_handler(ProductException, product_exception_handler)
