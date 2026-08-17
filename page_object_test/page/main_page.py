import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    URL = 'http://192.168.10.247:8081'
    PRODUCT_NAME_ON_MAIN_PAGE = (By.XPATH, '//*[@id="content"]/section[1]/div/div[6]/article/div/div[2]/h3/a')
    PRODUCT_ON_MAIN_PAGE = (By.CSS_SELECTOR, '[href="http://192.168.10.247:8081/home-accessories/6-mug-the-best-is-yet-to'
                                             '-come.html"]')
    BUTTON_CURRENCY_SELECTOR = (By.CSS_SELECTOR, '[class="expand-more _gray-darker"]')
    PRICE_PRODUCT = (By.XPATH, '//*[@id="content"]/section[1]/div/div[6]/article/div/div[2]/div[1]/span')
    EUR = (By.XPATH, '//*[@id="_desktop_currency_selector"]/div/ul/li[1]/a')
    USD = (By.XPATH, '//*[@id="_desktop_currency_selector"]/div/ul/li[2]/a')
    BUTTON_CONTACT_US = (By.ID, "contact-link")
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, '[class="btn btn-primary float-xs-right hidden-xs-down"]')
    BUTTON_SIGN_IN = (By.XPATH, '//*[@id="_desktop_user_info"]/div/a/span')
    BUTTON_NAME_ACCOUNT = (By.CSS_SELECTOR, '[class="account"]')
    BUTTON_MOBILE_MENU = (By.CSS_SELECTOR, '[aria-controls="mobileMenu"]')

    @allure.step('Переходим на страницу "Main"')
    def load_page(self):
        self.visit_page(self.URL)

    def product_name_on_main_page(self):
        text = self.get_text(*self.PRODUCT_NAME_ON_MAIN_PAGE)
        words = text.split()
        return ' '.join([
            words[0],
            words[1].capitalize(),
            *[w.lower() for w in words[2:]]
        ])

    def price_product(self):
        return self.get_text(*self.PRICE_PRODUCT)

    @allure.step("Проверяем что валюта изменилась")
    def checking_change_currency(self, price_euro):
        self.checking_text_element_not_equal(*self.PRICE_PRODUCT, expected_value=price_euro)

    @allure.step("Проверяем кликабельность кнопки 'Subscribe'")
    def clickable_button_add_to_cart(self):
        assert self.element_is_clickable(*self.BUTTON_SUBSCRIBE), f"Button 'Subscribe' is not clickable"

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
                time.sleep(1)
                self.click(*self.USD)
        if currency == "euro":
            self.local_log('Change price EUR € -> USD $')
            if self.get_text(*self.BUTTON_CURRENCY_SELECTOR) == "EUR €":
                pass
            else:
                self.click(*self.BUTTON_CURRENCY_SELECTOR)
                time.sleep(1)
                self.click(*self.EUR)

    @allure.step("Нажимаем на продукт")
    def click_on_product(self):
        self.click(*self.PRODUCT_ON_MAIN_PAGE)
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

    @allure.step("Проверяем цвет кнопки 'Subscribe'")
    def checking_color_button_subscribe(self):
        self.checking_color_element(*self.BUTTON_SUBSCRIBE, expected_value='rgba(36, 185, 215, 1)')
