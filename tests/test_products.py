from playwright.sync_api import Page, expect
import allure

@allure.feature('Products')
def test_search_product(page: Page, home_page):
    product_name_to_search = 'Stylish'
    product_page = home_page.navigate().navigate_to_products().search_product(product_name_to_search)
    expect(product_page.product_title).to_contain_text(product_name_to_search)

@allure.feature('Products')
def test_add_product_to_cart(page: Page, home_page, product_page):
    product_name_to_search = 'Stylish'
    home_page.navigate().navigate_to_products().search_product(product_name_to_search)
    product_page.add_to_cart()
    expect(product_page.add_cart_button).to_be_visible()

