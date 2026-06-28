import time
from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


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

    def load_page(self):
        self.local_log('Open "Main" page')
        self.visit_page(self.URL)

    def product_name_on_main_page(self):
        self.local_log('Return product name')
        return self.get_text(*self.PRODUCT_NAME_ON_MAIN_PAGE)

    def price_product(self):
        self.local_log('Return product price')
        return self.get_text(*self.PRICE_PRODUCT)

    def name_button_contact_us(self):
        self.local_log('Return name button "Contact us"')
        return self.get_text(*self.BUTTON_CONTACT_US)

    def name_button_sign_in(self):
        self.local_log('Return name button "Sign in"')
        return self.get_text(*self.BUTTON_SIGN_IN)

    def color_button_add_to_cart(self):
        self.local_log('Return color button "Add to cart"')
        return self.get_color(*self.BUTTON_ADD_TO_CART)

    def clickable_button_add_to_cart(self):
        self.local_log('Check that button "Add to cart" is clickable')
        return self.element_is_clickable(*self.BUTTON_ADD_TO_CART)

    def visible_button_contact_us(self):
        self.local_log('Check that button "Contact us" is visible')
        return self.element_is_visible(*self.BUTTON_CONTACT_US)

    def change_price(self, currency):
        self.local_log('Change price')
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

    def add_to_cart(self):
        self.local_log('Add to cart')
        self.click(*self.BUTTON_ADD_TO_CART)

    def wait_to_add(self):
        self.local_log('Wait to add to cart')
        self.wait_visible(10, self.MODAL_WINDOWS)

    def scroll_to_button_add_to_cart(self):
        self.local_log('Scroll to button "Add to cart"')
        self.scroll(*self.BUTTON_ADD_TO_CART)
        time.sleep(1)

    def name_account(self):
        self.local_log('Return name account')
        return self.get_text(*self.BUTTON_NAME_ACCOUNT)

