from selenium.webdriver.common.by import By

from page.base_page import BasePage


class RegisterPage(BasePage):
    def register(self):
        self.find(By.ID, 'corp_name').send_keys('这是一个企业名称')
        self.find(By.ID, 'manager_name').send_keys('管理员名称')
        return True
