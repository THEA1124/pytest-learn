import unittest

from day1.testcase.temp.test_api import TestApi

# #通过测试套件加载测试用例
# if __name__=='__main__':
#     #创建一个测试套件
#     suite = unittest.TestSuite()
#     #把测试用例加载到测试套件里，可以加载多个测试用例
#     #suite.addTest(TestApi('test_daa'))
#     testcase = TestApi('test_daa')
#     suite.addTest(testcase)
#     #执行用例的时候需要指定套件
#     unittest.main(defaultTest='suite')

#通过测试加载器加载测试用例
if __name__=='__main__':
    suite=unittest.defaultTestLoader.discover("./testcase/temp",pattern='test*.py')
    unittest.main(defaultTest='suite')
