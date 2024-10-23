from faker import Faker


class DataUpdateUser:
    fake = Faker("ru_RU")
    DATA_PAYLOAD = ({"email": fake.email()},
                    {"name": fake.name()},
                    {"password": fake.password()}
                    )
    DATA_PAYLOAD_EMAIL = {"email": fake.email()}
    DATA_PAYLOAD_NAME = {"name": fake.name()}
    DATA_PAYLOAD_PASSWORD = {"password": fake.password()}

    JSON_BAD_UPDATE_USER = "You should be authorised"
