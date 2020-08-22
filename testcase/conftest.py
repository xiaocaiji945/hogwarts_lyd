# import shelve
# from typing import List
#
# import pytest
#
# from page.base_page import BasePage
#
#
# def pytest_collection_modifyitems(
#         session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     # 修改编码
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#
#
# @pytest.fixture(scope="session")
# def cookie_login():
#     base = BasePage()
#
#     login_url = 'https://work.weixin.qq.com/'
#     # 从shelve中读取cookie
#     db = shelve.open('mydb/logincookies')
#     cookies = db['cookie']
#     db.close()
#
#     # base.driver.get(login_url)
#     for cookie in cookies:
#         base._driver.get_cookies(cookie)
