from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.button_contact_us = browser.find_element(By.CSS_SELECTOR, "[class='ps-contactinfo__email']")
        self.button_mobile_menu = browser.find_element(By.CSS_SELECTOR, '[class="material-icons"]')
        self.button_sign_in = browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span')
        self.button_add_to_cart = browser.find_element(By.CSS_SELECTOR, "[class='product-miniature__add btn "
                                                                        "btn-primary btn-square-icon']")
        self.product_name = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article['
                                                           '3]/div/div[2]/div[1]/a')


class Catalog:
    def __init__(self, browser):
        self.browser = browser
        self.chapter_home = browser.find_element(By.CSS_SELECTOR, '[class="left-block__title-link"]')
        self.count_of_subsections = browser.find_elements(By.CSS_SELECTOR, '[class="category-tree__list"]')
        self.filter_list = browser.find_elements(By.XPATH, '//*[@id="search-filters"]/div/section')
        self.button_clothes = browser.find_element(By.CSS_SELECTOR, '[class="subcategory__link '
                                                                    'subcategory__link--with-image"]')
        self.button_subscribe = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')


class ProductCart:
    def __init__(self, browser):
        self.browser = browser
        self.button_add_to_cart = browser.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div['
                                                                 '2]/div[2]/button')
        self.price = browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div[2]/div[2]/div/div[1]/div')
        self.name_product = browser.find_element(By.CSS_SELECTOR, '[class="product__name h2 mb-1"]')
        self.share_elements = browser.find_elements(By.XPATH, "//*[@class='ps-sharebuttons__list']//li")


class SignIn:
    def __init__(self, browser):
        self.browser = browser
        self.name_page = browser.find_element(By.CSS_SELECTOR, '[class="page-title-section"]')
        self.sign_in_button = browser.find_element(By.ID, 'submit-login')
        self.button_create_account = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/a')
        self.button_forgot_password = browser.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/a')


class Register:
    def __init__(self, browser):
        self.browser = browser
        self.section_first_name = browser.find_element(By.XPATH, '//*[@id="customer-form"]/section/div[2]/label')
        self.button_create_account = browser.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button')
        self.sections_to_fill = browser.find_elements(By.XPATH, '//*[@id="customer-form"]/section/div')
        self.name_page = browser.find_element(By.CSS_SELECTOR, '[class="page-title-section"]')


class Cart:
    def __init__(self, browser):
        self.product_name_in_cart = browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div[1]/div['
                                                                   '2]/div/div/div/div/div[2]/div[1]/a')
        self.proceed_checkout_button = browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div['
                                                                      '2]/div/div[1]/div/div[3]/div/a')

