from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ProductPage(BasePage):
    URL = 'http://192.168.10.247:8081/home-accessories/6-mug-the-best-is-yet-to-come.html'
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '[class="btn btn-primary add-to-cart"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="current-price-value"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="h1"]')
    SHARE_ELEMENTS = (By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[3]/div/ul/li')
    MODAL_WINDOWS = (By.CSS_SELECTOR, '#blockcart-modal ')

    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем цвет кнопки 'Add to cart'")
    def checking_color_button_add_to_cart(self):
        self.checking_color_element(*self.BUTTON_ADD_TO_CART, expected_value='rgba(36, 185, 215, 1)')

    @allure.step("Проверяем наименование продукта")
    def checking_name_product(self):
        self.checking_text_element(*self.PRODUCT_NAME, expected_value="MUG THE BEST IS YET TO COME")

    @allure.step("Проверяем видимость кнопки 'Add to cart'")
    def visible_button_add_to_cart(self):
        assert self.element_is_visible(*self.BUTTON_ADD_TO_CART), f"Button 'Contact us' is not visible"

    @allure.step("Проверяем стоимость продукта")
    def checking_price_product(self):
        self.checking_text_element(*self.PRODUCT_PRICE, expected_value="€11.90")

    @allure.step("Проверяем количество возможностей чтобы поделиться")
    def checking_count_share_elements(self):
        self.checking_count_element(*self.SHARE_ELEMENTS, expected_value=3)

    @allure.step("Нажимаем на элемент BUTTON_ADD_TO_CART")
    def add_to_cart(self):
        self.click(*self.BUTTON_ADD_TO_CART)

    def wait_to_add(self):
        self.wait_visible(10, self.MODAL_WINDOWS)
