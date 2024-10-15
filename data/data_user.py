from faker import Faker


class DataUser:
    fake = Faker("ru_RU")
    DATA_PAYLOAD = ({"email": fake.email(),
                     "password": fake.password()
                     },
                    {"email": fake.email(),
                     "name": fake.name()
                     },
                    {"password": fake.password(),
                     "name": fake.name()
                     }
                    )
    PAYLOAD_FOR_USER = {"email": fake.email(),
                        "password": fake.password(),
                        "name": fake.name()
                        }
    JSON_ALREADY_EXIST = 'User already exists'
    JSON_NOT_FOUND_FIELD = 'Email, password and name are required fields'


