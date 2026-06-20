from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    URL = 'http://localhost:8081/2-home'
    PRICE_PRODUCT = (By.CSS_SELECTOR, '[aria-label="View product Hummingbird printed sweater"]~['
                                      'class="product-miniature__prices"]')
    CHAPTER_HOME_LINK = (By.CSS_SELECTOR, '[class="left-block__title-link"]')
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, '[class="btn btn-primary"]')
    BUTTON_CLOTHES = (By.CSS_SELECTOR, '[class="subcategory__link subcategory__link--with-image"]')
    COUNT_SUBSECTION = (By.CSS_SELECTOR, '[class="category-tree__list"]')
    FILTER_LIST = (By.CSS_SELECTOR, '[class="accordion-item"]')

    def load_page(self):
        self.browser.get(self.URL)

    def price_product(self):
        return self.get_text(*self.PRICE_PRODUCT)

    def name_chapter_home(self):
        return self.get_text(*self.CHAPTER_HOME_LINK)

    def name_button_clothes(self):
        return self.get_text(*self.BUTTON_CLOTHES)

    def color_button_subscribe(self):
        return self.get_color(*self.BUTTON_SUBSCRIBE)

    def count_of_subsection(self):
        return len(self.find_elements(*self.COUNT_SUBSECTION))

    def count_of_element_in_filter_list(self):
        return len(self.find_elements(*self.FILTER_LIST))
