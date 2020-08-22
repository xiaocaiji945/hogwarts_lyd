from page.main_page import MainPage


class TestDepartment:
    def setup_class(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close_win()

    def test_add_department(self):
        result = self.main.go_to_contact_page().go_to_add_department_page().add_department(
            '这是第一个部门')._get_department_list()
        print(result)
        assert ' 这是第一个部门' in result
