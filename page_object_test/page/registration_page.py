import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    URL = 'http://localhost:8081/registration'
    NAME_PAGE = (By.CSS_SELECTOR, '[class="page-title-section"]')
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, '[class="btn btn-primary form-control-submit"]')
    SECTIONS_TO_FILTERS = (By.CSS_SELECTOR, '[class="mb-3"]')
    SECTION_FIRST_NAME = (By.CSS_SELECTOR, '[for="field-firstname"]')
    SOCIAL_TITLE_M = (By.ID, 'field-id_gender_1')
    SOCIAL_TITLE_W = (By.ID, 'field-id_gender_2')
    FIRST_NAME_INPUT = (By.ID, 'field-firstname')
    LAST_NAME_INPUT = (By.ID, 'field-lastname')
    EMAIL_INPUT = (By.ID, 'field-email')
    PASSWORD_INPUT = (By.ID, 'field-password')
    BIRTHDAY_INPUT = (By.ID, 'field-birthday')
    CHECKBOX_PRIVACY_POLICY = (By.ID, 'field-psgdpr')
    CHECKBOX_CUSTOMER_POLICY = (By.ID, 'field-customer_privacy')
    SECTION_NAME = (By.CSS_SELECTOR, '[class="breadcrumb"]')

    def load_page(self):
        self.browser.get(self.URL)

    def name_page(self):
        return self.get_text(*self.NAME_PAGE)

    def clickable_button_create_account(self):
        return self.element_is_clickable(*self.BUTTON_CREATE_ACCOUNT)

    def color_button_create_account(self):
        return self.get_color(*self.BUTTON_CREATE_ACCOUNT)

    def count_section_to_filters(self):
        return len(self.find_elements(*self.SECTIONS_TO_FILTERS))

    def name_section(self):
        return self.get_text(*self.SECTION_FIRST_NAME)

    def create_new_account(self, social_title, firstname, lastname, email, password, birthday):
        if social_title == 'm':
            self.click(*self.SOCIAL_TITLE_M)
        else:
            self.click(*self.SOCIAL_TITLE_W)
        self.send_keys(*self.FIRST_NAME_INPUT, text=firstname)
        self.send_keys(*self.LAST_NAME_INPUT, text=lastname)
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.send_keys(*self.BIRTHDAY_INPUT, text=birthday)
        self.scroll(*self.CHECKBOX_PRIVACY_POLICY)
        time.sleep(2)
        self.click(*self.CHECKBOX_PRIVACY_POLICY)
        self.click(*self.CHECKBOX_CUSTOMER_POLICY)
        self.click(*self.BUTTON_CREATE_ACCOUNT)
