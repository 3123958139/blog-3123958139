"""
用于测试 libdll_.dll 函数
"""

# -*- coding: utf-8 -*-
import sys
import class_
import tushare
from ctypes import *

# 加载模块，获得 dll 句柄
sys.path.append('D:\\360data\\blog-3123958139')
h_dll_ = class_.class_().import_dll_()

# 调用函数1
h_dll_.hello_()

# 由调用函数1知道调用方法，所以根据需要下载测试数据
data_frame = tushare.get_hist_data('sh')
stock_open_ = data_frame['open'].values
stock_high_ = data_frame['high'].values
stock_low_ = data_frame['low'].values
stock_close_ = data_frame['close'].values

stock_len_ = len(stock_open_)
ma_len_ = 5

# 数据格式转换
stock_open_ = (c_double * stock_len_)(*stock_open_)
stock_high_ = (c_double * stock_len_)(*stock_high_)
stock_low_ = (c_double * stock_len_)(*stock_low_)
stock_close_ = (c_double * stock_len_)(*stock_close_)

# 调用函数2
h_dll_.w_price_rate_ma_(stock_open_, stock_high_, stock_low_, stock_close_, stock_len_, ma_len_)
