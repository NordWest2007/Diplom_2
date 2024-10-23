import allure
import pytest
from faker import Faker

from endpoints.orders.create_order import CreateOrder


@allure.feature('Создание заказа')
@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.sub_suite('Позитивные данные')
    @allure.story('Позитивные данные')
    @allure.title('С ингредиентами(с авторизацией и без)')
    @pytest.mark.parametrize('authorization', ['None', 'Auth'], indirect=True)
    def test_create_order(self, create_burger, authorization):
        create = CreateOrder()
        create.create_order(token=authorization, ingredients=create_burger)
        create.response_is(200)
        create.response_json_is('success', True)

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('Без ингредиентов(с авторизацией и без)')
    @pytest.mark.parametrize('authorization', ['None', 'Auth'], indirect=True)
    def test_create_order_without_ingredients(self, create_burger, authorization):
        create = CreateOrder()
        create.create_order(token=authorization, ingredients='')
        create.response_is(400)
        create.response_json_is('success', False)

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('С неверным хешем ингредиентов')
    def test_create_order_with_bad_hash(self, create_burger, authorization_user):
        create = CreateOrder()
        fake = Faker('ru_RU')
        create.create_order(token=authorization_user, ingredients=[fake.uuid4()])
        create.response_is(500)
