from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CatalogPage(BasePage):
    URL = 'http://localhost:8081/2-home'
    PRICE_PRODUCT = (By.CSS_SELECTOR, '[aria-label="View product Hummingbird printed sweater"]~['
                                      'class="product-miniature__prices"]')
    CHAPTER_HOME_LINK = (By.CSS_SELECTOR, '[class="left-block__title-link"]')
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, '[class="btn btn-primary"]')
    BUTTON_CLOTHES = (By.CSS_SELECTOR, '[class="subcategory__link subcategory__link--with-image"]')
    COUNT_SUBSECTION = (By.CSS_SELECTOR, '[class="category-tree__list"]')
    FILTER_LIST = (By.CSS_SELECTOR, '[class="accordion-item"]')

    @allure.step('Переходим на страницу "Catalog"')
    def load_page(self):
        self.visit_page(self.URL)

    @allure.step("Проверяем что цена изменилась")
    def checking_change_price(self, price_euro):
        self.checking_text_element_not_equal(*self.PRICE_PRODUCT, expected_value=price_euro)

    @allure.step("Проверяем наименование кнопки 'Home'")
    def checking_name_button_home(self):
        self.checking_text_element(*self.CHAPTER_HOME_LINK, expected_value='Home')

    @allure.step("Проверяем наименование кнопки 'Clothes'")
    def checking_name_button_clothes(self):
        self.checking_text_element(*self.BUTTON_CLOTHES, expected_value='Clothes')

    @allure.step("Проверяем цвет кнопки 'Subscribe'")
    def checking_color_button_subscribe(self):
        self.checking_color_element(*self.BUTTON_SUBSCRIBE, expected_value='rgba(11, 105, 246, 1)')

    @allure.step("Проверяем количество подразделов")
    def checking_count_subsection(self):
        self.checking_count_element(*self.COUNT_SUBSECTION, expected_value=3)

    @allure.step("Проверяем количество элементов фильтрации")
    def checking_count_filter_list(self):
        self.checking_count_element(*self.FILTER_LIST, expected_value=11)
