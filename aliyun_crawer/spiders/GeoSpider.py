import json
import logging
import pymysql
from aliyun_crawer.settings import HOST
from scrapy import *

from aliyun_crawer.items import *


class GeoSpider(Spider):
    name = 'GeoSpider'
    api_url = "http://restapi.amap.com/v3/geocode/regeo?key={0}&location={1}&radius=100&extensions=all&batch=true"
    key = '59a8167b169e97d4acda9ad829fbcc23'
    poi_info = ['id', 'name', 'type', 'location', 'address', 'poiweight', 'businessarea']

    def __init__(self):
        self.locations = set()
        self.ids = set()
        conn = pymysql.connect(host=HOST,port=3306,user='root',password='19980819',database='data')
        my_cur = conn.cursor()
        my_cur.execute('select location from spois')
        k=my_cur.fetchall()
        logging.info(k)
        for x in k:
            self.locations.add(x[0])

    def get_url(self, location_list):
        s = location_list[0].replace(' ', '')
        for x in range(location_list.__len__() - 1):
            s += '|' + location_list[x + 1].replace(' ', '')
        return self.api_url.format(self.key, s)

    def start_requests(self):
        index = 0
        while self.locations.__len__() >= 20:
            location_list = []
            while location_list.__len__() < 20:
                location_list.append(self.locations.pop())
            url = self.get_url(location_list)
            logging.info(url)
            yield Request(url=url, callback=self.parse)
            return

    def parse(self, response):
        result = json.loads(response.text)
        if result['info'] != 'OK':
            logging.info('something error happen with' + response.url)
        for node in result['regeocodes']:
            district = node['addressComponent']['district']
            for poi in node['pois']:
                item = PoiItem()
                id = poi['id']
                if id in self.ids:
                    continue
                self.ids.add(id)
                item['district'] = district
                for x in self.poi_info:
                    if type(poi[x]) != list:
                        item[x] = poi[x]
                    else:
                        item[x]=None
                yield item
