import allure


class BaseEndpoint:

    def __init__(self):
        self.response = None

    def response_is(self, code):
        with allure.step(f'Ожидаемый ответ {code}, фактический {self.status}'):
            assert self.status == code

    def response_json_is(self, key, response):
        with allure.step(f'Ожидаемый ответ {self.response_json[key]}, фактический {response}'):
            assert self.response_json[key] == response
