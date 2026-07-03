from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminCatalogPage(BasePage):
    URL = 'http://localhost:8081/administration/sell/catalog/products/'
    WARNING_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-outline-danger mr-3"]')
    ADD_PRODUCT_BUTTON = (By.ID, 'page-header-desc-configuration-add')
    STANDARD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button.product-type-choice[data-value="standard"]')
    ADD_NEW_PRODUCT_BUTTON = (By.ID, 'create_product_create')
    PRODUCT_NAME_INPUT = (By.ID, 'product_header_name_1')
    PRODUCT_PRICE_NAV_BUTTON = (By.ID, 'product_pricing-tab-nav')
    PRODUCT_RETAIL_PRICE_INPUT = (By.ID, 'product_pricing_retail_price_price_tax_excluded')
    PRODUCT_COST_PRICE_INPUT = (By.ID, 'product_pricing_wholesale_price')
    SAVE_BUTTON = (By.ID, 'product_footer_save')
    MODAL_WINDOWS_ADD_PRODUCT = (By.ID, 'create_product')
    MODAL_WINDOWS = (By.ID, 'product-grid-confirm-modal')
    STATUS = (By.CSS_SELECTOR, '[class="alert-text"]')
    BUTTON_AFTER = (By.CSS_SELECTOR, '[class="btn btn-link dropdown-toggle dropdown-toggle-dots dropdown-toggle-split '
                                     'no-rotate"]')
    BUTTON_DELETE = (By.CSS_SELECTOR, '[data-confirm-button-label="Delete"]')
    BUTTON_CONFIRM_DELETE = (By.CSS_SELECTOR, '.btn-confirm-submit')

    @allure.step('Переходим на страницу "Admin-Catalog"')
    def load_page(self):
        self.visit_page(self.URL)
        self.click(*self.WARNING_BUTTON)

    @allure.step("Вводим данные продукта")
    def add_new_product(self, product_name, retail_price, wholesale_price):
        self.click(*self.ADD_PRODUCT_BUTTON)
        iframes = self.browser.find_elements(By.TAG_NAME, 'iframe')
        if iframes:
            self.browser.switch_to.frame(iframes[0])
        self.wait_visible(10, self.STANDARD_PRODUCT_BUTTON)
        self.click(*self.STANDARD_PRODUCT_BUTTON)
        self.click(*self.ADD_NEW_PRODUCT_BUTTON)
        self.wait(10, self.MODAL_WINDOWS_ADD_PRODUCT)
        with allure.step("Вводим наименование продукта"):
            self.send_keys(*self.PRODUCT_NAME_INPUT, text=product_name)
        self.click(*self.PRODUCT_PRICE_NAV_BUTTON)
        with allure.step("Вводим розничную цену продукта"):
            self.send_keys(*self.PRODUCT_RETAIL_PRICE_INPUT, text=retail_price)
        with allure.step("Вводим себестоимость продукта"):
            self.send_keys(*self.PRODUCT_COST_PRICE_INPUT, text=wholesale_price)
        self.click(*self.SAVE_BUTTON)

    @allure.step("Удаляем продукт")
    def delete_product(self):
        self.click(*self.BUTTON_AFTER)
        self.click(*self.BUTTON_DELETE)
        self.wait_visible(10, self.MODAL_WINDOWS)
        self.click(*self.BUTTON_CONFIRM_DELETE)

    @allure.step("Проверяем что продукт успешно создан")
    def get_successful_update_status(self):
        self.checking_text_element(*self.STATUS, expected_value='Successful update')

    @allure.step("Проверяем что продукт успешно удален")
    def get_successful_deletion_status(self):
        self.checking_text_element(*self.STATUS, expected_value='Successful deletion')

