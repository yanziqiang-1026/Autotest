"""
该文件是专门存放fixture的配置文件，单独管理全局的fixture,只对同一个package下的所有用例生效
"""
import pytest

# @pytest.fixture(scope='package',autouse=True)
# def initialization():
#     # yield 生成器，yield之前是初始化，yield之后是清楚
#     yield
#
#     print("clear")