from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def sign_in(browser, url, email, password):
    browser.get(url)
    if url != 'http://localhost:8081/administration/login':
        browser.find_element(By.XPATH, '//*[@id="field-email"]').send_keys(email)
        browser.find_element(By.XPATH, '//*[@id="field-password"]').send_keys(password)
        browser.find_element(By.ID, 'submit-login').click()
        WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.ID, 'submit-login')))
    else:
        browser.find_element(By.ID, 'email').send_keys(email)
        browser.find_element(By.ID, 'passwd').send_keys(password)
        browser.find_element(By.ID, 'submit_login').click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'page-header-desc-configuration'
                                                                                  '-back')))


def create_new_account(browser, social_title, firstname, lastname, email, password, birthday):
    if social_title == 'm':
        browser.find_element(By.ID, 'field-id_gender_1').click()
    else:
        browser.find_element(By.ID, 'field-id_gender_2').click()
    browser.find_element(By.ID, 'field-firstname').send_keys(firstname)
    browser.find_element(By.ID, 'field-lastname').send_keys(lastname)
    browser.find_element(By.ID, 'field-email').send_keys(email)
    browser.find_element(By.ID, 'field-password').send_keys(password)
    browser.find_element(By.ID, 'field-birthday').send_keys(birthday)
    psgdpr = browser.find_element(By.ID, 'field-psgdpr')
    browser.execute_script('arguments[0].scrollIntoView(true);', psgdpr)
    time.sleep(1)
    psgdpr.click()
    browser.find_element(By.ID, 'field-customer_privacy').click()
    browser.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button').click()
    WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="wrapper"]/nav/div/ol')))
    name_account = browser.find_element(By.XPATH, '//*[@id="userMenuButton"]/span[2]').get_property(
        'textContent').strip()
    assert name_account == firstname + ' ' + lastname
