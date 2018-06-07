# -*- coding: utf-8 -*-
import requests
import scrapy
from pyquery import PyQuery
from ..items import FoodItem
from ..utils.parse import parse, Home_cooking, othe_cooking, Dishes, Dishes_Details
from scrapy.http import Request
from traceback import format_exc

from pymongo import MongoClient
class FoodTestSpider(scrapy.Spider):
    name = 'Food_test'
    allowed_domains = ['meishij.net']
    start_urls = ['https://www.meishij.net/chufang/diy/']


    client = MongoClient()
    db = client.test  # 连接test数据库，没有则自动创建
    my_set = db.meishi  # 使用set集合，没有则自动创建
    result = {"": {"": []}}
    def parse(self, response):
        url_list = parse(response)
        for url in url_list:
            item = Request(url_list[url],
                          callback=self.jiachagncai,
                         meta={"url":url},
                          errback=self.error_back,)



            yield item

        # with open('meishi.json', 'w', encoding='utf-8') as f:
        #     f.write(self.result)


    def jiachagncai(self, response):
        # requests.post().url

        if response.url == 'https://www.meishij.net/chufang/diy/':
            home = Home_cooking(response)
            #print(home)
        else:
            home = othe_cooking(response)
        for url in home:
            #print(url)
            name = response.meta["url"]
            name_= self.result.get(name,{})
            # print(name_)
            name__ = name_.get(name,{}).get(url,[])
            # name__.append(url)
            name_[url] = name__
            _name = {name:name_}
            self.result.update(_name)
            # print(name_)
            # print(type(self.result.get(name)))
            yield Request(home[url],
                          callback=self.shangping_list,
                          meta={"temp":{"first": name, "se":url}},
                          errback=self.error_back,)



    def shangping_list(self,response):
        date = Dishes(response)
        for url in date:
            yield Request(url,
                          callback=self.xiangqingye,
                          meta=response.meta['temp'],
                          errback=self.error_back, )

    def xiangqingye(self,response):
        first = response.meta['first']
        se = response.meta['se']
        print('---------------------------',first)
        print('===========================',se)

        temp = Dishes_Details(response)
        # self.result.get(first).get(se).append(temp)
        self.my_set.insert({first:{se:temp}})
        # print(response.meta['temp']:temp)




    def error_back(self, e):
        _ = e
        self.logger.error(format_exc())
