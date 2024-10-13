import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class CreateOrders(BaseEndpoint):
    status = None
    response_json = None

    def create_user(self, payload) -> None:
        with allure.step('Создание заказа. Отправка запроса'):
            self.response = requests.post(f'{Constants.BASE_URL}{Constants.ORDER_URL}', data=payload)
            self.status = self.response.status_code
            self.response_json = self.response.json()
