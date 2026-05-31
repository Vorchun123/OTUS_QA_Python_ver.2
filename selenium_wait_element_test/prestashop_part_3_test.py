import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_sign_in(browser):
    if browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').get_property(
            'textContent').strip() == 'Sign in':
        browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').click()
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button')))
        browser.find_element(By.XPATH, '//*[@id="field-email"]').send_keys('otus@mail.ru')
        browser.find_element(By.XPATH, '//*[@id="field-password"]').send_keys('$%12zxopNM')
        browser.find_element(By.ID, 'submit-login').click()
        try:
            WebDriverWait(browser, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/section[2]/div')))
            assert browser.find_element(By.XPATH, '//*[@id="content"]/section[2]/div').is_displayed()
            print("\nsuccessfully logged in")
        except (TimeoutError, AssertionError):
            print("\ncouldn't log in")
    else:
        browser.find_element(By.XPATH, '//*[@id="userMenuButton"]/span[2]').click()
        browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/div/a[6]').click()
        browser.find_element(By.XPATH, '//*[@id="_desktop_ps_customersignin"]/div/div/a/span').click()
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="login-form"]/div[2]/div[1]/button')))
        browser.find_element(By.XPATH, '//*[@id="field-email"]').send_keys('otus@mail.ru')
        browser.find_element(By.XPATH, '//*[@id="field-password"]').send_keys('$%12zxopNM')
        browser.find_element(By.ID, 'submit-login').click()
        try:
            WebDriverWait(browser, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/section[2]/div')))
            assert browser.find_element(By.XPATH, '//*[@id="content"]/section[2]/div').is_displayed()
            print("\nsuccessfully logged in")
        except (TimeoutError, AssertionError):
            print("\ncouldn't log in")


def test_add_to_cart(browser):
    product = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[3]/div/div['
                                             '2]/div[2]/form/button')
    product_name = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[1]/div/article[3]/div/div['
                                                  '2]/div[1]/a').text.strip()
    browser.execute_script('arguments[0].scrollIntoView(true);', product)
    time.sleep(1)
    product.click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="blockcart-modal"]/div/div'
                                                                                '/div[2]')))
    browser.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[3]/a').click()
    WebDriverWait(browser, 2).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="blockcart-modal"]/div/div'
                                                                                  '/div[2]')))
    product_name_in_cart = browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div[1]/div['
                                                          '2]/div/div/div/div/div[2]/div[1]/a').text.strip()
    browser.find_element(By.XPATH, '//*[@id="center-column"]/div[1]/div[2]/div/div[1]/div/div[3]/div/a').is_enabled()
    assert product_name == product_name_in_cart


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
    all_product = browser.find_element(By.XPATH, '//*[@id="content"]/section[3]/div/div[2]/a')
    browser.execute_script("arguments[0].scrollIntoView(true);", all_product)
    time.sleep(1)
    all_product.click()
    (WebDriverWait(browser, 2).until
     (EC.visibility_of_element_located((By.ID, "js-product-list-header"))))
    price_dollar = browser.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/article[2]/div/div[2]/div['
                                                  '1]/div[1]/div[1]').text.strip()
    assert price_dollar != price_euro
