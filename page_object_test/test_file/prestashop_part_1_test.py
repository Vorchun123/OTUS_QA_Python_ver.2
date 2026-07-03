from page_object_test.page.main_page import MainPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage
from page_object_test.page.product_page import ProductPage
from page_object_test.page.registration_page import RegistrationPage
import allure


@allure.tag("functional")
@allure.title("Проверка элементов на главной странице")
def test_check_element_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.load_page()
    main_page.checking_name_button_contact_us()
    main_page.checking_name_button_sign_in()
    main_page.checking_color_button_add_to_cart()
    main_page.clickable_button_add_to_cart()
    main_page.visible_button_contact_us()


@allure.tag("functional")
@allure.title("Проверка элементов на странице 'Каталог'")
def test_check_element_in_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    catalog_page.checking_name_button_home()
    catalog_page.checking_count_subsection()
    catalog_page.checking_name_button_clothes()
    catalog_page.checking_count_filter_list()
    catalog_page.checking_color_button_subscribe()


@allure.tag("functional")
@allure.title("Проверка элементов на странице продукта")
def test_check_element_on_product_card(browser):
    product_page = ProductPage(browser)
    product_page.load_page()
    product_page.visible_button_add_to_cart()
    product_page.checking_color_button_add_to_cart()
    product_page.checking_price_product()
    product_page.checking_count_share_elements()
    product_page.checking_name_product()


@allure.tag("functional")
@allure.title("Проверка элементов на странице авторизации")
def test_check_element_on_sign_in(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    sign_in_page.checking_name_button_sign_in()
    sign_in_page.checking_color_button_sign_in()
    sign_in_page.clickable_button_sign_in()
    sign_in_page.checking_name_button_create_your_account()
    sign_in_page.visible_button_forgot_password()


@allure.tag("functional")
@allure.title("Проверка элементов на странице регистрации")
def test_check_element_on_page_of_register(browser):
    registration_page = RegistrationPage(browser)
    registration_page.load_page()
    registration_page.checking_name_button_create_account()
    registration_page.clickable_button_create_your_account()
    registration_page.checking_color_button_create_your_account()
    registration_page.checking_count_sections_to_filters()
    registration_page.checking_name_section_firstname()
