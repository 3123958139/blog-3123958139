"""
用于测试 my_py_class 内函数
"""
import sys

import class_

# 模块初始化
sys.path.append('D:\\360data\\blog-3123958139')
class_ = class_.myPyClass_()

# 运行 socket client
while True:
    print(class_.run_socket_client_())
