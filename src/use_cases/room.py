from typing import List

from src.domain.room import Room


class RoomUseCase:
    def __init__(self):
        pass

    def list(self, repo: List[Room]):
        return repo