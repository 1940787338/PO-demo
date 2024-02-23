import time
import unittest

import ddt

from PO.study01.EPR_PO.Website.test_case.model import myunit, function
from PO.study01.EPR_PO.Website.test_case.page_object.LoginPage import *
from PO.study01.EPR_PO.Website.test_case.page_object.NxyjPage import *


@ddt.ddt
class NxyjTest(myunit.StartEnd):
    data_url = 'G:/upup/自动化测试/PO/study01/EPR_PO/Website/test_data/test_data.csv'
    test_data = function.read_csv_data(data_url)

    @ddt.data(*test_data)
    def test_nxyj(self, values):
        login(self.driver, 'mobin', '123456')
        add_nxyj(self.driver, values[0], values[1], values[2], values[3], values[4], values[5])
        time.sleep(0.3)
        function.save_image(self.driver, 'add-nxyj.png')


if __name__ == '__main__':
    unittest.main()
