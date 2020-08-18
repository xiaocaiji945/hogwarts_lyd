import os
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWexin():
    def setup(self):
        # 复用浏览器
        option = Options()
        option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        # 从shelve中读取cookie
        db = shelve.open('mydb/logincookies')
        self.cookies = db['cookie']
        db.close()

    def teardown(self):
        self.driver.quit()

    def test_weixin_import(self):
        '''
        使用cookie 登录企业微信，完成导入联系人，加上断言验证
        '''
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        for cookie in self.cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        ex_path = os.path.dirname(__file__) + '/test01.xlsx'
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys(ex_path)
        sleep(3)
        text_value = self.driver.find_element(By.ID, 'upload_file_name').text
        assert 'test01.xlsx' == text_value

    @pytest.mark.skip
    def test_weixin01(self):
        sleep(3)
        # # 切换通讯录
        # self.driver.find_element(By.ID, "menu_contacts").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        # # 获取coockie
        # coockies = self.driver.get_cookies()
        # print(coockies)

        # # 将cookies写入shelve
        # db = shelve.open('mydb/logincookies')
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853145129250'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853145129250'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325025156755'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'jhwI26vLByhnkSATww32Hm9-TSOSPtmiUKNNL-w6bv89LaamNY7uk_oWOti2BazA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2725481'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '_jBXd2fUmEUrAAsoQd3zLOKyiG-7-pWFtKAzKDRnCGxz9xSC8geFlpvREieKvmpnjF6c_CzbroSYU5eoHYG2xFk0ZGQ-1q811GdMBViBnXBxshrD8a0UZSDct45APZzGYsjX6HEhAPbUugLPz_m3mugK5oZ7w-1cr648usO7zMpA6HHqpARikFZaptHQbEfKCq6M8sH0oDK4BZCAj6CcpLEipeWRoS-aQXv03395XY4axeaj0HuOU3L9ymBxUhUjduNbLGu-XJne9aJdtYO07w'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597790502.12, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '11npg1i'}, {'domain': '.qq.com', 'expiry': 1597848536, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.31206385.1597758968'}, {'domain': '.qq.com', 'expiry': 1660834136, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1217963930.1597758968'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629294966, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1598277883, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1226331226'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'c7982d036e0f0f11a6081232c0c770dd48541fb49b564c1c158d096a9d798aa1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629298111, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597758967,1597761074,1597762111'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '7rg4FbMSU7'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600354571, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597762111'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '40719120592910243'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5457384448'}]
        # db['cookie'] = cookies

        # # 从shelve中读取cookie
        db = shelve.open('mydb/logincookies')
        cookies = db['cookie']
        db.close()

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
