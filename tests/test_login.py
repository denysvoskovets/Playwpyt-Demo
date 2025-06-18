import pytest
from playwright.sync_api import Page, expect
import allure


@pytest.mark.smoke
@allure.feature('Login Page')
def test_login_valid_credentials(login_page, test_user, clean_user):
    login_page.navigate()
    login_page.login(test_user["email_address"], test_user["password"])
    expect(login_page.header.logout_button).to_be_visible()


@allure.feature('Login Page')
def test_user_can_logout(test_user, login_page, clean_user):
    login_page.navigate()
    login_page.login(test_user['email_address'], test_user['password'])
    login_page.logout()
    expect(login_page.login_btn).to_be_visible()


@allure.feature('Login Page')
def test_login_invalid_credentials(test_user, login_page, clean_user):
    login_page.navigate()
    login_page.login(test_user['email_address'], test_user['password'] + "some")
    login_page.login_btn.click()
    expect(login_page.login_error).to_be_visible()
