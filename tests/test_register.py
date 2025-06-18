import pytest
from playwright.sync_api import expect
import allure


@pytest.mark.smoke
@allure.feature('Registration')
@pytest.mark.parametrize("user_data", ["normal", "long_names"], indirect=True)
def test_register(user_data, login_page, home_page, register_page, clean_user):
    login_page.navigate()
    login_page.start_register(user_data['name'], user_data['email_address'])
    register_page.register_user(user_data)
    expect(home_page.account_created_label).to_be_visible()

@allure.feature('Registration')
def test_email_is_prefilled(user_data, login_page, register_page, clean_user):
    login_page.navigate()
    login_page.start_register(user_data['name'], user_data['email_address'])
    expect(register_page.email_input).to_have_value(user_data['email_address'])











