from page_object_test.page.admin_sign_in_page import AdminSignInPage
from page_object_test.page.admin_catalog_page import AdminCatalogPage
from page_object_test.page.registration_page import RegistrationPage
from page_object_test.page.main_page import MainPage

EMAIL = 'admin@example.com'
PASSWORD = 'Admin123!'

social_title = 'm'
firstname = 'Bart'
lastname = 'Simpson'
email = 'ivanov_bolt171@mail.ru'
password = '123ivan456!'
birthday = '12/05/1993'


def test_create_account(browser):
    registration_page = RegistrationPage(browser)
    registration_page.load_page()
    registration_page.create_new_account(social_title, firstname, lastname, email, password, birthday)
    main_page = MainPage(browser)
    main_page.load_page()
    name_account = main_page.name_account()
    assert name_account == firstname + ' ' + lastname


def test_add_new_product_on_admin(browser):
    admin_sign_in_page = AdminSignInPage(browser)
    admin_sign_in_page.load_page()
    admin_sign_in_page.sign_in(EMAIL, PASSWORD)
    admin_catalog_page = AdminCatalogPage(browser)
    admin_catalog_page.load_page()
    admin_catalog_page.add_new_product('New_product', '25', '14')
    assert admin_catalog_page.get_status() == 'Successful update'


def test_delete_product_on_admin(browser):
    admin_sign_in_page = AdminSignInPage(browser)
    admin_sign_in_page.load_page()
    admin_sign_in_page.sign_in(EMAIL, PASSWORD)
    admin_catalog_page = AdminCatalogPage(browser)
    admin_catalog_page.load_page()
    admin_catalog_page.delete_product()
    assert admin_catalog_page.get_status() == 'Successful deletion'
