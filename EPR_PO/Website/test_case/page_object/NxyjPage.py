from selenium.webdriver.common.by import By

from PO.study01.EPR_PO.Website.test_case.page_object.BasePage import Page


# 能效预警页
class NxyjPage(Page):
    url = '/index/nxyj'
    nxyj_loc = (By.XPATH, '/html/body/div/div/section/section/aside/ul/li[1]/ul/li/ul/a/li')
    add_btn_loc = (By.XPATH, '/html/body/div/div/section/section/main/div/div[3]/button')
    name_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div[1]/input')
    address_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div[1]/input')
    power_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[3]/div/div[1]/input')
    voltage_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[4]/div/div[1]/input')
    status_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[5]/div/div/input')
    note_loc = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[2]/form/div[6]/div/div/input')
    save_btn_loc = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[4]/div/div[3]/div/button[2]')

    def type_nxyj(self):
        self.base_click(self.nxyj_loc)

    def type_add_btn(self):
        self.base_click(self.add_btn_loc)

    def type_name(self, name):
        self.base_input(self.name_loc, name)

    def type_address(self, address):
        self.base_input(self.address_loc, address)

    def type_power(self, power):
        self.base_input(self.power_loc, power)

    def type_voltage(self, voltage):
        self.base_input(self.voltage_loc, voltage)

    def type_status(self, status):
        self.base_input(self.status_loc, status)

    def type_note(self, note):
        self.base_input(self.note_loc, note)

    def type_submit(self):
        self.base_click(self.save_btn_loc)


def add_nxyj(driver, name, address, power, voltage, status, note):
    nxyj_page = NxyjPage(driver)
    nxyj_page.type_nxyj()
    nxyj_page.type_add_btn()
    nxyj_page.type_name(name)
    nxyj_page.type_address(address)
    nxyj_page.type_power(power)
    nxyj_page.type_voltage(voltage)
    nxyj_page.type_status(status)
    nxyj_page.type_note(note)
    nxyj_page.type_submit()
