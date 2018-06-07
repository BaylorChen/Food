__author__ = 'chenjianguo'
# -*- coding:utf-8 -*-


from scrapy.cmdline import execute

execute('scrapy crawl Food_test'.split())


# from pymongo import MongoClient
# client = MongoClient()
# db = client.test #连接test数据库，没有则自动创建
# my_set = db.set #使用set集合，没有则自动创建
# my_set.insert({'name':'Vinie','age':24})#插入一条数据
# my_set.insert({'name':{'Vinie':[{'1':'2'},{'3':'4'}]}})#插入一条数据

