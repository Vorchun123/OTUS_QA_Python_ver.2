import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    URL = 'http://localhost:8081'
    PRODUCT_NAME_ON_MAIN_PAGE = (By.CSS_SELECTOR, '[aria-label = "View product The adventure begins Framed poster"]')
    BUTTON_CURRENCY_SELECTOR = (By.CSS_SELECTOR, '[class="ps-currencyselector"]')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '[aria-label="View product Hummingbird printed sweater"]~['
                                      'class="product-miniature__prices"]')
    EUR = (By.CSS_SELECTOR, '[value="http://localhost:8081/?SubmitCurrency=1&id_currency=1"]')
    USD = (By.CSS_SELECTOR, '[value="http://localhost:8081/?SubmitCurrency=1&id_currency=2"]')
    BUTTON_CONTACT_US = (By.CSS_SELECTOR, "[class='ps-contactinfo__email']")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '[aria-label="Add to cart The adventure begins Framed poster"]')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, '[class="d-none d-md-inline header-block__title"]')
    BUTTON_NAME_ACCOUNT = (By.CSS_SELECTOR, '[class="header-block__title d-lg-inline d-none"]')
    BUTTON_MOBILE_MENU = (By.CSS_SELECTOR, '[aria-controls="mobileMenu"]')
    MODAL_WINDOWS = (By.CSS_SELECTOR, '[class="modal-content"]')

    @allure.step('Переходим на страницу "Main"')
    def load_page(self):
        self.visit_page(self.URL)

    def product_name_on_main_page(self):
        return self.get_text(*self.PRODUCT_NAME_ON_MAIN_PAGE)

    def price_product(self):
        return self.get_text(*self.PRICE_PRODUCT)

    @allure.step("Проверяем что валюта изменилась")
    def checking_change_currency(self, price_euro):
        self.checking_text_element_not_equal(*self.PRICE_PRODUCT, expected_value=price_euro)

    @allure.step("Проверяем кликабельность кнопки 'Add to cart'")
    def clickable_button_add_to_cart(self):
        assert self.element_is_clickable(*self.BUTTON_ADD_TO_CART), f"Button 'Add to cart' is not clickable"

    @allure.step("Проверяем видимость кнопки 'Contact us'")
    def visible_button_contact_us(self):
        assert self.element_is_visible(*self.BUTTON_CONTACT_US), f"Button 'Contact us' is not visible"

    @allure.step("Переводим цену продукта в выбранную валюту")
    def change_price(self, currency):
        if currency == "dollar":
            self.local_log('Change price USD $ -> EUR €')
            if self.get_text(*self.BUTTON_CURRENCY_SELECTOR) == "USD $":
                pass
            else:
                self.click(*self.BUTTON_CURRENCY_SELECTOR)
                self.click(*self.USD)
        if currency == "euro":
            self.local_log('Change price EUR € -> USD $')
            if self.get_text(*self.BUTTON_CURRENCY_SELECTOR) == "EUR €":
                pass
            else:
                self.click(*self.BUTTON_CURRENCY_SELECTOR)
                self.click(*self.EUR)

    @allure.step("Нажимаем на элемент BUTTON_ADD_TO_CART")
    def add_to_cart(self):
        self.click(*self.BUTTON_ADD_TO_CART)

    def wait_to_add(self):
        self.wait_visible(10, self.MODAL_WINDOWS)

    @allure.step("Скроллим до элемента BUTTON_ADD_TO_CART")
    def scroll_to_button_add_to_cart(self):
        self.scroll(*self.BUTTON_ADD_TO_CART)
        time.sleep(1)

    @allure.step("Проверяем имя пользователя")
    def checking_name_user(self, firstname, lastname):
        self.checking_text_element(*self.BUTTON_NAME_ACCOUNT, expected_value=firstname + ' ' + lastname)

    @allure.step("Проверяем наименование кнопки 'Contact us'")
    def checking_name_button_contact_us(self):
        self.checking_text_element(*self.BUTTON_CONTACT_US, expected_value='Contact us')

    @allure.step("Проверяем наименование кнопки 'Sign in'")
    def checking_name_button_sign_in(self):
        self.checking_text_element(*self.BUTTON_SIGN_IN, expected_value='Sign in')

    @allure.step("Проверяем цвет кнопки 'Add to cart'")
    def checking_color_button_add_to_cart(self):
        self.checking_color_element(*self.BUTTON_ADD_TO_CART, expected_value='rgba(11, 105, 246, 1)')
