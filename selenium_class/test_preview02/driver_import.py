import os
import pytest
from selenium import webdriver


class DrIm:
    @pytest.fixture()
    def open_url(self):
        # 多浏览器处理
        browser = os.getenv("brower")
        if browser == 'firefox':
            self.driver = webdriver.Firefox=()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()

    # def setup(self):
    #     # # 多浏览器处理
    #     browser = os.getenv("brower")
    #     if browser == 'firefox':
    #         self.driver = webdriver.Firefox = ()
    #     elif browser == 'headless':
    #         self.driver = webdriver.PhantomJS()
    #     else:
    #         self.driver = webdriver.Chrome()
    #
    #     # self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    # def teardown(self):
    #     self.driver.quit()
