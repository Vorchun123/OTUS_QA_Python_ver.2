from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    BUTTON_AFTER = (By.CSS_SELECTOR, '[class="btn btn-link dropdown-toggle dropdown-toggle-dots dropdown-toggle-split no-rotate"]')
    BUTTON_DELETE = (By.CSS_SELECTOR, '[data-confirm-button-label="Delete"]')
    BUTTON_CONFIRM_DELETE = (By.CSS_SELECTOR, '.btn-confirm-submit')

    def load_page(self):
        self.browser.get(self.URL)
        self.click(*self.WARNING_BUTTON)

    def add_new_product(self, product_name, retail_price, wholesale_price):
        self.click(*self.ADD_PRODUCT_BUTTON)
        iframes = self.browser.find_elements(By.TAG_NAME, 'iframe')
        if iframes:
            self.browser.switch_to.frame(iframes[0])
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.STANDARD_PRODUCT_BUTTON))
        self.click(*self.STANDARD_PRODUCT_BUTTON)
        self.click(*self.ADD_NEW_PRODUCT_BUTTON)
        WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located(self.MODAL_WINDOWS_ADD_PRODUCT))
        self.send_keys(*self.PRODUCT_NAME_INPUT, text=product_name)
        self.click(*self.PRODUCT_PRICE_NAV_BUTTON)
        self.send_keys(*self.PRODUCT_RETAIL_PRICE_INPUT, text=retail_price)
        self.send_keys(*self.PRODUCT_COST_PRICE_INPUT, text=wholesale_price)
        self.click(*self.SAVE_BUTTON)

    def delete_product(self):
        self.click(*self.BUTTON_AFTER)
        self.click(*self.BUTTON_DELETE)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.MODAL_WINDOWS))
        self.click(*self.BUTTON_CONFIRM_DELETE)

    def get_status(self):
        return self.get_text(*self.STATUS)
