from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'http://localhost:8081/login?back=http%3A%2F%2Flocalhost%3A8081%2F'
    NAME_PAGE = (By.CSS_SELECTOR, '[class="page-title-section"]')
    BUTTON_SIGN_IN = (By.ID, 'submit-login')
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, '[class="btn btn-outline-primary"]')
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, '[class="btn btn-basic"]')
    EMAIL_INPUT = (By.ID, 'field-email')
    PASSWORD_INPUT = (By.ID, 'field-password')

    def load_page(self):
        self.local_log('Open "Sign in" page')
        self.visit_page(self.URL)

    def sign_in(self, email, password):
        self.local_log('Input email and password for sign in')
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.BUTTON_SIGN_IN)

    def wait_sign_in(self):
        self.local_log('Wait sign in')
        self.wait(5, self.BUTTON_SIGN_IN)

    def name_page(self):
        self.local_log('Return name page')
        return self.get_text(*self.NAME_PAGE)

    def name_button_create_account(self):
        self.local_log('Return name button "Create  account"')
        return self.get_text(*self.BUTTON_CREATE_ACCOUNT)

    def color_button_sign_in(self):
        self.local_log('Return color button "Sign in"')
        return self.get_color(*self.BUTTON_SIGN_IN)

    def clickable_button_sign_in(self):
        self.local_log('Check that button "Sign in" is clickable')
        return self.element_is_clickable(*self.BUTTON_SIGN_IN)

    def visible_button_forgot_password(self):
        self.local_log('Check that button "Forgot password" is visible')
        return self.element_is_visible(*self.BUTTON_FORGOT_PASSWORD)
