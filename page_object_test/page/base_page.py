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
        self.logger.info(f'{self.class_name}: Opening url: {url}')
        self.browser.get(url)

    def find_element(self, *locator):
        self.logger.info(f'{self.class_name}: Find element: {locator}')
        try:
            return self.browser.find_element(*locator)
        except Exception as e:
            self.logger.error(f'Error finding element: {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def find_elements(self, *locator):
        self.logger.info(f'{self.class_name}: Find elements: {locator}')
        return self.browser.find_elements(*locator)

    def click(self, *locator):
        self.logger.info(f'{self.class_name}: Click to element: {locator}')
        self.find_element(*locator).click()

    def send_keys(self, *locator, text):
        self.logger.info(f'{self.class_name}: Input field: {locator} , Input text: {text}')
        self.find_element(*locator).send_keys(text)

    def get_text(self, *locator):
        self.logger.info(f'{self.class_name}: Got text:{locator}')
        return self.find_element(*locator).text.strip()

    def get_color(self, *locator):
        self.logger.info(f'{self.class_name}: Got color: {locator}')
        return self.find_element(*locator).value_of_css_property('background-color')

    def element_is_clickable(self, *locator):
        self.logger.info(f'{self.class_name}: Check that the {locator} is clickable')
        return self.find_element(*locator).is_enabled()

    def element_is_visible(self, *locator):
        self.logger.info(f'{self.class_name}: Check that the {locator}is visible')
        return self.find_element(*locator).is_displayed()

    def scroll(self, *locator):
        self.logger.info(f'{self.class_name}: Scroll to the {locator}')
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element(*locator))

    def wait(self, timeout, locator):
        try:
            self.logger.info(f'{self.class_name} Wait for disappear {locator}')
            WebDriverWait(self.browser, timeout).until(
                EC.invisibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f'{self.class_name} Element {locator} is not found {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def wait_visible(self, timeout, locator):
        try:
            self.logger.info(f'{self.class_name} Wait for appear {locator}')
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f'{self.class_name} Element {locator} is not found {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def checking_text_element(self, *locator, expected_value):
        try:
            actual_value = self.get_text(*locator)
            self.logger.info(f'{self.class_name} Checking {locator} with {expected_value}')
            assert actual_value == expected_value, f'Expected value: {expected_value}, received value: {actual_value}'
        except Exception as e:
            self.logger.error(f'{self.class_name} Error getting text from element {locator} {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def checking_text_element_not_equal(self, *locator, expected_value):
        try:
            actual_value = self.get_text(*locator)
            self.logger.info(f'{self.class_name} Checking {locator} with {expected_value}')
            assert actual_value != expected_value, (f'Expected value: {expected_value}, received value: {actual_value}'
                                                    f' should not be equal')
        except Exception as e:
            self.logger.error(f'{self.class_name} Error getting text from element {locator} {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def checking_color_element(self, *locator, expected_value):
        try:
            actual_value = self.get_color(*locator)
            self.logger.info(f'{self.class_name} Checking {locator} with {expected_value}')
            assert actual_value == expected_value, f'Expected value: {expected_value}, received value: {actual_value}'
        except Exception as e:
            self.logger.error(f'{self.class_name} Error getting color from element {locator} {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise

    def checking_count_element(self, *locator, expected_value):
        try:
            actual_value = len(self.find_elements(*locator))
            self.logger.info(f'{self.class_name} Checking {locator} with {expected_value}')
            assert actual_value == expected_value, f'Expected value: {expected_value}, received value: {actual_value}'
        except Exception as e:
            self.logger.error(f'{self.class_name} Error getting color from element {locator} {e}')
            self.browser.save_screenshot(f"screenshot/{self.class_name}.png")
            screenshot = self.browser.get_screenshot_as_png()
            allure.attach(screenshot, f"{self.class_name}.png", allure.attachment_type.PNG)
            raise
