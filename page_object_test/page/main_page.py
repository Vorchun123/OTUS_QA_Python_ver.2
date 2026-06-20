import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    STATUS = (By.CSS_SELECTOR, '[class = "header-block__title d-lg-inline d-none"]')
    MODAL_WINDOWS = (By.CSS_SELECTOR, '[class="modal-content"]')

    def load_page(self):
        self.browser.get(self.URL)

    def product_name_on_main_page(self):
        return self.get_text(*self.PRODUCT_NAME_ON_MAIN_PAGE)

    def price_product(self):
        return self.get_text(*self.PRICE_PRODUCT)

    def name_button_contact_us(self):
        return self.get_text(*self.BUTTON_CONTACT_US)

    def name_button_sign_in(self):
        return self.get_text(*self.BUTTON_SIGN_IN)

    def color_button_add_to_cart(self):
        return self.get_color(*self.BUTTON_ADD_TO_CART)

    def clickable_button_add_to_cart(self):
        return self.element_is_clickable(*self.BUTTON_ADD_TO_CART)

    def visible_button_contact_us(self):
        return self.element_is_visible(*self.BUTTON_CONTACT_US)

    def change_price(self, currency):
        if currency == "dollar":
            if self.get_text(*self.BUTTON_CURRENCY_SELECTOR) == "USD $":
                pass
            else:
                self.click(*self.BUTTON_CURRENCY_SELECTOR)
                self.click(*self.USD)
        if currency == "euro":
            if self.get_text(*self.BUTTON_CURRENCY_SELECTOR) == "EUR €":
                pass
            else:
                self.click(*self.BUTTON_CURRENCY_SELECTOR)
                self.click(*self.EUR)

    def account_status(self):
        return self.get_text(*self.STATUS)

    def add_to_cart(self):
        self.click(*self.BUTTON_ADD_TO_CART)
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.MODAL_WINDOWS))

    def scroll_to_button_add_to_cart(self):
        self.scroll(*self.BUTTON_ADD_TO_CART)
        time.sleep(1)

    def name_account(self):
        return self.get_text(*self.BUTTON_NAME_ACCOUNT)

