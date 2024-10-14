from faker import Faker


class DataUpdateUser:
    fake = Faker("ru_RU")
    DATA_PAYLOAD = ({"email": fake.email()},
                    {"name": fake.name()},
                    {"password": fake.password()}
                    )

    JSON_UPDATE_USER = {
        "success": True,
        "user": {
            "email": {},
            "name": {}
        }
    }

    JSON_BAD_UPDATE_USER ={  "success": False, "message": "You should be authorised"}