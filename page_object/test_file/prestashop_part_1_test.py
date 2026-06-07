from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_object.additional_files.navigation import navigation_with_scroll, navigation_on_click
from page_object.additional_files.page_object import MainPage, SignIn, Catalog, ProductCart, Register


def test_check_element_on_main_page(browser):
    element = MainPage(browser)
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class ="logo img-fluid"]')))
    assert element.button_contact_us.get_property('textContent').strip() == 'Contact us', 'Name is not correct'
    assert element.button_add_to_cart.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"
    assert element.button_add_to_cart.is_enabled(), 'Button Add to cart is not clickable'
    assert element.button_mobile_menu.is_displayed(), "Button Mobile Menu is not displayed"
    assert element.button_sign_in.get_property('textContent').strip() == 'Sign in', "Button name is not correct"


def test_check_element_in_catalog(browser):
    navigation_with_scroll(browser, (By.XPATH, '//*[@id="content"]/section[3]/div/div[2]/a'),
                           (By.ID, "js-product-list-header"))
    element = Catalog(browser)
    assert element.chapter_home.get_property('textContent').strip() == 'Home', 'Chapter name is not correct'
    assert len(element.count_of_subsections) == 3, 'Count of subsections is not correct'
    assert element.button_clothes.get_property('textContent').strip() == 'Clothes'
    assert len(element.filter_list) == 11, 'Filter count is not correct'
    assert element.button_subscribe.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"


def test_check_element_on_product_card(browser):
    navigation_with_scroll(browser, (By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[3]/div/div['
                                               '1]/div/a'), (By.CSS_SELECTOR, "[class = 'product__name h2 mb-1']"))
    element = ProductCart(browser)
    assert element.button_add_to_cart.is_enabled(), 'Button Add to cart is not clickable'
    assert element.button_add_to_cart.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Add to cart is not blue"
    assert element.price.text.strip() == 'Price:\n€29.00', 'Price is not correct'
    assert element.name_product.text.strip() == "The best is yet to come' Framed poster", "Name product is not correct"
    assert len(element.share_elements) == 3, 'Count of share elements is not correct'


def test_check_element_on_sign_in(browser):
    navigation_on_click(browser, (By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span'),
                        (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button'))
    element = SignIn(browser)
    assert element.name_page.text == 'Sign in', "Name of page is not correct"
    assert element.sign_in_button.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button Sign in is not blue"
    assert element.sign_in_button.is_enabled(), 'Button Sign in is not clickable'
    assert element.button_create_account.get_property('textContent').strip() == 'Create your account', \
        "Name button 'Create your account' is not correct"
    assert element.button_forgot_password.is_displayed(), 'Button "Forgot your password" is not displayed '


def test_check_element_on_page_of_register(browser):
    navigation_on_click(browser, (By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span'),
                        (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button'))
    navigation_on_click(browser, (By.XPATH, '//*[@id="content"]/div/div/div/a'),
                        (By.CSS_SELECTOR, '[class = "page-title-section"]'))
    element = Register(browser)
    assert element.name_page.text.strip() == 'Create an account', "Name page is not correct"
    assert element.button_create_account.is_enabled(), "Button 'Create account' is not clickable"
    assert element.button_create_account.value_of_css_property('background-color') == 'rgba(11, 105, 246, 1)', \
        "Button 'Create account' is not blue"
    assert len(element.sections_to_fill) == 10
    assert element.section_first_name.text.strip() == 'First name', "Name of section is not correct"
