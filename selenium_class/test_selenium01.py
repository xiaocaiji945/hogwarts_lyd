from selenium import webdriver


def test_selenium_01():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.baidu.com')
