import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetOrders(BaseEndpoint):
    status = None
    response_json = None

    def get_orders(self, token=None,):
        with allure.step('Получение  заказов пользователя'):
            headers = ''
            if token is not None:
                headers = {'Authorization': 'Bearer {}'.format(token)}
            response = requests.get(f"{Constants.BASE_URL}{Constants.ORDER_URL}", headers=headers)
            self.status = response.status_code
            self.response_json = response.json()
