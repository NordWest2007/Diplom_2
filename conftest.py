import pytest

from data.data_user import DataUser
from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser


@pytest.fixture()
def create_user():
    create = CreateUser()
    create.create_user(DataUser.PAYLOAD_FOR_USER)
    yield create.token, DataUser.PAYLOAD_FOR_USER,create.refreshToken


    del_user = DeleteUser()
    del_user.delete(create.refreshToken)
