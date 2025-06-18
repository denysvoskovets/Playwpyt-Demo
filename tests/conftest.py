import pytest
import json
from pathlib import Path
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage
from testdata.user_factory import UserFactory
from utils.user_api_helper import create_user_via_api, delete_account_from_session


# ------------------------------------------------------------
# Setup Run
# ------------------------------------------------------------

@pytest.fixture
def user_factory():
    return UserFactory()

@pytest.fixture
def user_data(user_factory, request):
    profile = getattr(request, "param", "normal")
    return user_factory.build(profile)

@pytest.fixture
def test_user(user_data, page):
    create_user_via_api(user_data)
    yield user_data

@pytest.fixture
def clean_user(page):
    yield
    cookies = page.context.cookies()
    delete_account_from_session(cookies)


# ------------------------------------------------------------
# Pages fixtures
# ------------------------------------------------------------

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)


@pytest.fixture
def register_page(page: Page) -> RegisterPage:
    return RegisterPage(page)


# ------------------------------------------------------------
# Project fixtures
# ------------------------------------------------------------
@pytest.fixture
def load_user_data(request):
    relative_path = request.param
    file_path = Path(__file__).parent.parent / relative_path

    if not file_path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path.resolve()}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data
