import allure
import pytest

from data.data_user import DataUser
from endpoints.users.create_user import CreateUser
from endpoints.users.delete_user import DeleteUser


@allure.feature('Создание пользователя')
@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.story('Позитивные данные')
    @allure.sub_suite('Позитивные данные')
    @allure.title('Уникальный пользователь')
    def test_create_user(self):
        create = CreateUser()
        create.create_user(DataUser.PAYLOAD_FOR_USER)
        create.response_is(200)
        create.response_json_is('success', True)
        assert create.response_json["user"]["email"] == DataUser.PAYLOAD_FOR_USER["email"]
        assert create.response_json["user"]["name"] == DataUser.PAYLOAD_FOR_USER["name"]

        del_user = DeleteUser()
        del_user.delete(create.token)
        del_user.response_is(202)
        create.response_json_is('success', True)

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('Пользователь уже зарегистрирован')
    def test_create_double(self, create_user):
        payload = create_user[1]
        create = CreateUser()
        create.create_user(payload)
        create.response_is(403)
        create.response_json_is('success', False)
        create.response_json_is('message', DataUser.JSON_ALREADY_EXIST)

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('Без обязательных полей')
    @pytest.mark.parametrize('payload', DataUser.DATA_PAYLOAD)
    def test_create_user_with_bad_payload(self, payload):
        create = CreateUser()
        create.create_user(payload)
        create.response_is(403)
        create.response_json_is('success', False)
        create.response_json_is('message', DataUser.JSON_NOT_FOUND_FIELD)
