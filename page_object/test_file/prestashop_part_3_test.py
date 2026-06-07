from page_object.additional_files.account import sign_in
from page_object.additional_files.account import create_new_account
from page_object.additional_files.navigation import navigation_with_scroll
from selenium.webdriver.common.by import By


def test_create_account(browser):
    social_title = 'm'
    firstname = 'Ivan'
    lastname = 'Ivanov'
    email = 'ivanov_bolt131@mail.ru'
    password = '123ivan456!'
    bithday = '12/05/1993'
    navigation_with_scroll(browser, (By.XPATH, '//*[@id="footer_customeraccountlinks"]/ul/li[3]/a'),
                           (By.XPATH, '//*[@id="center-column"]/div/h1'))
    create_new_account(browser, social_title, firstname, lastname, email, password, bithday)


def test_add_new_product_on_admin(browser):
    url = 'http://localhost:8081/administration/login'
    email = 'admin@example.com'
    password = 'Admin123!'
    sign_in(browser, url, email, password)
    browser.get('http://localhost:8081/administration/sell/catalog/products/?_token=d59a87df9dd4484222359'
                '.tGanVXSPYhDyPeCNMApPw7xlmNrtSMwGxzqrMFeCo9o.9yDtMUPGFkO5dLLfdH1'
                '-qekk7IOMEaRprlDldyDDlrjaMcA4OsYLSMAO0A')
    browser.find_element(By.ID, 'page-header-desc-configuration-add').click()
    browser.find_element(By.XPATH, '//*[@id="create_product"]/div[1]/div[1]/button[1]').click()
    browser.find_element(By.ID, 'create_product_create').click()
    browser.find_element(By.ID, 'id="product_header_name_1"').send_keys('New_product')
    browser.find_element(By.ID, 'product_pricing-tab-nav').click()
    browser.find_element(By.ID, 'product_pricing_retail_price_price_tax_excluded').send_keys('25')
    browser.find_element(By.ID, 'product_pricing_wholesale_price').send_keys('14')
    browser.find_element(By.ID, 'product_footer_save').click()
    assert (browser.find_element(By.XPATH, '//*[@id="main-div"]/div/div[3]/form/div[3]/div').get_property('textContent')
            == 'Successful update')


def test_delete_product_on_admin(browser):
    url = 'http://localhost:8081/administration/login'
    email = 'admin@example.com'
    password = 'Admin123!'
    sign_in(browser, url, email, password)
    browser.get('http://localhost:8081/administration/sell/catalog/products/?_token=d59a87df9dd4484222359'
                '.tGanVXSPYhDyPeCNMApPw7xlmNrtSMwGxzqrMFeCo9o.9yDtMUPGFkO5dLLfdH1'
                '-qekk7IOMEaRprlDldyDDlrjaMcA4OsYLSMAO0A')
    browser.find_element(By.XPATH, '//*[@id="product_grid_table"]/tbody/tr[1]/td[11]/div/div/a[2]').click()
    browser.find_element(By.XPATH, '//*[@id="product_grid_table"]/tbody/tr[1]/td[11]/div/div/div/a[3]').click()
    browser.find_element(By.XPATH, '//*[@id="product-grid-confirm-modal"]/div/div/div[3]/button[2]').click()
    assert (browser.find_element(By.XPATH, '//*[@id="main-div"]/div/div[3]/form/div[3]/div').get_property('textContent')
            == 'Successful deletion')
