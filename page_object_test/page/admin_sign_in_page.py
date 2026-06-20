from page_object_test.page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminSignInPage(BasePage):
    URL = 'http://localhost:8081/administration/login'
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    LOG_IN_BUTTON = (By.ID, 'submit_login')

    def load_page(self):
        self.browser.get(self.URL)

    def sign_in(self, email, password):
        self.send_keys(*self.EMAIL_INPUT, text=email)
        self.send_keys(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOG_IN_BUTTON)
        WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(self.LOG_IN_BUTTON))
