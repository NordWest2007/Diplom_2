import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetOrders(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_orders(self, token=None,):
        with allure.step('Получение  заказов пользователя'):
            headers = ''
            if token is not None:
                headers = {'Authorization': 'Bearer {}'.format(token)}
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.ORDER_URL}", headers=headers)
            self.status = self.response.status_code
            self.response_json = self.response.json()
