import time

import allure
import pytest
from selenium import webdriver


@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data1', ['测试', '开发', '产品'])
def test_steps_demo(test_data1):
    with allure.step('打开百度网页'):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://www.baidu.com')
        driver.maximize_window()
    with allure.step('搜索前保存图片'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', name='初始页面', attachment_type=allure.attachment_type.PNG)

    with allure.step(f'输入关键词：{test_data1}'):
        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(2)
    with allure.step('保存图片'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', name='搜索结果', attachment_type=allure.attachment_type.PNG)
        # allure.attach('<head></head><body>首页</body>', attachment_type=allure.attachment_type.HTML)
    with allure.step('关闭浏览器'):
        driver.quit()
