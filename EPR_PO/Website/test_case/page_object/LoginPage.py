from selenium.webdriver.common.by import By

from PO.study01.EPR_PO.Website.test_case.page_object.BasePage import Page


# 登录页
class LoginPage(Page):
    url = '/login'
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    login_btn_loc = (By.ID, 'loginBth')

    def type_username(self, username):
        self.base_input(self.username_loc, username)

    def type_password(self, password):
        self.base_input(self.password_loc, password)

    def type_submit(self):
        self.base_click(self.login_btn_loc)


def login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open(login_page.url)
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()
