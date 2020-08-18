from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_link_text('开源项目').click()

        # sleep(3)
        # 方式 一
        # def wait(x):
        #     return len(self.driver.find_elements_by_link_text('Appium-style-guide')) >= 1
        # WebDriverWait(self.driver, 10).until(wait)

        # 方式 二

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(By.XPATH, '//*[@class="title raw-link raw-topic-link"]'))

        self.driver.find_element_by_link_text(('Appium-style-guide')).click()
