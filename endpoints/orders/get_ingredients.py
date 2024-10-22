import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetIngredients(BaseEndpoint):
    response = None
    status = None
    response_json = None

    def get_ingredients(self):
        with allure.step('Получение ингредиентов'):
            self.response = requests.get(f"{Constants.BASE_URL}{Constants.INGREDIENT_URL}")
            self.status = self.response.status_code
            self.response_json = self.response.json()
