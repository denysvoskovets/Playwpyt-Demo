import uuid
from faker import Faker

fake = Faker()

def generate_user():
    return {
        "title": "Mr",
        "name": fake.user_name(),
        "email_address": f"{fake.user_name()}_{uuid.uuid4().hex[:5]}@denys.com",
        "password": "1111",
        "days": str(fake.random_int(min=1, max=28)),
        "months": str(fake.random_int(min=1, max=12)),
        "years": str(fake.random_int(min=1980, max=2005)),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": "",
        "country": "United States",
        "state": fake.state_abbr(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.msisdn()[:10]
    }