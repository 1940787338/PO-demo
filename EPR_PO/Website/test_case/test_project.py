import time
import unittest

from PO.study01.EPR_PO.Website.test_case.model import myunit, function
from PO.study01.EPR_PO.Website.test_case.page_object.LoginPage import *
from PO.study01.EPR_PO.Website.test_case.page_object.ProjectPage import *


class AddProjectTest(myunit.StartEnd):
    def test_add(self):
        login(self.driver, 'mobin', '123456')
        add_project(self.driver, '红蓝大战', '彬~~', '2024-02-23', '2024-03-30')
        function.save_image(self.driver, 'add-project.png')


if __name__ == '__main__':
    unittest.main()
