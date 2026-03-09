class DomainError(Exception):
    """Error base del dominio"""
    def __init__(self, message: str):
        self.message = message
    
    def __str__(self):
        return f"DomainError: {self.message}"

class InvalidIdError(DomainError):
    """
    Error que se lanza cuando el id es inválido
    """
    def __init__(self, message: str):
        super().__init__(message)
    
    def __str__(self):
        return f"InvalidIdError: {self.message}"


class EmptyTitleError(DomainError):
    """
    Error que se lanza cuando el título está vacío
    """
    def __init__(self, message: str):
        super().__init__(message)
    
    def __str__(self):
        return f"EmptyTitleError: {self.message}"


class InvalidAmountError(DomainError):
    """
    Error que se lanza cuando el importe es inválido
    """
    def __init__(self, message: str):
        super().__init__(message)
    
    def __str__(self):
        return f"InvalidAmountError: {self.message}"


class InvalidExpenseDateError(DomainError):
    """
    Error que se lanza cuando la fecha del gasto es inválida
    """
    def __init__(self, message: str):
        super().__init__(message)
    
    def __str__(self):
        return f"InvalidExpenseDateError: {self.message}"
