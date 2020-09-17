from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # self._driver = ""
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
            # self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        self._driver.maximize_window()
        self._driver.implicitly_wait(3)

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(by, locator))
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def close_win(self):
        return self._driver.quit()

    @property
    def driver(self):
        return self._driver
