from selenium.webdriver.common.by import By
from page_object.additional_files.navigation import navigation_with_scroll, navigation_on_click
from page_object.additional_files.account import sign_in
from page_object.additional_files.page_object import MainPage, Cart


def test_sign_in(browser):
    url = 'http://localhost:8081/login?back=http%3A%2F%2Flocalhost%3A8081%2F'
    email = 'otus@mail.ru'
    password = '$%12zxopNM'
    if browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').get_property(
            'textContent').strip() == 'Sign in':
        sign_in(browser, url, email, password)
    else:
        browser.find_element(By.XPATH, '//*[@id="userMenuButton"]/span[2]').click()
        browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/div/a[6]').click()
        sign_in(browser, url, email, password)


def test_add_to_cart(browser):
    element = MainPage(browser)
    product_name_on_main = element.product_name.text.strip()
    navigation_with_scroll(browser, (By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[3]/div/div['
                                               '2]/div[2]/form/button'), (By.XPATH,
                                                                          '//*[@id="blockcart-modal"]/div/div/div[2]'))
    navigation_on_click(browser, (By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[3]/a'),
                        (By.XPATH, '//*[@id="center-column"]/div[1]/div[2]/div/div[1]/div/div[3]/div/a'))
    element_in_cart = Cart(browser)
    product_name_in_cart = element_in_cart.product_name_in_cart.text.strip()
    element_in_cart.proceed_checkout_button.is_enabled()
    assert product_name_on_main == product_name_in_cart


def test_change_price_on_main_page(browser):
    price_euro = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[2]/div/div['
                                                '2]/div[1]/div[1]/div[1]').text.strip()
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_currencyselector"]/div/select').click()
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_currencyselector"]/div/select/option[2]').click()
    price_dollar = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[2]/div/div['
                                                  '2]/div[1]/div[1]/div[1]').text.strip()
    assert price_dollar != price_euro


def test_change_price_in_catalog(browser):
    price_euro = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[2]/div/div['
                                                '2]/div[1]/div[1]/div[1]').text.strip()
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_currencyselector"]/div/select').click()
    browser.find_element(By.XPATH, '//*[@id="_desktop_ps_currencyselector"]/div/select/option[2]').click()
    navigation_with_scroll(browser, (By.XPATH, '//*[@id="content"]/section[3]/div/div[2]/a'),
                           (By.ID, "js-product-list-header"))
    price_dollar = browser.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/article[2]/div/div[2]/div['
                                                  '1]/div[1]/div[1]').text.strip()
    assert price_dollar != price_euro
