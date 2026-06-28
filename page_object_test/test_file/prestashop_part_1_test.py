from page_object_test.page.main_page import MainPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage
from page_object_test.page.product_page import ProductPage
from page_object_test.page.registration_page import RegistrationPage
import allure


@allure.tag("functional")
def test_check_element_on_main_page(browser):
    """Тестирование элементов на главной странице"""
    main_page = MainPage(browser)
    main_page.load_page()
    with allure.step("Проверяем наименование кнопки 'Contact us'"):
        assert main_page.name_button_contact_us() == 'Contact us'
    with allure.step("Проверяем цвет кнопки 'Add to cart'"):
        assert main_page.color_button_add_to_cart() == 'rgba(11, 105, 246, 1)'
    with allure.step("Проверяем кликабельность кнопки 'Add to cart'"):
        assert main_page.clickable_button_add_to_cart()
    with allure.step("Проверяем наименование кнопки 'Sign in'"):
        assert main_page.name_button_sign_in() == 'Sign in'
    with allure.step("Проверяем видимость кнопки 'Contact us'"):
        assert main_page.visible_button_contact_us()


@allure.tag("functional")
def test_check_element_in_catalog(browser):
    """Тестирование элементов на странице 'Каталог'"""
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    with allure.step("Проверяем наименование кнопки 'Home'"):
        assert catalog_page.name_chapter_home() == 'Home'
    with allure.step("Проверяем количество подразделов"):
        assert catalog_page.count_of_subsection() == 3
    with allure.step("Проверяем наименование кнопки 'Clothes'"):
        assert catalog_page.name_button_clothes() == 'Clothes'
    with allure.step("Проверяем количество элементов фильтрации"):
        assert catalog_page.count_of_element_in_filter_list() == 11
    with allure.step("Проверяем цвет кнопки 'Subscribe'"):
        assert catalog_page.color_button_subscribe() == 'rgba(11, 105, 246, 1)'


@allure.tag("functional")
def test_check_element_on_product_card(browser):
    """Тестирование элементов на странице продукта"""
    product_page = ProductPage(browser)
    product_page.load_page()
    with allure.step("Проверяем видимость кнопки 'Add to cart'"):
        assert product_page.visible_button_add_to_cart()
    with allure.step("Проверяем цвет кнопки 'Add to cart'"):
        assert product_page.color_button_add_to_cart() == 'rgba(11, 105, 246, 1)'
    with allure.step("Проверяем стоимость продукта'"):
        assert product_page.price_product() == 'Price:\n€29.00'
    with allure.step("Проверяем наименование продукта'"):
        assert product_page.name_product() == "The best is yet to come' Framed poster"
    with allure.step("Проверяем количество элементов чтобы поделиться"):
        assert product_page.count_share_elements() == 3


@allure.tag("functional")
def test_check_element_on_sign_in(browser):
    """Тестирование элементов на странице авторизации"""
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    with allure.step("Проверяем наименование кнопки 'Sign in'"):
        assert sign_in_page.name_page() == 'Sign in'
    with allure.step("Проверяем цвет кнопки 'Sign in'"):
        assert sign_in_page.color_button_sign_in() == 'rgba(11, 105, 246, 1)'
    with allure.step("Проверяем кликабельность кнопки 'Sign in'"):
        assert sign_in_page.clickable_button_sign_in()
    with allure.step("Проверяем наименование кнопки 'Create your account'"):
        assert sign_in_page.name_button_create_account() == 'Create your account'
    with allure.step("Проверяем видимость кнопки 'Forgot password'"):
        assert sign_in_page.visible_button_forgot_password()


@allure.tag("functional")
def test_check_element_on_page_of_register(browser):
    """Тестирование элементов на странице регистрации"""
    registration_page = RegistrationPage(browser)
    registration_page.load_page()
    with allure.step("Проверяем наименование кнопки 'Create your account'"):
        assert registration_page.name_page() == 'Create an account'
    with allure.step("Проверяем кликабельность кнопки 'Create an account'"):
        assert registration_page.clickable_button_create_account()
    with allure.step("Проверяем цвет кнопки 'Create your account'"):
        assert registration_page.color_button_create_account() == 'rgba(11, 105, 246, 1)'
    with allure.step("Проверяем количество секций фильтрации"):
        assert registration_page.count_section_to_filters() == 10
    with allure.step("Проверяем наименование секции 'First name'"):
        assert registration_page.name_section() == 'First name'
