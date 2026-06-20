from page_object_test.page.main_page import MainPage
from page_object_test.page.cart_page import CartPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage

EMAIL = 'otus@mail.ru'
PASSWORD = '$%12zxopNM'


def test_sign_in(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    sign_in_page.sign_in(EMAIL, PASSWORD)
    main_page = MainPage(browser)
    main_page.load_page()
    assert main_page.account_status() == 'Test Login'


def test_add_to_cart(browser):
    main_page = MainPage(browser)
    main_page.load_page()
    name_on_main = main_page.product_name_on_main_page()
    main_page.scroll_to_button_add_to_cart()
    main_page.add_to_cart()
    cart_page = CartPage(browser)
    cart_page.load_page()
    name_in_cart = cart_page.product_name_on_cart_page()
    assert name_on_main == name_in_cart


def test_change_price_on_main_page(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    price_dollar = main_page.price_product()
    assert price_dollar != price_euro


def test_change_price_in_catalog(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    price_dollar = catalog_page.price_product()
    assert price_dollar != price_euro
