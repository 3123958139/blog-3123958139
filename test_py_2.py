"""
用于测试 my_py_class 内函数
"""
import sys

import my_py_class_

# 模块初始化
sys.path.append('D:\\360data\\Clion2016.1.3')
class_ = my_py_class_.myPyClass_()

# 下载 tushare.org 数据
# class_.get_url_data_()

# 调用 mysql 数据
# print(class_.get_sql_data_(code_='000886'))

# 运行 socket server
class_.run_socket_server_()
