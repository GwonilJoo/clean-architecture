import uuid
from typing import List

from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.domain.room import Room
from src.use_cases.room import RoomUseCase
from src.repository.memrepo import MemRepo
from src.requests.room import RoomListParameters, build_room_list_request
from src.requests.base import ValidRequest, InvalidRequest
from src.responses import ResponseTypes, ResponseSuccess, ResponseFailure, Message


router = APIRouter()

STATUS_CODE = {
    ResponseTypes.SUCCESS : status.HTTP_200_OK,
    ResponseTypes.PARAMETERS_ERROR: status.HTTP_400_BAD_REQUEST,
    ResponseTypes.RESOURCE_ERROR: status.HTTP_404_NOT_FOUND,
    ResponseTypes.SYSTEM_ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR
}

responses = {
    status.HTTP_200_OK: {"model": List[Room]},
    status.HTTP_400_BAD_REQUEST: {"model": Message},
    status.HTTP_404_NOT_FOUND: {"model": Message},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": Message},
}

@router.get(path="", responses=responses)
async def room_list(
    request: Request,
    parameters: RoomListParameters = Depends()
) -> list[Room]:
    data = room_dicts()
    repo = MemRepo(data)

    parameters = request.query_params
    request: ValidRequest | InvalidRequest = build_room_list_request(parameters)

    room_use_case = RoomUseCase()
    result: ResponseSuccess | ResponseFailure = room_use_case.list(repo, request)

    return JSONResponse(status_code=STATUS_CODE[result.type], content=jsonable_encoder(result.value))


def room_dicts() -> List[dict]:
    room_1 = Room(
        code=uuid.uuid4(),
        size=100,
        price=10,
        longitude=-10.1,
        latitude=10.1
    )
    room_2 = Room(
        code=uuid.uuid4(),
        size=200,
        price=20,
        longitude=-0.2,
        latitude=20.1
    )
    room_3 = Room(
        code=uuid.uuid4(),
        size=300,
        price=30,
        longitude=-0.3,
        latitude=30.1
    )
    room_4 = Room(
        code=uuid.uuid4(),
        size=400,
        price=40,
        longitude=-0.4,
        latitude=40.1
    )

    return [room_1.dict(), room_2.dict(), room_3.dict(), room_4.dict()]