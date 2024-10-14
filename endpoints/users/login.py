import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class Login(BaseEndpoint):
    status = None
    response_json = None
    token = None
    refreshToken = None

    def login_user(self, payload) -> None:
        with allure.step('Авторизация. Отправка запроса'):

            self.response = requests.post(f'{Constants.BASE_URL}{Constants.LOGIN_URL}', data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
            if self.status == 200:
                self.token = self.response_json['accessToken'].split(' ')[1]
                self.refreshToken = self.response_json['refreshToken']
