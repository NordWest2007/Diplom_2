import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetOrder(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_order_by_id(self):
        with allure.step('Получение  заказов пользователя'):
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.ORDER_URL}")
            self.status = self.response.status_code
            self.response_json = self.response.json()
