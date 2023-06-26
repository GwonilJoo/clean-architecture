import uuid
import json

from src.domain.room import Room


class TestRoom:
    code = uuid.uuid4()
    size = 200
    price = 10
    longitude = -0.09998975
    latitude = 51.75436293

    init_dict = {
        "code": code,
        "size": size,
        "price": price,
        "longitude": longitude,
        "latitude": latitude,
    }


    def test_room_model_init(self):
        room = Room(
            code=self.code,
            size=self.size,
            price=self.price,
            longitude=self.longitude,
            latitude=self.latitude,
        )
        
        assert room.code == self.code
        assert room.size == self.size
        assert room.price == self.price
        assert room.longitude == self.longitude
        assert room.latitude == self.latitude


    def test_room_model_from_dict(self):
        room = Room.parse_obj(self.init_dict)

        assert room.code == self.code
        assert room.size == self.size
        assert room.price == self.price
        assert room.longitude == self.longitude
        assert room.latitude == self.latitude


    def test_room_model_to_dict(self):
        room = Room.parse_obj(self.init_dict)

        assert room.dict() == self.init_dict


    def test_room_model_comparison(self):
        room1 = Room.parse_obj(self.init_dict)
        room2 = Room.parse_obj(self.init_dict)

        assert room1 == room2

    
    def test_serialize_domain_room(self):
        room = Room.parse_obj(self.init_dict)

        expected_json = f'''
            {{
                "code": "{self.code}",
                "size": {self.size},
                "price": {self.price},
                "longitude": {self.longitude},
                "latitude": {self.latitude}
            }}
        '''

        json_room = room.json()

        assert json.loads(json_room) == json.loads(expected_json)