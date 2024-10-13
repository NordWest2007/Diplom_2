import pytest
from faker import Faker

from data.data_user import DataUser
from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser

fake = Faker("ru_RU")


@pytest.fixture()
def create_user():
    create = CreateUser()
    create.create_user(DataUser.PAYLOAD_FOR_USER)
    yield create.token,DataUser.PAYLOAD_FOR_USER

    del_user = DeleteUser()
    del_user.delete(create.token)
