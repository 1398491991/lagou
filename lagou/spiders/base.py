#coding=utf-8
import MySQLdb
from ..settings import DB_CONFIG
import scrapy

class BaseSpider(scrapy.Spider):
    conn=MySQLdb.connect(**DB_CONFIG)
    name = None
    base_url=None

    def _requests(self, data, **kwargs):
        return scrapy.FormRequest(self.base_url, formdata=data, callback=self.parse, dont_filter=True,
                                  **kwargs)