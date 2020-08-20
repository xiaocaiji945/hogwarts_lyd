import sys
from time import sleep
import sys

sys.path.append('..')
sys.path.append('..')
# from selenium_class.test_preview02.driver_import import DrIm
from selenium_class.test_preview02.driver_import import DrIm

'''
打开百度页面
点击登录
弹窗点击'立即注册'，输入用户名和帐号
返回刚才的登录页，点击登录
输入用户名密码，点击登录
'''


class TestWin(DrIm):
    def test_win01(self, open_url):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_link_text('登录').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        windows = self.driver.window_handles
        sleep(2)

        self.driver.switch_to_window(windows[-1])
        # 注册页面输入用户名、密码
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('password')
        sleep(3)

        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(2)
