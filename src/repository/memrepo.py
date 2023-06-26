from typing import List

from pydantic import parse_obj_as

from src.domain.room import Room
from src.interfaces.repository import IRepository



class MemRepo(IRepository):
    def __init__(self, data: List[dict]):
        self.data = data
    

    def list(self) -> List[Room]:
        result = parse_obj_as(List[Room], self.data)
        return result