import os

import pytest
import yaml
from work.work_pytest01.pythoncode.calculator import Calculator

'''
• 作业1：
• 1、补全计算器（加减乘除）的测试用例
• 2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
• 3、将 Fixture 方法存放在conftest.py ，设置scope=module
• 作业2：
• 1、编写用例顺序：加- 除-减-乘
• 2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
• 3、本地生成测试报告
'''
# 读取测试数据


class GetDatas:
    mydatapath = os.path.dirname(__file__) + '/datas/calculator.yml'
    with open(mydatapath, encoding='utf-') as f:
        mydatas = yaml.safe_load(f)

    def add_datas(self):
        adddatas = self.mydatas['add']['datas']
        addname = self.mydatas['add']['myids']
        return [adddatas, addname]

    def sub_datas(self):
        subdatas = self.mydatas['sub']['datas']
        subname = self.mydatas['sub']['myids']
        return [subdatas, subname]

    def mul_datas(self):
        muldatas = self.mydatas['mul']['datas']
        mulname = self.mydatas['mul']['myids']
        return [muldatas, mulname]

    def div_datas(self):
        divdatas = self.mydatas['div']['datas']
        divname = self.mydatas['div']['myids']
        return [divdatas, divname]


class TestCaculator:

    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("\n**********测试开始**********\n")
    #
    # def teardown_class(self):
    #     print("\n**********测试结束**********")
    #
    # def setup(self):
    #     print("~~~~~~开始计算~~~~~~")
    #
    # def teardown(self):
    #     print("\n~~~~~~结束计算~~~~~~\n")
    @pytest.mark.run(order=0)
    # @pytest.mark.first
    @pytest.mark.parametrize('a, b, value', GetDatas().add_datas()[0], ids=GetDatas().add_datas()[1])
    def test_add(self, begin_caculator, a, b, value):
        result = round(begin_caculator.add(a, b), 2)
        assert value == result

    @pytest.mark.run(order=3)
    # @pytest.mark.fourth
    @pytest.mark.parametrize('a, b, value', GetDatas().div_datas()[0], ids=GetDatas().div_datas()[1])
    def test_div(self, begin_caculator, a, b, value):
        result = round(begin_caculator.divide(a, b), 2)
        assert value == result

    @pytest.mark.run(order=2)
    # @pytest.mark.second
    @pytest.mark.parametrize('a, b, value', GetDatas().sub_datas()[0], ids=GetDatas().sub_datas()[1])
    def test_sub(self, begin_caculator, a, b, value):
        result = round(begin_caculator.subtract(a, b), 2)
        assert value == result

    @pytest.mark.run(order=3)
    # @pytest.mark.third
    @pytest.mark.parametrize('a, b, value', GetDatas().mul_datas()[0], ids=GetDatas().mul_datas()[1])
    def test_mul(self, begin_caculator, a, b, value):
        result = round(begin_caculator.multiply(a, b), 2)
        assert value == result


