# content of test_sample.py
import pytest


def inc(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (3,4),
    (10,20),
    ('a','a1'),
    (9,10)
])
def test_answer(a,b):
    assert inc(a) == b

def test_answer1():
    assert inc(4) == 5

@pytest.fixture()
def login():
    print('登录操作')
    username = '测试'
    return username

class TestDemo:
    def test_a(self, login):
        print(f'a   login = {login}')
    def test_b(self):
        print('b')
    def test_c(self, login):
        print(f'c   login = {login}')


# if __name__ == '__main__':
#     pytest.main(['test_a.py::TestDemo','-v'])