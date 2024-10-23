import allure
import pytest

from data.data_update_user import DataUpdateUser
from endpoints.users.update_user import UpdateUser


@allure.feature('Изменение данных пользователя')
@allure.suite('Изменение данных пользователя')
class TestUpdateUser:
    @allure.story('Позитивные данные')
    @allure.sub_suite('Позитивные данные')
    @pytest.mark.parametrize('payload', DataUpdateUser.DATA_PAYLOAD)
    @allure.title('с  авторизацией')
    def test_update(self, create_user, payload):
        update = UpdateUser()
        update.update_user(payload, create_user[0])
        update.response_is(200)

        update.response_json_is('success', True)
        for key in ['name', 'email']:
            if key in payload:
                assert update.response_json["user"][key] == payload[key]
            else:
                assert update.response_json["user"][key] == create_user[1][key]

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @pytest.mark.parametrize('payload', DataUpdateUser.DATA_PAYLOAD)
    @allure.title('без авторизации')
    def test_update_without_token(self, create_user, payload):
        update = UpdateUser()
        update.update_user(payload)
        update.response_is(401)
        update.response_json_is('success', False)
        update.response_json_is('message', DataUpdateUser.JSON_BAD_UPDATE_USER)
