import pytest

from data.data_user import DataUser
from endpoints.users.create_user import CreateUser
from endpoints.users.delete_user import DeleteUser


class TestCreateUser:

    def test_create_user(self):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)
        create.response_is(200)
        assert create.response_json["user"]["email"] == DataUser.PAYLOAD_FOR_USER["email"]
        assert create.response_json["user"]["name"] == DataUser.PAYLOAD_FOR_USER["name"]

        del_user = DeleteUser()
        del_user.delete(create.token)
        del_user.response_is(202)
        del_user.response_json_is({'success': True, 'message': 'User successfully removed'})

    def test_create_double(self, create_user):
        payload = create_user[1]
        create = CreateUser()
        create.create_user(payload)
        create.response_is(403)
        create.response_json_is(DataUser.JSON_ALREADY_EXIST)

    @pytest.mark.parametrize('payload', DataUser.DATA_PAYLOAD)
    def test_create_user_with_bad_payload(self, payload):
        create = CreateUser()
        create.create_user(payload)
        create.response_is(403)
        create.response_json_is(DataUser.JSON_NOT_FOUND_FIELD)
