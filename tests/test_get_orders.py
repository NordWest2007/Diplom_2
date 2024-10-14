from endpoints.orders.get_orders import GetOrders


class TestGetOrders:
    def test_get_order_with_auth(self, authorization_user, create_order):
        orders = GetOrders()
        orders.get_orders(authorization_user)
        orders.response_is(200)
        orders.response_is_success(True)
        assert len(orders.response_json['orders']) == 1

    def test_get_order_without_auth(self):
        orders = GetOrders()
        orders.get_orders('')
        orders.response_is(401)
        orders.response_is_success(False)
