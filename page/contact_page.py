from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ContactPage(BasePage):
    _left_add_btn = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _add_department_btn = (By.CSS_SELECTOR, '.js_create_party')
    # _department_list_value = (By.CSS_SELECTOR, '.jstree-anchor')
    # _department_list_value = (By.CSS_SELECTOR, '.jstree-children > li')
    _department_list_value = (By.CSS_SELECTOR, '.jstree-children > li:nth-child(3)')

    def go_to_add_department_page(self):
        from page.add_department_page import AddDepartmentPage

        self.find(*self._left_add_btn).click()
        self.find(*self._add_department_btn).click()

        return AddDepartmentPage(self._driver)

    def _get_department_list(self):
        department_list = self.finds(*self._department_list_value)
        new_department_list = []
        for department in department_list:
            new_department_list.append(department.text)

        return new_department_list
