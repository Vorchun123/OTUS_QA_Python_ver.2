from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    URL = 'http://localhost:8081/cart?action=show'
    PRODUCT_NAME_ON_CART_PAGE = (By.CSS_SELECTOR, '[class = "product-line__title"]')

    def load_page(self):
        self.browser.get(self.URL)

    def product_name_on_cart_page(self):
        return self.get_text(*self.PRODUCT_NAME_ON_CART_PAGE)
