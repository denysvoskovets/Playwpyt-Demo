from pages.base_page import BasePage
from pages.register_page import RegisterPage
import allure


class LoginPage(BasePage):
    URL = "https://www.automationexercise.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.login_email_input = page.locator('input[data-qa="login-email"]')
        self.login_password_input = page.locator('input[data-qa="login-password"]')
        self.login_btn = page.get_by_role('button', name = 'Login')
        self.login_error = page.locator('p', has_text="Your email or password is incorrect!")
        self.register_name_input = page.locator('input[data-qa="signup-name"]')
        self.register_email_input = page.locator('input[data-qa="signup-email"]')
        self.register_button = page.locator('[data-qa="signup-button"]')


    def navigate(self):
        with allure.step('Open Login Page'):
            self.page.goto(self.URL)

    def login(self, email, password):
        with allure.step(f'Perform Login with credentials {email} {password}'):
            self.login_email_input.fill(email)
            self.login_password_input.fill(password)
            self.login_btn.click()

    def logout(self):
        with allure.step('Perform logout'):
            self.header.logout_button.click()

    def start_register(self, name, email):
        with allure.step('Start registration'):
            self.register_name_input.fill(name)
            self.register_email_input.fill(email)
            self.register_button.click()
            return RegisterPage(self.page)