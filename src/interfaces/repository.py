from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.room import Room
from src.requests.room import RoomListParameters


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def list(self, paramters: RoomListParameters) -> List[Room]:
        pass