from time import sleep

import pytest

from selenium_class.test_preview02.driver_import import DrIm

'''
打开百度首页
输入搜索关键词
点击搜索后，跳转到搜索结果页
滑动到底部，点击'下一页'
'''


class TestJS(DrIm):
    @pytest.mark.skip
    def test_js_scroll(self, open_url):
        self.driver.get('https://www.baidu.com/')
        # text_input = self.driver.find_element_by_id('kw')
        # search_btn = self.driver.find_element_by_id('su')
        # 使用js获取元素
        text_input = self.driver.execute_script('return document.getElementById("kw")')
        search_btn = self.driver.execute_script('return document.getElementById("su")')

        text_input.send_keys('selenium')
        search_btn.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)

        next_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]')
        next_btn.click()
        sleep(3)

        # for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    '''
    打开网址：https://www.12306.cn/index/
    修改出发日期为 2020-12-30
    打印出发日期
    关闭网站
    '''
    def test_datetime(self, open_url):
        self.driver.get('https://www.12306.cn/index/')
        # date_text = self.driver.execute_script('document.getElementById("train_date")')
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2020-12-30"')
        sleep(3)
