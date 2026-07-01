from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminSignInPage(BasePage):
    URL = 'http://localhost:8081/administration/login'
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    LOG_IN_BUTTON = (By.ID, 'submit_login')

    @allure.step('Переходим на страницу "Admin-Sign in"')
    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Авторизуемся в системе")
    def sign_in(self, email, password):
        with allure.step("Вводим почтовый адрес"):
            self.send_keys(*self.EMAIL_INPUT, text=email)
        with allure.step("Вводим пароль"):
            self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOG_IN_BUTTON)
        self.wait(5, self.LOG_IN_BUTTON)
