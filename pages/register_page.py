from pages.base_page import BasePage
from pages.home_page import HomePage
import allure


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.gender_m_dropdown = page.locator('#id_gender1')
        self.gender_f_dropdown = page.locator('#id_gender2')
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.password_input = page.locator('[data-qa="password"]')
        self.day_input = page.locator('[data-qa="days"]')
        self.month_input = page.locator('[data-qa="months"]')
        self.year_input = page.locator('[data-qa="years"]')
        self.letters_checkmark = page.locator('#newsletter')
        self.special_offers_checkmark = page.locator('#optin')
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address1_input = page.locator('[data-qa="address"]')
        self.address2_input = page.locator('[data-qa="address2"]')
        self.country_select = page.locator('[data-qa="country"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_number_input = page.locator('[data-qa="mobile_number"]')
        self.create_acc_button = page.locator('button[data-qa="create-account"]')


    def register_user(self, user_data: dict):
        with allure.step('Registrate user'):
            self.select_gender(user_data['title'])
            self.fill_input_name(user_data['name'])
            self.fill_input_email(user_data['email_address'])
            self.fill_input_password(user_data['password'])
            self.select_date_of_birth(
                day = user_data['days'],
                month= user_data['months'],
                year = user_data['years']
            )
            self.choose_newsletter(user_data)
            self.choose_option(user_data)
            self.fill_first_name(user_data['first_name'])
            self.fill_last_name(user_data['last_name'])
            self.fill_company(user_data['company'])
            self.fill_address1(user_data['address1'])
            self.fill_address2(user_data.get('address2', ''))
            self.select_country(user_data['country'])
            self.fill_state(user_data['state'])
            self.fill_city(user_data['city'])
            self.fill_zipcode(user_data['zipcode'])
            self.fill_mobile_number(user_data['mobile_number'])
            self.create_acc_button.click()
            return HomePage(self.page)


    def select_gender(self, title: str):
        if title.lower() == 'mr':
            self.gender_m_dropdown.check()
        else:
            self.gender_f_dropdown.check()

    def fill_input_name(self, name: str):
        self.name_input.fill(name)

    def fill_input_email(self, email: str):
        if self.email_input.is_enabled():
            self.email_input.fill(email)

    def fill_input_password(self, password: str):
        self.password_input.fill(password)

    def select_date_of_birth(self, day: str, month: str, year: str):
        self.day_input.select_option(value=day)
        self.month_input.select_option(value=month)
        self.year_input.select_option(value=year)

    def choose_newsletter(self, user_data: dict):
        if user_data.get('newsletter', True): #can do additional checks for value. But for this site it is redundant
            self.letters_checkmark.check()

    def choose_option(self, user_data: dict):
        if user_data.get('optin', True):  #the same
            self.special_offers_checkmark.check()

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def fill_company(self, company: str):
        self.company_input.fill(company)

    def fill_address1(self, address1: str):
        self.address1_input.fill(address1)

    def fill_address2(self, address2: str):
        self.address2_input.fill(address2)

    def select_country(self, country: str):
        self.country_select.select_option(label=country)

    def fill_state(self, state: str):
        self.state_input.fill(state)

    def fill_city(self, city: str):
        self.city_input.fill(city)

    def fill_zipcode(self, zipcode: str):
        self.zipcode_input.fill(zipcode)

    def fill_mobile_number(self, mobile_number: str):
        self.mobile_number_input.fill(mobile_number)