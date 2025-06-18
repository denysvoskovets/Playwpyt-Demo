import uuid
from faker import Faker

fake = Faker()

class UserFactory:
    def __init__(self):
        self.fake = Faker()

    def build(self, profile="normal"):
        user = {
            "title": "Mr",
            "name": self.fake.user_name(),
            "email_address": f"{self.fake.user_name()}_{uuid.uuid4().hex[:5]}@denys.com",
            "password": "1111",
            "days": str(self.fake.random_int(min=1, max=28)),
            "months": str(self.fake.random_int(min=1, max=12)),
            "years": str(self.fake.random_int(min=1980, max=2005)),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "company": self.fake.company(),
            "address1": self.fake.street_address(),
            "address2": "",
            "country": "United States",
            "state": self.fake.state_abbr(),
            "city": self.fake.city(),
            "zipcode": self.fake.zipcode(),
            "mobile_number": self.fake.msisdn()[:10]
        }

        if profile == "long_names":
            user["name"] = self.fake.user_name() + self.fake.pystr(min_chars=10, max_chars=15)
            user["first_name"] = self.fake.user_name() + self.fake.pystr(min_chars=20, max_chars=25)
            user["last_name"] = self.fake.user_name() + self.fake.pystr(min_chars=20, max_chars=25)
            user["email_address"] = f"{self.fake.user_name()}_{uuid.uuid4().hex[:15]}@denys.com"

        return user
