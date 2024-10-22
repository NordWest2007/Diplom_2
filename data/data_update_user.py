from faker import Faker


class DataUpdateUser:
    fake = Faker("ru_RU")
    DATA_PAYLOAD = ({"email": fake.email()},
                    {"name": fake.name()},
                    {"password": fake.password()}
                    )

    JSON_BAD_UPDATE_USER = "You should be authorised"
