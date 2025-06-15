import requests

def delete_account_from_session(cookies: list[dict]):
    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"], domain=cookie["domain"])

    url = "https://www.automationexercise.com/delete_account"
    headers = {
        "Referer": "https://www.automationexercise.com/",
    }
    response = session.get(url, headers=headers)
    return response


def get_csrf_token(session: requests.Session, url: str) -> str:

    resp = session.get(url)
    token = session.cookies.get('csrftoken')
    if not token:
        raise Exception("CSRF token not found in cookies")
    return token


def create_user_via_api():

    base_url = "https://www.automationexercise.com"
    signup_url = f"{base_url}/signup"

    session = requests.Session()

    csrf_token = get_csrf_token(session, signup_url)

    headers = {
        "Referer": signup_url,
        "X-CSRFToken": csrf_token,
        # Add common headers if needed
        "User-Agent": "Mozilla/5.0",
    }

    user_data = {
        "title": "Mr",
        "name": "denys_test",
        "email_address": "denys_test_test@gmail.com",
        "password": "1111",
        "days": "1",
        "months": "1",
        "years": "2000",
        "first_name": "Denys",
        "last_name": "Test",
        "company": "TestCo",
        "address1": "Some street",
        "address2": "",
        "country": "United States",
        "state": "Some state",
        "city": "Some city",
        "zipcode": "12345",
        "mobile_number": "1234567890",
        "form_type": "create_account"
    }

    response = session.post(signup_url, data=user_data, headers=headers)

    return response
    # base_url = "https://www.automationexercise.com"
    # signup_url = f"{base_url}/signup"
    #
    # session = requests.Session()
    # csrf_token = get_csrf_token(session, signup_url)
    #
    # headers = {
    #     "Referer": signup_url,
    #     "X-CSRFToken": csrf_token,
    #     "User-Agent": "Mozilla/5.0",
    # }
    #
    # response = session.post(signup_url, data=user_data, headers=headers)
    # return response