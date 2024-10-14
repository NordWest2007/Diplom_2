import pytest

from data.data_update_user import DataUpdateUser
from endpoints.users.update_user import UpdateUser


class TestUpdateUser:
    @pytest.mark.parametrize('payload', DataUpdateUser.DATA_PAYLOAD)
    def test_update(self, create_user, payload):
        update = UpdateUser()
        update.update_user(payload, create_user[0])
        update.response_is(200)
        assert update.response_json["success"] == True
        for key in ['name', 'email']:
            if key in payload:
                assert update.response_json["user"][key] == payload[key]
            else:
                assert update.response_json["user"][key] == create_user[1][key]

    @pytest.mark.parametrize('payload', DataUpdateUser.DATA_PAYLOAD)
    def test_update_without_token(self, create_user, payload):
        update = UpdateUser()
        update.update_user(payload)
        update.response_is(401)
        update.response_json_is(DataUpdateUser.JSON_BAD_UPDATE_USER)
