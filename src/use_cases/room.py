from typing import List

from src.domain.room import Room
from src.interfaces.repository import IRepository


class RoomUseCase:
    def __init__(self):
        pass

    def list(self, repo: IRepository):
        return repo.list()