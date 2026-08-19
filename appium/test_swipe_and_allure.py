import time
import pytest
import allure
from appium.options.common import AppiumOptions
from appium.webdriver import webdriver
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "uiautomator2",
    "appium:app": "D:/Учеба/OTUS/Appium_файлы_примеров/pnv.apk"
})

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()


@allure.tag('functional')
@allure.title("Swipe to Calendar")
def test_swipe(driver):
    while True:
        with allure.step('Поиск элементов'):
            elements = driver.find_elements(AppiumBy.ID, 'com.csdroid.pkg:id/tv_title')
        with allure.step('Swipe 3-х элементов'):
            driver.swipe(elements[3].rect['x'], elements[3].rect['y'], elements[0].rect['x'], elements[0].rect['y'])
        elements = driver.find_elements(AppiumBy.ID, 'com.csdroid.pkg:id/tv_title')
        elements_name = [name.text for name in elements]
        with allure.step('Проверяем наличие Calendar на экране'):
            if 'Calendar' in elements_name:
                with allure.step('Нажимаем на Calendar'):
                    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                        value='new UiSelector().text("Calendar")').click()
                    time.sleep(2)
                    driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
                    break
            elif 'YouTube Music' in elements_name and 'Calendar' not in elements_name:
                raise Exception('Вы долестали до конца списка, но Calendar не нашли')
