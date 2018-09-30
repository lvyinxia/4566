import allure


class Test01():
    @allure.step('执行学院新增操作')
    def test01(self):
        print('执行学院新增操作')

    @allure.step('执行学院更新操作')
    def test02(self):
        allure.attach('断言开始','断言新增操作')
        print('执行学院更新操作')
        allure.attach('断言结束', '断言新增操作成功')