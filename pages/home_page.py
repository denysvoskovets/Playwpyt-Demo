from pages.base_page import BasePage
from pages.product_page import ProductPage
import allure


class HomePage(BasePage):

    URL="https://www.automationexercise.com/"

    def __init__(self, page):
        super().__init__(page)
        self.account_created_label = page.locator('h2[data-qa="account-created"]')
        self.search_input = page.locator('#search_product')
        self.submit_search_button = page.locator('#submit_search')
        self.view_product_buttons = page.locator('a:has-text("View Product")')

    def navigate(self):
        with allure.step('Open Home Page'):
            self.page.goto(self.URL)
            return self

    def navigate_to_products(self):
        with allure.step('Navigate to Products Page'):
            self.header.products_button.click()
            return self

    def open_product(self):
        with allure.step('Open First Product'):
            self.view_product_buttons.nth(0).click()


    def search_product(self, product_name: str):
        with allure.step(f'Search product {product_name}'):
            self.search_input.fill(product_name)
            self.submit_search_button.click()
            self.open_product()
        return ProductPage(self.page)


