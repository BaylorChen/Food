# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodItem(scrapy.Item):
    # define the fields for your item here like:)
    id  =scrapy.Field() # tab
    # Dishes = scrapy.Field() #菜名
    # pic = scrapy.Field()
    # url = scrapy.Field()
    # material = scrapy.Field() #材料
    # Method = scrapy.Field()# 做法
    # Popularity = scrapy.Field()# 人气