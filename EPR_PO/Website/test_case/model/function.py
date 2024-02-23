import csv
import os.path
import time
from selenium import webdriver


# 封装截图方法
def save_image(driver, filename):
    # 获取当前文件路径
    func_path = os.path.dirname(__file__)
    base_path = os.path.dirname(func_path).split('test_case')[0]
    # 截图存放根路径
    file_path = base_path + 'test_report/srceenshot/' + time.strftime('%Y-%m-%d  %H-%M-%S') + filename
    # 保存截图
    driver.get_screenshot_as_file(file_path)
    print('save image successful to path: %s' % file_path)


# 读取数据方法
def read_csv_data(file_path):
    # 定义返回的数据
    data = []
    with open(file_path, 'r', encoding='UTF-8') as f:
        csv_file = csv.reader(f)
        # 下移一行 跳过标题行
        next(csv_file)
        for row in csv_file:
            # 每次遍历是一行 追加进 data里
            data.append(row)
        return data


# 读取数据 读取某一行
def read_csv_line(file_path, line):
    with open(file_path, 'r', encoding='UTF-8') as f:
        csv_file = csv.reader(f)
        # 枚举每行的数据
        for index, row in enumerate(csv_file, 1):
            # 如果枚举到的索引等于就传入的行，就返回当前行的数据
            if index == line:
                return row


if __name__ == '__main__':
    data_path = 'G:/upup/自动化测试/PO/study01/EPR_PO/Website/test_data/test_data.csv'
    print(read_csv_line(data_path, 2))
