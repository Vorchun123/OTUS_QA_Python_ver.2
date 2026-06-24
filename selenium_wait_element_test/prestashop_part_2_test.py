import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_check_element_on_main_page(browser):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class ="logo img-fluid"]')))

    button_contact_us = browser.find_element(By.CSS_SELECTOR, "[class = 'ps-contactinfo__email']")
    button_mobile_menu = browser.find_element(By.CSS_SELECTOR, '[class = "material-icons"]')
    button_sign_in = browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span')
    button_add_to_cart = browser.find_element(By.CSS_SELECTOR,
                                              "[class ='product-miniature__add btn btn-primary btn-square-icon']")

    assert button_contact_us.get_property('textContent').strip() == 'Contact us', 'Name is not correct'
    assert button_add_to_cart.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"
    assert button_add_to_cart.is_enabled(), 'Button Add to cart is not clickable'
    assert button_mobile_menu.is_displayed(), "Button Mobile Menu is not displayed"
    assert button_sign_in.get_property('textContent').strip() == 'Sign in', "Button name is not correct"


def test_check_element_in_catalog(browser):
    all_product = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[2]/a')
    browser.execute_script("arguments[0].scrollIntoView(true);", all_product)
    time.sleep(1)
    all_product.click()
    (WebDriverWait(browser, 2).until
     (EC.visibility_of_element_located((By.ID, "js-product-list-header"))))
    chapter_home = browser.find_element(By.CSS_SELECTOR, '[class = "left-block__title-link"]')
    count_of_subsections = browser.find_elements(By.CSS_SELECTOR, '[class = "category-tree__list"]')
    filter_list = browser.find_elements(By.XPATH, '//*[@id="search-filters"]/div/section')
    button_clothes = browser.find_element(By.CSS_SELECTOR,
                                          '[class = "subcategory__link subcategory__link--with-image"]')
    button_subscribe = browser.find_element(By.CSS_SELECTOR, '[class = "btn btn-primary"]')

    assert chapter_home.get_property('textContent').strip() == 'Home', 'Chapter name is not correct'
    assert len(count_of_subsections) == 3, 'Count of subsections is not correct'
    assert button_clothes.get_property('textContent').strip() == 'Clothes'
    assert len(filter_list) == 11, 'Filter count is not correct'
    assert button_subscribe.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"


def test_check_element_on_product_card(browser):
    product_card = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[3]/div/div['
                                                  '1]/div/a')
    browser.execute_script('arguments[0].scrollIntoView(true);', product_card)
    time.sleep(1)
    product_card.click()
    (WebDriverWait(browser, 2).until
     (EC.visibility_of_element_located((By.CSS_SELECTOR, "[class = 'product__name h2 mb-1']"))))

    button_add_to_cart = browser.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div[2]/div[2]/button')
    price = browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div[2]/div[2]/div/div[1]/div')
    name_product = browser.find_element(By.CSS_SELECTOR, '[class = "product__name h2 mb-1"]')
    share_elements = browser.find_elements(By.XPATH, "//*[@class='ps-sharebuttons__list']//li")

    assert button_add_to_cart.is_enabled(), 'Button Add to cart is not clickable'
    assert button_add_to_cart.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"
    assert price.text.strip() == 'Price:\n€29.00', 'Price is not correct'
    assert name_product.text.strip() == "The best is yet to come' Framed poster", "Name product is not correct"
    assert len(share_elements) == 3, 'Count of share elements is not correct'


def test_check_element_on_sign_in(browser):
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').click()
    WebDriverWait(browser, 200).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button')))

    name_page = browser.find_element(By.CSS_SELECTOR, '[class = "page-title-section"]')
    sign_in_button = browser.find_element(By.ID, 'submit-login')
    button_create_account = browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/a')
    button_forgot_password = browser.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/a')

    assert name_page.text == 'Sign in', "Name of page is not correct"
    assert sign_in_button.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Sign in is not blue"
    assert sign_in_button.is_enabled(), 'Button Sign in is not clickable'
    assert button_create_account.get_property('textContent').strip() == 'Create your account', \
        "Name button 'Create your account' is not correct"
    assert button_forgot_password.is_displayed(), 'Button "Forgot your password" is not displayed '


def test_check_element_on_page_of_register(browser):
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').click()
    WebDriverWait(browser, 200).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button')))
    browser.find_element(By.XPATH, '//*[@id="content"]/div/div/div/a').click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[class = "page-title-section"]')))

    name_page = browser.find_element(By.CSS_SELECTOR, "[class ='page-title-section']")
    section_first_name = browser.find_element(By.XPATH, '//*[@id="customer-form"]/section/div[2]/label')
    button_create_account = browser.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button')
    sections_to_fill = browser.find_elements(By.XPATH, '//*[@id="customer-form"]/section/div')

    assert name_page.text.strip() == 'Create an account', "Name page is not correct"
    assert button_create_account.is_enabled(), "Button 'Create account' is not clickable"
    assert button_create_account.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button 'Create account' is not blue"
    assert len(sections_to_fill) == 10
    assert section_first_name.text.strip() == 'First name', "Name of section is not correct"
