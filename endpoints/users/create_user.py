import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class CreateUser(BaseEndpoint):
    status = None
    response_json = None
    token = None
    refreshToken = None

    def create_user(self, payload) -> None:
        with allure.step('Создание пользователя. Отправка запроса'):
            self.response = requests.post(f'{Constants.BASE_URL}{Constants.CREATE_USER_URL}', data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
            if self.status == 200:
                self.token = self.response_json['accessToken'].split(' ')[1]
                self.refreshToken = self.response_json['refreshToken']
