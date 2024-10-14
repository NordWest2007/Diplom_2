import random

import pytest

from data.data_user import DataUser
from endpoints.orders.get_ingredients import GetIngredients
from endpoints.users.create_user import CreateUser
from endpoints.users.delete_user import DeleteUser
from endpoints.users.login import Login


@pytest.fixture()
def create_user():
    create = CreateUser()
    create.create_user(DataUser.PAYLOAD_FOR_USER)
    yield create.token, DataUser.PAYLOAD_FOR_USER

    del_user = DeleteUser()
    del_user.delete(create.token)


@pytest.fixture()
def create_burger():
    ingredient = GetIngredients()
    ingredient.get_ingredients()
    ingredients = ingredient.response_json['data']
    burger = []
    buns = []
    sauces = []
    mains = []
    for i in range(0, len(ingredients)):
        if ingredients[i]['type'] == 'bun':
            buns.append(ingredients[i]['_id'])
        if ingredients[i]['type'] == 'sauce':
            sauces.append(ingredients[i]['_id'])
        if ingredients[i]['type'] == 'main':
            mains.append(ingredients[i]['_id'])
    burger.append(random.choice(buns))
    for i in range(0, random.randint(0, len(sauces))):
        burger.append(random.choice(sauces))
    for i in range(0, random.randint(0, len(mains))):
        burger.append(random.choice(mains))
    return burger


@pytest.fixture()
def authorization_user():
    create = CreateUser()
    create.create_user(DataUser.PAYLOAD_FOR_USER)

    login = Login()
    login.login_user(DataUser.PAYLOAD_FOR_USER)
    login.response_is(200)
    yield login.token

    del_user = DeleteUser()
    del_user.delete(login.token)
