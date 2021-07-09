#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-07-08 14:09:21
LastEditTime: 2021-07-08 16:09:37
Description: 多线程爬取句子迷推荐的句子,并存入 MongoDB 数据库
'''
from re import T
import threading
from APItest import *
import pymongo
from concurrent.futures import ThreadPoolExecutor


def getJuzhi_one() -> list:
    while True:
        api = GetJuzhi()
        result = api.get_tuijian()
        dataList = result["data"]["list"]
        ones = []
        
        for data in dataList:
            one = {}
            # print(data)
            one["_id"] = data["uuid"]  # 作品标识符
            one["cover"] = data["cover"]  # 封面图
            one["content"] = data["content"]  # 内容
            one["author"] = data["referAuthorName"]  # 作者名字
            one["works"] = data["referWorksName"]  # 出处作品
            writeMongo_one(one)
            # ones.append(one)
        # return ones

def getJuzhi() -> list:

    api = GetJuzhi()
    result = api.get_tuijian()
    dataList = result["data"]["list"]
    ones = []
    
    for data in dataList:
        one = {}
        # print(data)
        one["_id"] = data["uuid"]  # 作品标识符
        one["cover"] = data["cover"]  # 封面图
        one["content"] = data["content"]  # 内容
        one["author"] = data["referAuthorName"]  # 作者名字
        one["works"] = data["referWorksName"]  # 出处作品
        ones.append(one)
        
    return ones


def writeMongo():
    while True:
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["juzhi"]  # 数据库
        mycol = mydb["tuijian"]  # 数据集合
        try:
            mylist = getJuzhi()
            x = mycol.insert_many(mylist,ordered=False)
            # print(x.inserted_ids)
            print("线程%s,已插入:%s" % (threading.current_thread().name, len(x.inserted_ids)))
        except Exception as e:
            # print("线程%s,出现错误:%s" % (threading.current_thread().name, e))
            pass
            # break
        finally:
            myclient.close()

def writeMongo_one(one):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["juzhi"]  # 数据库
    mycol = mydb["tuijian"]  # 数据集合
    try:
        mycol.insert_one(one)
        print("线程%s,插入成功! %s"%(threading.current_thread().name,one["content"]))
    except Exception as e:
        # print("线程%s,出现错误:%s" % (threading.current_thread().name, e))
        pass
    finally:
        myclient.close()
    

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=30) as pool:
        for i in range(30):
            # 1分钟: 179693 _> 186372
            pool.submit(writeMongo)
            # 一分钟: 188665-> 190247 
            # pool.submit(getJuzhi_one)

