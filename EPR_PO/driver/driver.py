from selenium import webdriver


# 存放浏览器驱动文件夹
def browser():
    driver = webdriver.Chrome()
    return driver
