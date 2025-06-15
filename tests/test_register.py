import pytest
from playwright.sync_api import expect
import utils.user_api_helper as user_api_helper
import allure


@pytest.fixture(autouse=True)
def clean_user(page):
    yield
    cookies = page.context.cookies()
    user_api_helper.delete_account_from_session(cookies)

@pytest.mark.smoke
@allure.feature('Registration')
@pytest.mark.parametrize("load_user_data", ["testdata/valid_user_registration.json"], indirect=True)
def test_register(page, load_user_data, login_page, home_page, register_page):
    user_data = load_user_data
    login_page.navigate()
    login_page.start_register(user_data['name'], user_data['email_address'])
    register_page.register_user(user_data)
    expect(home_page.account_created_label).to_be_visible()

@allure.feature('Registration')
@pytest.mark.parametrize("load_user_data", ["testdata/valid_user_registration.json"], indirect=True)
def test_email_is_prefilled(page, load_user_data, login_page, register_page):
    user_data = load_user_data
    login_page.navigate()
    login_page.start_register(user_data['name'], user_data['email_address'])
    expect(register_page.email_input).to_have_value(user_data['email_address'])











