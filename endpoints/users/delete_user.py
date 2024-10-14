import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class DeleteUser(BaseEndpoint):
    status = None
    response_json = None
    response = None

    def delete(self, token):
        with allure.step('Удаление пользователя'):
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer {}'.format(token)}
            self.response = requests.delete(f"{Constants.BASE_URL}{Constants.USER_URL}", headers=headers)
            self.status = self.response.status_code
            self.response_json = self.response.json()
