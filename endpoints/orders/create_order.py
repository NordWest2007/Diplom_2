import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class CreateOrder(BaseEndpoint):
    status = None
    response_json = None

    def create_order(self, token=None, ingredients=None) -> None:
        with allure.step('Создание заказа. Отправка запроса'):
            headers=''
            if token is not None:
                headers = {'Authorization': 'Bearer {}'.format(token)}
            payload = {"ingredients": ingredients}
            response = requests.post(f'{Constants.BASE_URL}{Constants.ORDER_URL}', data=payload, headers=headers)
            self.status = response.status_code
            if response.status_code!=500:
                self.response_json = response.json()
