from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    URL = 'http://localhost:8081/cart?action=show'
    PRODUCT_NAME_ON_CART_PAGE = (By.CSS_SELECTOR, '[class = "product-line__title"]')

    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем наименование продукта в корзине")
    def checking_product_name_in_cart(self, name_on_main):
        self.checking_text_element(*self.PRODUCT_NAME_ON_CART_PAGE, expected_value=name_on_main)

