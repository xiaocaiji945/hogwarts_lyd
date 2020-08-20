from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.register_bage import RegisterPage


class LoginPage(BasePage):
    def login(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self._driver)