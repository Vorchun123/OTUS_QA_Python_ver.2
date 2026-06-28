from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def local_log(self, message):
        self.logger.info(f'{self.class_name}: {message}')

    def visit_page(self, url):
        self.logger.info('%s: Opening url: %s' % (self.class_name, url))
        self.browser.get(url)

    def find_element(self, *locator):
        self.logger.debug('%s: Find element: %s' % (self.class_name, locator))
        try:
            return self.browser.find_element(*locator)
        except Exception as e:
            self.logger.error(f'Error finding element: {e}')
            self.browser.save_screenshot(f"logs/screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def find_elements(self, *locator):
        self.logger.debug('%s: Find elements: %s' % (self.class_name, locator))
        return self.browser.find_elements(*locator)

    def click(self, *locator):
        self.logger.debug('%s: Click element: %s' % (self.class_name, locator))
        self.find_element(*locator).click()

    def send_keys(self, *locator, text):
        self.logger.info('%s: Input field: %s , Input text: %s' % (self.class_name, locator, text))
        self.find_element(*locator).send_keys(text)

    def get_text(self, *locator):
        self.logger.debug('%s: Get text: %s' % (self.class_name, locator))
        return self.find_element(*locator).text.strip()

    def get_color(self, *locator):
        self.logger.debug('%s: Get color: %s' % (self.class_name, locator))
        return self.find_element(*locator).value_of_css_property('background-color')

    def element_is_clickable(self, *locator):
        self.logger.debug('%s: Check that the element is clickable: %s' % (self.class_name, locator))
        return self.find_element(*locator).is_enabled()

    def element_is_visible(self, *locator):
        self.logger.debug('%s: Check that the element is visible: %s' % (self.class_name, locator))
        return self.find_element(*locator).is_displayed()

    def scroll(self, *locator):
        self.logger.debug('%s: Scroll to the element: %s' % (self.class_name, locator))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element(*locator))

    def wait(self, timeout, locator):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f'%s Element %s is not found {e}' % (self.class_name, locator))
            self.browser.save_screenshot(f"logs/screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def wait_visible(self, timeout, locator):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f'%s Element %s is not found {e}' % (self.class_name, locator))
            self.browser.save_screenshot(f"logs/screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise
