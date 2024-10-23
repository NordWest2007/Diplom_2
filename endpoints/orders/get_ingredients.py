import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from data.constants import Constants


class GetIngredients(BaseEndpoint):
    status = None
    response_json = None

    def get_ingredients(self):
        with allure.step('Получение ингредиентов'):
            response = requests.get(f"{Constants.BASE_URL}{Constants.INGREDIENT_URL}")
            self.status = response.status_code
            self.response_json = response.json()
