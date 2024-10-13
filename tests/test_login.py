import pytest

from data.data_user import DataUser
from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser
from endpoints.login import Login
from data.data_login import DataLogin


class TestLogin:

    def test_login_user(self):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)

        login = Login()
        login.login_user(DataUser.PAYLOAD_FOR_USER)
        login.response_is(200)
        assert create.response_json["user"]["email"] == DataUser.PAYLOAD_FOR_USER["email"]
        assert create.response_json["user"]["name"] == DataUser.PAYLOAD_FOR_USER["name"]

        del_user = DeleteUser()
        del_user.delete(login.token)

    @pytest.mark.parametrize('payload', DataLogin.DATA_PAYLOAD)
    def test_login_user_with_bad_payload(self, payload):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)
        new_payload=DataUser.PAYLOAD_FOR_USER
        for key,value in payload.items():
            new_payload[key]=value
        login = Login()
        login.login_user(new_payload)
        login.response_is(401)
        login.response_json_is(DataLogin.JSON_PAYLOAD_INCORRECT)

        del_user = DeleteUser()
        del_user.delete(login.token)
