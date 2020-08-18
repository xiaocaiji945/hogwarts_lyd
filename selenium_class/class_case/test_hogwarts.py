from selenium import webdriver
from time import sleep


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[4]/a').click()
        self.driver.find_element_by_link_text('君海游戏QA').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/a')
