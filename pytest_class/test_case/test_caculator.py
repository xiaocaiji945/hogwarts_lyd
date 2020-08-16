# -*- coding: utf-8 -*-
import allure
import pytest
import yaml

from pytest_class.pythoncode import calculator
from pytest_class.pythoncode.calculator import Calculator


# 读取测试数据
class GetDatas:
    with open('./datas/calculator.yml', encoding='utf-') as f:
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

@allure.feature('这是测试计算器的class')
class TestCaculator:

    def setup_class(self):
        self.calc = Calculator()

    @allure.story('这是测试计算器的story')
    @pytest.mark.parametrize('a, b, value', GetDatas().add_datas()[0], ids=GetDatas().add_datas()[1])
    def test_add(self, a, b, value):
        with allure.step('这是测试计算器加法的step'):
            result = round(self.calc.add(a, b), 2)
        with allure.step('这是校验加法结果的step'):
            assert value == result

    @pytest.mark.parametrize('a, b, value', GetDatas().sub_datas()[0], ids=GetDatas().sub_datas()[1])
    def test_sub(self, a, b, value):
        result = round(self.calc.subtract(a, b), 2)
        assert value == result

    @pytest.mark.parametrize('a, b, value', GetDatas().mul_datas()[0], ids=GetDatas().mul_datas()[1])
    def test_mul(self, a, b, value):
        result = round(self.calc.multiply(a, b), 2)
        assert value == result

    @pytest.mark.parametrize('a, b, value', GetDatas().div_datas()[0], ids=GetDatas().div_datas()[1])
    def test_div(self, a, b, value):
        result = round(self.calc.divide(a, b), 2)
        assert value == result