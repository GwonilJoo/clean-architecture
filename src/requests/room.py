from uuid import UUID

from pydantic import BaseModel, Extra

from src.requests.base import ValidRequest, InvalidRequest


class RoomListParameters(BaseModel):
    code__eq: UUID | None = None
    price__eq: int | None = None
    price__lt: int | None = None
    price__gt: int | None = None

    class Config:
        extra = Extra.forbid


def build_room_list_request(
        parameters: dict | None = None
    ) -> ValidRequest | InvalidRequest:
    try:
        room_list_parameters = RoomListParameters.parse_obj(parameters)
        request = ValidRequest(parameters=room_list_parameters)
    except Exception as exc:
        request = InvalidRequest(error=exc)
    return request
