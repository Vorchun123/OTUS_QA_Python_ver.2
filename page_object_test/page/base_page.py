class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def send_keys(self, *locator, text):
        self.find_element(*locator).send_keys(text)

    def get_text(self, *locator):
        return self.find_element(*locator).text.strip()

    def get_color(self, *locator):
        return self.find_element(*locator).value_of_css_property('background-color')

    def element_is_clickable(self, *locator):
        return self.find_element(*locator).is_enabled()

    def element_is_visible(self, *locator):
        return self.find_element(*locator).is_displayed()

    def scroll(self, *locator):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element(*locator))
