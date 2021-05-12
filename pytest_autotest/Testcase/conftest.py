"""
该文件是专门存放fixture的配置文件，单独管理全局的fixture,只对同一个package下的所有用例生效
fixture(固定装置):https://www.osgeo.cn/pytest/fixture.html#fixture-availabiility
"""
# 示例
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

# fixture使用方式一：测试函数通过将fixture声明为参数来请求fixture
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket