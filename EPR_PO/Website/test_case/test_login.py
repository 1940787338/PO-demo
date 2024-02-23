import time
import unittest

from PO.study01.EPR_PO.Website.test_case.model import myunit, function
from PO.study01.EPR_PO.Website.test_case.page_object.LoginPage import *


class LoginTest(myunit.StartEnd):
    def test_login(self):
        login(self.driver, 'mobin', '123456')
        time.sleep(0.5)
        function.save_image(self.driver, 'login.png')


if __name__ == '__main__':
    unittest.main()
