# -*- coding: utf-8 -*-
from base import BaseSpider

class ZhiweiSpider(BaseSpider):
    name = "zhiwei"
    # allowed_domains = []
    base_url="http://www.lagou.com/gongsi/searchPosition.json"
    start_urls = (
        'http://www.zhiwei/',
    )
    page = 1
    data = {'companyId':'52315',
            'positionFirstType':u'全部',
            'pageNo':str(page),
            'pageSize':'10'}


    def start_requests(self):

        yield self._requests(data=self.data,)


    def parse(self, response):
        pass
