from pages.header_component import Header


class BasePage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)
