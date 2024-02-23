import time
import unittest
import HTMLTestRunner
print('test start')
# 测试目录
test_dir = './test_case'
# 测试报名目录
report_dir = './test_report/' + time.strftime('%Y-%m-%d %H-%M-%S') + 'result.html'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_nxyj.py')

with open(report_dir, 'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='啊彬测试报告', description='能效预警测试')
    runner.run(discover)
    f.close()

print('test end')
