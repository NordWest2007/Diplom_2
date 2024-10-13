import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetUser(BaseEndpoint):
    status = None
    response_json = None

    def create_user(self) -> None:
        with allure.step('Получение данных о пользователе. Отправка запроса'):
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.GET_USER_URL}")
            self.status = self.response.status_code
            self.response_json = self.response.json()
