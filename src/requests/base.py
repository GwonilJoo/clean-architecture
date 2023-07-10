from pydantic import BaseModel


class InvalidRequest:
    def __init__(self, error: Exception | str):
        self.error = error
    
    def __bool__(self):
        return False
    

class ValidRequest:
    def __init__(self, parameters: BaseModel):
        self.parameters = parameters

    def __bool__(self):
        return True