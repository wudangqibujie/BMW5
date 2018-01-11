# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class Bmw5Pipeline(object):
    def __init__(self):
        self.file = open('BMW5.json','w',encoding="utf-8")

    #存储数据，把item实例作为json数据写入到文件中
    def process_item(self, item, spider):
        if dict(item)['model']:
            a = dict(item)
            if a['year_age']:
                a['year'] = a['year_age'][0]
                a['age'] = a['year_age'][1]
            if a['price']:
                a['price'] = a['price'][0].strip()
            del a['year_age']
            lines = json.dumps(a,ensure_ascii = False)+'\n'
            self.file.write(lines)



    def close_spider(self,spider):
        self.file.close()



