from typing import List

import pytest
# import os,sys
# sys.path.append(os.getcwd())


from work.work_pytest01.pythoncode.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="module")
def begin_caculator():
    calc = Calculator()
    print("\n**********测试开始**********\n")
    yield calc
    print("\n**********测试结束**********")


@pytest.fixture(autouse=True, scope="function")
def begin_caculator02():
    print("~~~~~~开始计算~~~~~~")
    yield
    print("\n~~~~~~结束计算~~~~~~\n")
