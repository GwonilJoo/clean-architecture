from pydantic import BaseModel

from src.responses.types import ResponseTypes


class Message(BaseModel):
    type: str
    message: str


class ResponseFailure:
    def __init__(self, type: ResponseTypes, message: Exception | str):
        self.type = type
        self.message = self.__format_message(message)

    def __format_message(self, msg):
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__}: {msg}"
        return msg
    
    @property
    def value(self):
        return Message(
            type=self.type,
            message=self.message
        )
    
    def __bool__(self):
        return False