import unittest

from PO.study01.EPR_PO.driver.driver import browser


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
