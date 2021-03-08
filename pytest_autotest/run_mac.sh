pytest --alluredir ./Testcase/allure-results --clean-alluredir
# 由于pytest生成的大多数是json原文件，所以使用--clean-alluredir参数清除allure-results历史数据
allure generate ./Testcase/allure-results -c -o allure-report
# generate命令导出新的html到新目录
allure open ./Testcase/allure-report
# 在浏览器中打开html