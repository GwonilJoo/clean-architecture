from abc import ABCMeta, abstractmethod
from typing import List

from src.domain.room import Room


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[Room]:
        pass