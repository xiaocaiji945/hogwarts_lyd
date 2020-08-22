from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    _department_name_input = (By.CSS_SELECTOR, '.member_tag_dialog_inputDlg [name=name]')
    _exist_in_department_click = (By.CSS_SELECTOR, '.js_parent_party_name')
    # _first_department_btn = (By.CSS_SELECTOR, '.member_tag_dialog_inputDlg [id=1688853096647541_anchor]')
    _first_department_btn = (By.XPATH, '//*[@id="__dialog__MNDialog__"]//*[contains(text(), "晟源综合商店")]')
    _submit_btn = (By.CSS_SELECTOR, '#__dialog__MNDialog__ [d_ck=submit]')

    def add_department(self, name):
        self.find(*self._department_name_input).send_keys(name)
        self.find(*self._exist_in_department_click).click()

        self.find(*self._first_department_btn).click()
        self.find(*self._submit_btn).click()

        return ContactPage(self._driver)
