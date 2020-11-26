# Autotest
本案例使用python+pytest+allure实现接口自动化测试实例

#### 实现准备

* 安装allure
* 虚拟环境搭建
* 安装依赖包（本案例直接使用我导入的txt文件里的包即可）
* 导包命令：pip install -r requirements.txt
#### 目录结构讲解
* 根目录：Autotest
* 项目目录：pytest_autotest
* Common文件：存放的公共方法
* Config文件：配置文件及读取方法
* Params文件：存放的测试数据及读取数据后的py文件，目的是为了测试数据和测试用例分离，可维护。
* Testcase文件：存放测试用例及输出测试报告
