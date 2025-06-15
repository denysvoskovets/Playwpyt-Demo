import pytest
import json
from pathlib import Path
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage


# ------------------------------------------------------------
# Setup Run
# ------------------------------------------------------------



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
    # go one level up from tests/ folder to root
    file_path = Path(__file__).parent.parent / relative_path

    if not file_path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path.resolve()}")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data



