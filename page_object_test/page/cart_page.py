from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    URL = 'http://192.168.10.247:8081/cart?action=show'
    PRODUCT_NAME_ON_CART_PAGE = (By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/ul/li/div/div[2]/div[1]/a')

    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем наименование продукта в корзине")
    def checking_product_name_in_cart(self, name_on_main):
        self.checking_text_element(*self.PRODUCT_NAME_ON_CART_PAGE, expected_value=name_on_main)

