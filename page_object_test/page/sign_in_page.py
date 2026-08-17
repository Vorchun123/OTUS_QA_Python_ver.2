from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class SignInPage(BasePage):
    URL = 'http://192.168.10.247:8081/login?back=http%3A%2F%2Flocalhost%3A8081%2F'
    NAME_PAGE = (By.CSS_SELECTOR, '[class="page-title-section"]')
    BUTTON_SIGN_IN = (By.ID, 'submit-login')
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, '[data-link-action="display-register-form"]')
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, '[class="forgot-password"]')
    EMAIL_INPUT = (By.ID, 'field-email')
    PASSWORD_INPUT = (By.ID, 'field-password')

    @allure.step('Переходим на страницу "Sign in"')
    def load_page(self):
        self.visit_page(self.URL)

    @allure.step('Вводим данные email и password')
    def sign_in(self, email, password):
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.BUTTON_SIGN_IN)

    @allure.step('Ждем пока исчезнет эдемент BUTTON_SIGN_IN')
    def wait_sign_in(self):
        self.wait(5, self.BUTTON_SIGN_IN)

    @allure.step("Проверяем наименование кнопки 'Sign in'")
    def checking_name_button_sign_in(self):
        self.checking_text_element(*self.BUTTON_SIGN_IN, expected_value='SIGN IN')

    @allure.step("Проверяем наименование кнопки 'Create your account'")
    def checking_name_button_create_your_account(self):
        self.checking_text_element(*self.BUTTON_CREATE_ACCOUNT, expected_value='No account? Create one here')

    @allure.step("Проверяем цвет кнопки 'Sign in'")
    def checking_color_button_sign_in(self):
        self.checking_color_element(*self.BUTTON_SIGN_IN, expected_value='rgba(36, 185, 215, 1)')

    @allure.step("Проверяем кликабельность кнопки 'Sign in'")
    def clickable_button_sign_in(self):
        assert self.element_is_clickable(*self.BUTTON_SIGN_IN), f"Button 'Sign in' is not clickable"

    @allure.step("Проверяем видимость кнопки 'Forgot password'")
    def visible_button_forgot_password(self):
        assert self.element_is_visible(*self.BUTTON_FORGOT_PASSWORD), f"Button 'Forgot password' is not visible"

