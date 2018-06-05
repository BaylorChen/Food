# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class FoodPipeline(object):

    def open_spider(self, spider):
        self.file = open('Food_test.txt', 'w', encoding='utf8')
        print('打开文件了')

    def process_item(self, item, spider):
        line = '{}\n'.format(json.dumps(dict(item), ensure_ascii=False))
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('关闭文件了')

