# -*- coding: utf-8 -*-
from base import BaseSpider
import scrapy
from ..items import GongSiItem
import json
import logging


class GongSiSpider(BaseSpider):
    """
    专门抓取 公司介绍信息的爬虫 通过  http://www.lagou.com/gongsi/0-0-0.json post 获得
    """
    name = "gongsi"
    # allowed_domains = []
    base_url = 'http://www.lagou.com/gongsi/0-0-0.json'   # 方法 post
    start_urls = (
        base_url,
    )

    page=1
    data={'first':'false',
            'pn':str(page),
            'sortField':'0',
            'havemark':'0',}

    def start_requests(self):

        yield self._requests(data=self.data,)

    def parse(self, response):
        item = GongSiItem()
        try:
            res=json.loads(response.text)
            if res['result']:
                item['gongsi']=res
                item['conn']=BaseSpider.conn
                yield item
                self.page += 1
                self.page = int(self.data['pn']) + 1
                self.data['pn'] = str(self.page)
                yield self._requests(data=self.data)

        except ValueError:
            self.log('response result json format error : %s'%response.text,level=logging.warn)



    def _requests(self,data,**kwargs):
        return scrapy.FormRequest(self.base_url,formdata=data,callback=self.parse,dont_filter=True)

