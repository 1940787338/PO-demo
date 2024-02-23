import time
import unittest

from PO.study01.EPR_PO.Website.test_case.model import myunit, function
from PO.study01.EPR_PO.Website.test_case.page_object.LoginPage import *
from PO.study01.EPR_PO.Website.test_case.page_object.NxyjPage import *


class NxyjTest(myunit.StartEnd):
    def test_nxyj(self):
        login(self.driver, 'mobin', '123456')
        add_nxyj(self.driver, '梧州监测点', '梧州', '120', '666', '启用', '监测点')
        time.sleep(0.3)
        function.save_image(self.driver, 'add-nxyj.png')


if __name__ == '__main__':
    unittest.main()
