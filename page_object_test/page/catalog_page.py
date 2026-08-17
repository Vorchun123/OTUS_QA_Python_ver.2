from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CatalogPage(BasePage):
    URL = 'http://192.168.10.247:8081/2-home'
    PRICE_PRODUCT = (By.XPATH, '//*[@id="js-product-list"]/div[1]/div[6]/article/div/div[2]/div[1]/span')
    CHAPTER_HOME_LINK = (By.XPATH, '//*[@id="left-column"]/div[1]/ul/li[1]/a')
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, '[class="btn btn-primary"]')
    BUTTON_CLOTHES = (By.XPATH, '//*[@id="category-3"]/a')
    COUNT_SUBCATEGORIES = (By.CSS_SELECTOR, '#subcategories > ul > li')
    FILTER_LIST = (By.CSS_SELECTOR, '#search_filters > section')

    @allure.step('Переходим на страницу "Catalog"')
    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем что цена изменилась")
    def checking_change_price(self, price_euro):
        self.checking_text_element_not_equal(*self.PRICE_PRODUCT, expected_value=price_euro)

    @allure.step("Проверяем наименование кнопки 'Home'")
    def checking_name_button_home(self):
        self.checking_text_element(*self.CHAPTER_HOME_LINK, expected_value='HOME')

    @allure.step("Проверяем наименование кнопки 'Clothes'")
    def checking_name_button_clothes(self):
        self.checking_text_element(*self.BUTTON_CLOTHES, expected_value='CLOTHES')

    @allure.step("Проверяем цвет кнопки 'Subscribe'")
    def checking_color_button_subscribe(self):
        self.checking_color_element(*self.BUTTON_SUBSCRIBE, expected_value='rgba(36, 185, 215, 1)')

    @allure.step("Проверяем количество подразделов")
    def checking_count_subcategories(self):
        self.checking_count_element(*self.COUNT_SUBCATEGORIES, expected_value=3)

    @allure.step("Проверяем количество элементов фильтрации")
    def checking_count_filter_list(self):
        self.checking_count_element(*self.FILTER_LIST, expected_value=11)
