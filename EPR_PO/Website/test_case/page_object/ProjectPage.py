import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from PO.study01.EPR_PO.Website.test_case.page_object.BasePage import Page


# 项目维护页面
class ProjectPage(Page):
    url = '/index/xmwh'
    project_page_loc = (By.XPATH, '/html/body/div/div/section/section/aside/ul/li[2]/ul/li/ul/a[1]/li')
    add_btn_loc = (By.XPATH, '/html/body/div/div/section/section/main/div/div[4]/button')
    name_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[1]/div/div[1]/input')
    person_in_head_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[2]/div/div[1]/input')
    start_date_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[3]/div/div/input')
    end_date_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[4]/div/div/input')
    project_status_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[5]/div/div/div/input')
    status_ok_loc = (By.CLASS_NAME, 'el-select-dropdown__item selected')
    picture_loc = (
        By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[2]/form/div[6]/div/div/div/i')

    save_btn_loc = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[1]/div/div[3]/div/button[2]/span')

    def type_project_page(self):
        self.base_click(self.project_page_loc)

    def type_add_btn(self):
        self.base_click(self.add_btn_loc)

    def type_name(self, name):
        self.base_input(self.name_loc, name)

    def type_head(self, person_in_head):
        self.base_input(self.person_in_head_loc, person_in_head)

    def type_start_date(self, start_date):
        self.base_input(self.start_date_loc, start_date)

    def type_end_date(self, end_date):
        self.base_input(self.end_date_loc, end_date)

    def type_status(self):
        self.base_click(self.project_status_loc)
        a = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.status_ok_loc)
        )
        a.click()

    def type_picture(self, picture_file):
        pass

    def type_submit(self):
        self.base_click(self.save_btn_loc)


def add_project(driver, name, person_in_head, start_date, end_date):
    project_page = ProjectPage(driver)
    project_page.type_project_page()
    project_page.type_add_btn()
    project_page.type_name(name)
    project_page.type_head(person_in_head)
    project_page.type_start_date(start_date)
    project_page.type_end_date(end_date)
    project_page.type_status()
    project_page.type_submit()
