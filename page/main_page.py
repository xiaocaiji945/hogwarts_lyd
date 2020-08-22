from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    _go_contact_btn = (By.ID, 'menu_contacts')

    def go_to_contact_page(self):
        self.find(*self._go_contact_btn).click()
        return ContactPage(self._driver)
