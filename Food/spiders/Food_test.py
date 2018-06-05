# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import FoodItem

class FoodTestSpider(scrapy.Spider):
    name = 'Food_test'
    allowed_domains = ['meishij.net']
    start_urls = ['https://www.meishij.net/chufang/diy/']

    def parse(self, response):
        pass
        # jpy = PyQuery(response.text)

        # menu =jpy('#listnav_con_c > dl.listnav_dl_style1.w990.bb1.clearfix > dd')
        # menu_list =jpy('#listtyle1_list > div')



        # for it in menu_list.items():
        #     a_tag = it('a')
        #     item = FoodItem()
        #     item['Dishes'] = a_tag.text()
        #     item['url'] = a_tag.attr('href')
        #     item['Popularity'] = it('a > div > div > div.c1 > span').text()
        #     yield item



