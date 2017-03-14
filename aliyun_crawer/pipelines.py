# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from aliyun_crawer.settings import HOST

class AliyunCrawerPipeline(object):

    conn = pymysql.connect(host=HOST,port=3306,user='root',password='19980819',database='data',charset='utf8')
    def process_item(self, item, spider):
        self.conn.cursor().execute('insert ignore into pois values(%s,%s,%s,%s,%s,%s,%s,%s)',
                                   (item['id'],item['name'],item['district'],item['type'],item['location'],
                          item['address'],item['poiweight'],item['businessarea']))
        self.conn.commit()
        return item
