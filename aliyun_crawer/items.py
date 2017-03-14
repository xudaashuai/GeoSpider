# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    name=scrapy.Field()
    type=scrapy.Field()
    location=scrapy.Field()
    district=scrapy.Field()
    address=scrapy.Field()
    poiweight=scrapy.Field()
    businessarea=scrapy.Field()
    pass
