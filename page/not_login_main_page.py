from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login_page import LoginPage
from page.register_bage import RegisterPage


class NotLoginMainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/'

    def goto_login(self):
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)

    def goto_register(self):
        self.find(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)
