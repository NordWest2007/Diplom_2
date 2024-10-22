import allure
import pytest

from data.data_user import DataUser
from endpoints.users.create_user import CreateUser
from endpoints.users.delete_user import DeleteUser
from endpoints.users.login import Login
from data.data_login import DataLogin


@allure.feature('Логин пользователя')
@allure.suite('Логин пользователя')
class TestLogin:

    @allure.story('Позитивные данные')
    @allure.sub_suite('Позитивные данные')
    @allure.title('с существующим логином')
    def test_login_user(self):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)

        login = Login()
        login.login_user(DataUser.PAYLOAD_FOR_USER)
        login.response_is(200)
        login.response_json_is('success', True)
        assert create.response_json["user"]["email"] == DataUser.PAYLOAD_FOR_USER["email"]
        assert create.response_json["user"]["name"] == DataUser.PAYLOAD_FOR_USER["name"]

        del_user = DeleteUser()
        del_user.delete(login.token)

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('с неверным логином или паролем')
    @pytest.mark.parametrize('payload', DataLogin.DATA_PAYLOAD)
    def test_login_user_with_bad_payload(self, payload):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)
        new_payload = DataUser.PAYLOAD_FOR_USER
        for key, value in payload.items():
            new_payload[key] = value
        login = Login()
        login.login_user(new_payload)
        login.response_json_is('success', False)
        login.response_json_is('message', DataLogin.JSON_PAYLOAD_INCORRECT)

        del_user = DeleteUser()
        del_user.delete(login.token)
