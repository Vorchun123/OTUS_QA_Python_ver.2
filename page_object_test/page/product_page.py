from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ProductPage(BasePage):
    URL = 'http://localhost:8081/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm'
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '[class="product__add-to-cart-button btn btn-primary"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="product__price"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="product__name h2 mb-1"]')
    SHARE_ELEMENTS = (By.CSS_SELECTOR, '[class="ps-sharebuttons__list"] >*')

    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем цвет кнопки 'Add to cart'")
    def checking_color_button_add_to_cart(self):
        self.checking_color_element(*self.BUTTON_ADD_TO_CART, expected_value='rgba(11, 105, 246, 1)')

    @allure.step("Проверяем наименование продукта")
    def checking_name_product(self):
        self.checking_text_element(*self.PRODUCT_NAME, expected_value="The best is yet to come' Framed poster")

    @allure.step("Проверяем видимость кнопки 'Add to cart'")
    def visible_button_add_to_cart(self):
        assert self.element_is_visible(*self.BUTTON_ADD_TO_CART), f"Button 'Contact us' is not visible"

    @allure.step("Проверяем стоимость продукта")
    def checking_price_product(self):
        self.checking_text_element(*self.PRODUCT_PRICE, expected_value="Price:\n€29.00")

    @allure.step("Проверяем количество возможностей чтобы поделиться")
    def checking_count_share_elements(self):
        self.checking_count_element(*self.SHARE_ELEMENTS, expected_value=3)
