# -*- coding: utf-8 -*-
from base import BaseSpider

class PinglunSpider(BaseSpider):
    name = "pinglun"
    # allowed_domains = []
    base_url="http://www.lagou.com/gongsi/searchInterviewExperiences.json"
    start_urls = (
        base_url,
    )

    page=1


    data ={'companyId':'23177',
    'positionType':'',
    'pageSize':'10',
    'pageNo':str(page)}


    def start_requests(self):

        yield self._requests(data=self.data,)

    def parse(self, response):
        pass


