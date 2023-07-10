from typing import List

from pydantic import parse_obj_as

from src.domain.room import Room
from src.interfaces.repository import IRepository
from src.requests.room import RoomListParameters



class MemRepo(IRepository):
    def __init__(self, data: List[dict]):
        self.data = data
    

    def list(self, paramters: RoomListParameters) -> List[Room]:
        result = parse_obj_as(List[Room], self.data)

        if paramters.code__eq is not None:
            result = [r for r in result if r.code == paramters.code__eq]
        if paramters.price__eq is not None:
            result = [r for r in result if r.price == paramters.price__eq]
        if paramters.price__lt is not None:
            result = [r for r in result if r.price < paramters.price__lt]
        if paramters.price__gt is not None:
            result = [r for r in result if r.price > paramters.price__gt]
        
        return result