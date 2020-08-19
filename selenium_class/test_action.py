'''
打开页面（http://sahitest.com/demo/clicks.htm）
分别对按钮'click me','dbl click me','right click me',执行点击、双击、右键操作
打印上面展示框中的内容
'''
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_action_case1(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        click_btn = self.driver.find_element_by_css_selector('[value="click me"]')
        dobule_c_btn = self.driver.find_element_by_css_selector('[value="dbl click me"]')
        right_c_bth = self.driver.find_element_by_css_selector('[value="right click me"]')
        text_value = self.driver.find_element_by_css_selector('[name="t2"]')
        self.action.click(click_btn)
        self.action.double_click(dobule_c_btn)
        self.action.context_click(right_c_bth)
        self.action.perform()
        result_text = text_value.get_attribute('value')
        print(f'\n********{result_text}*******')
        sleep(3)

    @pytest.mark.skip
    def test_action_move(self):
        self.driver.get('https://www.baidu.com/')
        settings_btn = self.driver.find_element_by_id('s-usersetting-top')
        self.action.move_to_element(settings_btn).perform()
        sleep(3)
    @pytest.mark.skip
    def test_action_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_css_selector('div[class="item"]:nth-child(4)')
        # self.action.drag_and_drop(drag_ele,drop_ele).perform()
        # self.action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        self.action.click_and_hold(drag_ele).release(drop_ele).perform()
        sleep(3)


    def test_action_keys(self):
        '''
        打开网址：http://sahitest.com/demo/label.htm
        定位两个输入框 e1,e2
        向输入框e1中输入文字"username"
        使用全选、复制、粘贴到输入框e2中
        '''
        self.driver.get('http://sahitest.com/demo/label.htm')
        e1 = self.driver.find_element_by_xpath('//input[@type="textbox"]')
        e2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        e1.click()
        self.action.send_keys('username').pause(1)
        self.action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        self.action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        self.action.perform()
        sleep(3)
        e2.click()
        self.action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL)
        self.action.send_keys(Keys.SPACE).pause(1)
        self.action.send_keys('tom')
        self.action.perform()
        sleep(3)