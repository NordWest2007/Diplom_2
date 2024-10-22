import allure

from endpoints.orders.get_orders import GetOrders


@allure.feature('Получение заказов конкретного пользователя')
@allure.suite('Получение заказов конкретного пользователя')
class TestGetOrders:
    @allure.story('Позитивные данные')
    @allure.sub_suite('Позитивные данные')
    @allure.title('авторизованный пользователь')
    def test_get_order_with_auth(self, authorization_user, create_order):
        orders = GetOrders()
        orders.get_orders(authorization_user)
        orders.response_is(200)
        orders.response_json_is('success', True)
        assert len(orders.response_json['orders']) == 1

    @allure.story('Негативные данные')
    @allure.sub_suite('Негативные данные')
    @allure.title('неавторизованный пользователь')
    def test_get_order_without_auth(self):
        orders = GetOrders()
        orders.get_orders('')
        orders.response_is(401)
        orders.response_json_is('success', False)

