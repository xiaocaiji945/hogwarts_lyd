import allure


@allure.link('https://www.baidu.com', name='链接')
def test_with_link():
    print('这是一条link链接')
    pass


TEST_CASE_LINK = 'https://www.jianshu.com/p/82cdc0eddb16'


@allure.testcase(TEST_CASE_LINK, name='登录用例')
def test_with_case_link():
    print('这是一条测试用例的链接')
    pass


# --allure-link-pattern=issue:http://www.ceshi.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    print('这是一条issur的链接')
    pass
