from selenium import webdriver
from selenium.webdriver.common.by import By

'''
打开Chrome
打开URL：https://www.baidu.com/
向输入框中输入'selenium测试'
通过TouchAction点击搜索框
滑动到底部，点击下一页
关闭Chrome
'''


class TestTouch():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        self.touch = webdriver.TouchActions(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_touch_demo1(self):
        self.driver.get('https://www.baidu.com/')
        search_input = self.driver.find_element(By.ID, 'kw')
        search_btn = self.driver.find_element(By.ID, 'su')
        search_input.send_keys('selenium测试')
        self.touch.tap(search_btn).perform()
        self.touch.scroll_from_element(search_input, 0, 10000).perform()
