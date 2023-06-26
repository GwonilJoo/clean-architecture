import uuid

import pytest

from src.domain.room import Room
from src.use_cases.room import RoomUseCase


@pytest.fixture
def domain_rooms():
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

    return [room_1, room_2, room_3, room_4]


class TestRoomUseCase:
    def test_room_list_without_parameters(domain_rooms):
        repo = domain_rooms
        room_use_case = RoomUseCase()
        result = room_use_case.list(repo)

        assert result == domain_rooms
