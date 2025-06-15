import requests
from playwright.sync_api import Playwright

class APIHelper:
    def __init__(self, playwright: Playwright):
        self.request_context = playwright.request.new_context(
            base_url="https://www.automationexercise.com"
        )
        self.session = requests.Session()

    def get_csrf_token(self):
        self.request_context.get("/signup")
        storage = self.request_context.storage_state()
        cookies = storage.get("cookies", [])
        for cookie in cookies:
            if cookie['name'] == 'csrftoken':
                return cookie['value']
        return None

    def get_session_id(self):
        self.request_context.get("/account_created")
        storage = self.request_context.storage_state()
        cookies = storage.get("cookies", [])
        for cookie in cookies:
            if cookie['name'] == 'sessionid':
                return cookie['value']
        return None

    def create_user_via_api(self):
        csrf_token = self.get_csrf_token()
        if not csrf_token:
            raise Exception("CSRF token not found")

        headers = {
            "Referer": "https://www.automationexercise.com/signup",
            "X-CSRFToken": csrf_token,
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

        response = self.request_context.post(
            "/signup",
            form=user_data,
            headers=headers
        )

        print("Status:", response.status)
        # print("Response Text:", response.text())

        return response


    def delete_user_via_api(self):
        # csrf_token = self.get_csrf_token()
        # if not csrf_token:
        #     raise Exception("CSRF token not found")
        #
        # headers = {
        #     "Referer": "https://www.automationexercise.com/signup",
        #     "X-CSRFToken": csrf_token,  # if the site requires CSRF token header
        # }
        #
        # response = self.request_context.get("/delete_account")
        # return response

        csrf_token = self.get_csrf_token()
        session_id = self.get_session_id()
        print(f"Token: {csrf_token}")
        print(f"Session: {session_id}")

        if not csrf_token or not session_id:
            raise Exception("CSRF token or session ID not found")

        cookie_header = f"csrftoken={csrf_token}; sessionid={session_id}"

        headers = {
            "Referer": "https://www.automationexercise.com/signup",
            "X-CSRFToken": csrf_token,
            "Cookie": cookie_header,
        }

        response = self.request_context.get(
            "https://www.automationexercise.com/delete_account",
            headers=headers
        )
        return response

    # def delete_user(self) -> requests.Response:
    #     """
    #     Delete user: send GET request to ".../delete_account" with
    #     "sessionid" header.
    #     """
    #     if self.session.cookies.get("sessionid"):
    #         self.session.headers[
    #             "Cookie"
    #         ] += f"sessionid={self.session.cookies.get('sessionid')}"
    #
    #     response = self.session.get(
    #         url="https://www.automationexercise.com/delete_account"
    #     )
    #     return response