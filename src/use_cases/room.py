from typing import List

from src.domain.room import Room
from src.interfaces.repository import IRepository
from src.requests.room import RoomListParameters
from src.requests.base import ValidRequest, InvalidRequest
from src.responses import ResponseTypes, ResponseFailure, ResponseSuccess


class RoomUseCase:
    def __init__(self):
        pass

    def list(
            self, 
            repo: IRepository,
            request: ValidRequest | InvalidRequest,
        ) -> ResponseSuccess | ResponseFailure:
        if not request:
            return ResponseFailure(
                type=ResponseTypes.PARAMETERS_ERROR,
                message=request.error
            )
        try:
            rooms: List[Room] = repo.list(request.parameters)
            return ResponseSuccess(value=rooms)
        except Exception as exc:
            return ResponseFailure(
                type=ResponseTypes.SYSTEM_ERROR,
                message=exc,
            )

        #return repo.list(request=request.parameters)