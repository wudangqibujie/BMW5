# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Bmw5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model = scrapy.Field()
    # age = scrapy.Field()
    year_age = scrapy.Field()
    price = scrapy.Field()
    # car_url = scrapy.Field()
    # img_url=scrapy.Field()

