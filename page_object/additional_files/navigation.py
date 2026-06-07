import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def navigation_with_scroll(browser, locator_element, locator_page_element):
    element = browser.find_element(*locator_element)
    browser.execute_script('arguments[0].scrollIntoView(true);', element)
    time.sleep(1)
    element.click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(locator_page_element))


def navigation_on_click(browser, locator_element, locator_page_element):
    browser.find_element(*locator_element).click()
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(locator_page_element))
