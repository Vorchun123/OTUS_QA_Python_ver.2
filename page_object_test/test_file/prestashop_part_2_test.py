from page_object_test.page.main_page import MainPage
from page_object_test.page.cart_page import CartPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage
import allure
import pytest


@allure.tag('smoke')
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тестирование входа в систему с разными валидными данными")
@pytest.mark.parametrize("email, password, firstname, lastname", [
    ('otus@mail.ru', '$%12zxopNM', 'Test', 'Login'),
    ('ivanov_bolt291@mail.ru', '123ivan456!', 'Born', 'Simpsonet'),
    ('ivanov_bolt171@mail.ru', '123ivan456!', 'Bart', 'Simpson')
])
def test_sign_in(browser, email, password, firstname, lastname):
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    sign_in_page.sign_in(email, password)
    sign_in_page.wait_sign_in()
    main_page = MainPage(browser)
    main_page.load_page()
    main_page.checking_name_user(firstname, lastname)


@allure.tag('regression')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавление продукта в корзину")
def test_add_to_cart(browser):
    main_page = MainPage(browser)
    main_page.load_page()
    name_on_main = main_page.product_name_on_main_page()
    main_page.scroll_to_button_add_to_cart()
    main_page.add_to_cart()
    main_page.wait_to_add()
    cart_page = CartPage(browser)
    cart_page.load_page()
    cart_page.checking_product_name_in_cart(name_on_main)


@allure.tag('functional')
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Изменение цены на главной странице")
def test_change_price_on_main_page(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    main_page.checking_change_currency(price_euro)


@allure.tag('functional')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Изменение цены на карточке продукта")
def test_change_price_in_catalog(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    catalog_page.checking_change_price(price_euro)
