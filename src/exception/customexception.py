class ProductException(Exception):
    """Create custom exception for exception handling"""

    def __init__(self, message: str, http_status_code: int):
        self.message = message
        self.http_status_code = http_status_code
        super().__init__(self.message)