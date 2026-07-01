import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


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

    @allure.step('Переходим на страницу "Registration"')
    def load_page(self):
        self.visit_page(self.URL)

    def name_page(self):
        return self.get_text(*self.NAME_PAGE)

    @allure.step("Ввод пользовательских данных")
    def create_new_account(self, social_title, firstname, lastname, email, password, birthday):
        if social_title == 'm':
            self.click(*self.SOCIAL_TITLE_M)
        else:
            self.click(*self.SOCIAL_TITLE_W)
        with allure.step("Вводим имя пользователя"):
            self.send_keys(*self.FIRST_NAME_INPUT, text=firstname)
        with allure.step("Вводим фамилию пользователя"):
            self.send_keys(*self.LAST_NAME_INPUT, text=lastname)
        with allure.step("Вводим почтовый адрес пользователя"):
            self.send_keys(*self.EMAIL_INPUT, text=email)
        with allure.step("Вводим пароль"):
            self.send_keys(*self.PASSWORD_INPUT, text=password)
        with allure.step("Вводим дату рождения пользователя"):
            self.send_keys(*self.BIRTHDAY_INPUT, text=birthday)
        self.scroll(*self.CHECKBOX_PRIVACY_POLICY)
        time.sleep(2)
        with allure.step("Соглашаемся с политикой конфиденциальности"):
            self.click(*self.CHECKBOX_PRIVACY_POLICY)
        with allure.step("Соглашаемся с пользовательской политикой"):
            self.click(*self.CHECKBOX_CUSTOMER_POLICY)
        self.click(*self.BUTTON_CREATE_ACCOUNT)

    @allure.step("Проверяем наименование кнопки 'Create account'")
    def checking_name_button_create_account(self):
        self.checking_text_element(*self.BUTTON_CREATE_ACCOUNT, expected_value='Create account')

    @allure.step("Проверяем наименование секции 'First name'")
    def checking_name_section_firstname(self):
        self.checking_text_element(*self.SECTION_FIRST_NAME, expected_value='First name')

    @allure.step("Проверяем кликабельность кнопки 'Create your account'")
    def clickable_button_create_your_account(self):
        assert self.element_is_clickable(*self.BUTTON_CREATE_ACCOUNT), f"Button 'Create your account' is not clickable"

    @allure.step("Проверяем цвет кнопки 'Create your account'")
    def checking_color_button_create_your_account(self):
        self.checking_color_element(*self.BUTTON_CREATE_ACCOUNT, expected_value='rgba(11, 105, 246, 1)')

    @allure.step("Проверяем количество секций фильтрации")
    def checking_count_sections_to_filters(self):
        self.checking_count_element(*self.SECTIONS_TO_FILTERS, expected_value=10)
