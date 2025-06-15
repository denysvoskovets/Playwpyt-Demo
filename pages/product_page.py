from pages.base_page import BasePage
import allure


class ProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.product_title = page.locator("div.product-information h2")
        self.view_cart_button = page.get_by_text("View Cart")
        self.add_cart_button = page.get_by_role("button", name="Add to cart")



    def add_to_cart(self):
        with allure.step('Add product to cart'):
            self.add_cart_button.click()
