import uuid
from typing import List

import pytest
from pydantic import parse_obj_as

from src.domain.room import Room
from src.repository.memrepo import MemRepo


@pytest.fixture
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


class TestRepository:
    def test_repository_list_without_parameters(self, room_dicts):
        repo = MemRepo(room_dicts)

        rooms = parse_obj_as(List[Room], room_dicts)

        assert repo.list() == rooms
