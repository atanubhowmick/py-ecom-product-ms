from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datamodel.response import GenericResponse
from exception.customexception import ProductException

# Global exception handler
async def product_exception_handler(request: Request, exception: ProductException):
    response =  GenericResponse.failure(exception.error_code, exception.error_message)
    return JSONResponse(
        status_code = exception.http_status_code,
        content = jsonable_encoder(response)
    )