#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-09 23:28:08
LastEditTime: 2021-07-10 00:06:38
Description: 处理 33w 条数据 .CSV 文件
'''
import os
import sys
import pandas as pd

PATH = sys.path[0]
csv_path = os.path.join(os.path.join(PATH, "data"), "tuijian.csv")

data = pd.read_csv(csv_path)
# print(data.columns)
def check_key(df):
    '''
    查找包含某个关键词的
    '''
    return data["content"].str.contains("星空")
result = data.loc[check_key, : ]
print(type(result))
print(result)
result.to_csv("星空.csv",index=False)
