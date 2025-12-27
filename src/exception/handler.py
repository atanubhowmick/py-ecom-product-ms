from fastapi import Request
from fastapi.responses import JSONResponse
from exception.customexception import ProductException

# Global exception handler
async def product_exception_handler(request: Request, exc: ProductException):
    return JSONResponse(
        status_code = exc.http_status_code,
        content={"message": str(exc)},
    )