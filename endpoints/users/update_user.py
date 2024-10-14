import allure
import requests

from data.constants import Constants
from endpoints.base_endpoint import BaseEndpoint


class UpdateUser(BaseEndpoint):
    status = None
    response_json = None

    def update_user(self, payload, token=None) -> None:
        with allure.step('Обновление данных пользователя. Отправка запроса'):
            headers = ''
            if token is not None:
                headers = {'Content-Type': 'application/json',
                           'Authorization': 'Bearer {}'.format(token)}
            self.response = requests.patch(f'{Constants.BASE_URL}{Constants.USER_URL}', headers=headers, json=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
