import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class Login(BaseEndpoint):
    status = None
    response_json = None

    def create_user(self, payload) -> None:
        with allure.step('Авторизация. Отправка запроса'):
            self.response = requests.post(f'{Constants.BASE_URL}{Constants.LOGIN_URL}', data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
