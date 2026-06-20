from page_object_test.page.main_page import MainPage
from page_object_test.page.catalog_page import CatalogPage
from page_object_test.page.sign_in_page import SignInPage
from page_object_test.page.product_page import ProductPage
from page_object_test.page.registration_page import RegistrationPage


def test_check_element_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.load_page()
    assert main_page.name_button_contact_us() == 'Contact us'
    assert main_page.color_button_add_to_cart() == 'rgba(11, 105, 246, 1)'
    assert main_page.clickable_button_add_to_cart()
    assert main_page.name_button_sign_in() == 'Sign in'
    assert main_page.visible_button_contact_us()


def test_check_element_in_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.load_page()
    assert catalog_page.name_chapter_home() == 'Home'
    assert catalog_page.count_of_subsection() == 3
    assert catalog_page.name_button_clothes() == 'Clothes'
    assert catalog_page.count_of_element_in_filter_list() == 11
    assert catalog_page.color_button_subscribe() == 'rgba(11, 105, 246, 1)'


def test_check_element_on_product_card(browser):
    product_page = ProductPage(browser)
    product_page.load_page()
    assert product_page.visible_button_add_to_cart()
    assert product_page.color_button_add_to_cart() == 'rgba(11, 105, 246, 1)'
    assert product_page.price_product() == 'Price:\n€29.00'
    assert product_page.name_product() == "The best is yet to come' Framed poster"
    assert product_page.count_share_elements() == 3


def test_check_element_on_sign_in(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()
    assert sign_in_page.name_page() == 'Sign in'
    assert sign_in_page.color_button_sign_in() == 'rgba(11, 105, 246, 1)'
    assert sign_in_page.clickable_button_sign_in()
    assert sign_in_page.name_button_create_account() == 'Create your account'
    assert sign_in_page.visible_button_forgot_password()


def test_check_element_on_page_of_register(browser):
    registration_page = RegistrationPage(browser)
    registration_page.load_page()
    assert registration_page.name_page() == 'Create an account'
    assert registration_page.clickable_button_create_account()
    assert registration_page.color_button_create_account() == 'rgba(11, 105, 246, 1)'
    assert registration_page.count_section_to_filters() == 10
    assert registration_page.name_section() == 'First name'
