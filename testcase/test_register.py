from page.main_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close_win()

    # def test_register(self):
    #     assert self.main.goto_register().register()

    def test_register02(self):
        assert self.main.goto_login().goto_register().register()
