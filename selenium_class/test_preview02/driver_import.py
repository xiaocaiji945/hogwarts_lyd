import pytest
from selenium import webdriver


class DrIm:
    @pytest.fixture()
    def open_url(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        yield
        self.driver.quit()
