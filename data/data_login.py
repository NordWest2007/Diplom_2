from faker import Faker


class DataLogin:
    fake = Faker("ru_RU")
    DATA_PAYLOAD = ({"email": fake.email()},
                    {"password": fake.password()},
                    {"email": fake.email(),
                     "password": fake.password()}
                    )

    JSON_PAYLOAD_INCORRECT = "email or password are incorrect"
