from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    URL = 'http://localhost:8081/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm'
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '[class="product__add-to-cart-button btn btn-primary"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="product__price"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="product__name h2 mb-1"]')
    SHARE_ELEMENTS = (By.CSS_SELECTOR, '[class="ps-sharebuttons__list"] >*')

    def load_page(self):
        self.browser.get(self.URL)

    def visible_button_add_to_cart(self):
        return self.element_is_visible(*self.BUTTON_ADD_TO_CART)

    def color_button_add_to_cart(self):
        return self.get_color(*self.BUTTON_ADD_TO_CART)

    def price_product(self):
        return self.get_text(*self.PRODUCT_PRICE)

    def name_product(self):
        return self.get_text(*self.PRODUCT_NAME)

    def count_share_elements(self):
        return len(self.find_elements(*self.SHARE_ELEMENTS))


