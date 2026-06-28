from page_object_test.page.admin_sign_in_page import AdminSignInPage
from page_object_test.page.admin_catalog_page import AdminCatalogPage
from page_object_test.page.registration_page import RegistrationPage
from page_object_test.page.main_page import MainPage
import allure

EMAIL = 'admin@example.com'
PASSWORD = 'Admin123!'

social_title = 'm'
firstname = 'Born'
lastname = 'Simpsonet'
email = 'ivanov_bolt291@mail.ru'
password = '123ivan456!'
birthday = '12/05/1993'


@allure.feature("Управление пользователем")
@allure.story("Создание нового пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account(browser):
    """Создание новой учетной записи"""
    registration_page = RegistrationPage(browser)
    registration_page.load_page()
    with allure.step("Ввод пользовательских данных"):
        registration_page.create_new_account(social_title, firstname, lastname, email, password, birthday)
    main_page = MainPage(browser)
    main_page.load_page()
    name_account = main_page.name_account()
    with allure.step("Проверяем что новый пользователь создан"):
        assert name_account == firstname + ' ' + lastname


@allure.feature("Управление продуктом")
@allure.story("Создание нового продукта")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_product_on_admin(browser):
    admin_sign_in_page = AdminSignInPage(browser)
    admin_sign_in_page.load_page()
    with allure.step("Авторизуемся в системе"):
        admin_sign_in_page.sign_in(EMAIL, PASSWORD)
    admin_catalog_page = AdminCatalogPage(browser)
    admin_catalog_page.load_page()
    with allure.step("Вводим данные продукта"):
        admin_catalog_page.add_new_product('New_product', '25', '14')
    with allure.step("Проверяем что продукт успешно создан"):
        assert admin_catalog_page.get_status() == 'Successful update'


@allure.feature("Управление продуктом")
@allure.story("Удаление продукта")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_product_on_admin(browser):
    admin_sign_in_page = AdminSignInPage(browser)
    admin_sign_in_page.load_page()
    with allure.step("Авторизуемся в системе"):
        admin_sign_in_page.sign_in(EMAIL, PASSWORD)
    admin_catalog_page = AdminCatalogPage(browser)
    admin_catalog_page.load_page()
    with allure.step("Удаляем продукт"):
        admin_catalog_page.delete_product()
    with allure.step("Проверяем что продукт успешно удален"):
        assert admin_catalog_page.get_status() == 'Successful deletion'
