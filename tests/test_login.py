import pytest
from playwright.sync_api import Page, expect
import utils.user_api_helper as user_api_helper
import allure

@pytest.fixture(autouse=True)
def clean_user(page):
    user_api_helper.create_user_via_api()
    yield
    cookies = page.context.cookies()
    user_api_helper.delete_account_from_session(cookies)

@allure.feature('Login Page')
@pytest.mark.parametrize("load_user_data", ["testdata/valid_user_login.json"], indirect=True)
def test_login_valid_credentials(page: Page, load_user_data, login_page):
    login_page.navigate()
    login_page.login(load_user_data['email_address'], load_user_data['password'])
    expect(login_page.header.logout_button).to_be_visible()

@allure.feature('Login Page')
@pytest.mark.parametrize("load_user_data", ["testdata/valid_user_login.json"], indirect=True)
def test_user_can_logout(page: Page, load_user_data, login_page):
    login_page.navigate()
    login_page.login(load_user_data['email_address'], load_user_data['password'])
    login_page.logout()
    expect(login_page.login_btn).to_be_visible()

@allure.feature('Login Page')
@pytest.mark.parametrize("load_user_data", ["testdata/invalid_user_password.json"], indirect=True)
def test_login_invalid_credentials(page: Page, load_user_data, login_page):
    login_page.navigate()
    login_page.login(load_user_data['email_address'], load_user_data['password'] + "some")
    login_page.login_btn.click()
    expect(login_page.login_error).to_be_visible()

@allure.feature('Login Page')
@pytest.mark.parametrize("load_user_data", ["testdata/invalid_user_password.json"], indirect=True)
def test_login_invalid_credentials(page: Page, load_user_data, login_page):
    login_page.navigate()
    login_page.login(load_user_data['email_address'], load_user_data['password'])
    login_page.login_btn.click()
    expect(login_page.login_error).to_be_visible()
