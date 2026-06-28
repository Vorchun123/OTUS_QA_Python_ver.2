from page_object_test.page.main_page import MainPage
from page_object_test.page.cart_page import CartPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage
import allure
import pytest


@allure.tag('smoke')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("email, password, firstname, lastname", [
    ('otus@mail.ru', '$%12zxopNM', 'Test', 'Login'),
    ('ivanov_bolt291@mail.ru', '123ivan456!', 'Born', 'Simpsonet'),
    ('ivanov_bolt171@mail.ru', '123ivan456!', 'Bart', 'Simpson')
])
def test_sign_in(browser, email, password, firstname, lastname):
    """Тест входа в систему"""
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    sign_in_page.sign_in(email, password)
    sign_in_page.wait_sign_in()
    main_page = MainPage(browser)
    main_page.load_page()
    assert main_page.name_account() == firstname + ' ' + lastname


@allure.tag('regression')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(browser):
    """Проверяем добавления продукта в корзину"""
    main_page = MainPage(browser)
    main_page.load_page()
    name_on_main = main_page.product_name_on_main_page()
    main_page.scroll_to_button_add_to_cart()
    main_page.add_to_cart()
    cart_page = CartPage(browser)
    cart_page.load_page()
    name_in_cart = cart_page.product_name_on_cart_page()
    assert name_on_main == name_in_cart


@allure.tag('functional')
@allure.severity(allure.severity_level.TRIVIAL)
@allure.description("Проверка изменения цены на главной странице")
def test_change_price_on_main_page(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    price_dollar = main_page.price_product()
    assert price_dollar != price_euro


@allure.tag('functional')
@allure.severity(allure.severity_level.MINOR)
@allure.description("Проверка изменения цены на карточке продукта")
def test_change_price_in_catalog(browser):
    main_page = MainPage(browser)
    price_euro = main_page.price_product()
    main_page.change_price('dollar')
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    price_dollar = catalog_page.price_product()
    assert price_dollar != price_euro
