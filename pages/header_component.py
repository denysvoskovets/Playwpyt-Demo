class Header:
    def __init__(self, page):
        self.page = page
        self.logout_button = page.locator('a[href="/logout"]')
        self.login_button = page.locator('a[href="/login"]')
        self.products_button = page.locator('a[href="/products"]')

    def navigate_to_login(self):
        self.login_button.click()

    def navigate_to_products(self):
        self.products_button.cluck()
