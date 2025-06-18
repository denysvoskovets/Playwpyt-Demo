import requests

from config import BASE_URL


def delete_account_from_session(cookies: list[dict]):
    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"], domain=cookie["domain"])

    url = f"{BASE_URL}/delete_account"
    headers = {
        "Referer": f"{BASE_URL}",
    }
    response = session.get(url, headers=headers)
    return response


def get_csrf_token(session: requests.Session, url: str) -> str:
    token = session.cookies.get('csrftoken')
    if not token:
        raise Exception("CSRF token not found in cookies")
    return token


def create_user_via_api(user_data: dict) -> None:
    signup_url = f"{BASE_URL}/signup"

    session = requests.Session()
    session.get(signup_url)
    csrf_token = get_csrf_token(session, signup_url)

    headers = {
        "Referer": signup_url,
        "X-CSRFToken": csrf_token,
        "User-Agent": "Mozilla/5.0",
    }

    user_data = user_data.copy()
    user_data["form_type"] = "create_account"
    session.post(signup_url, data=user_data, headers=headers)
