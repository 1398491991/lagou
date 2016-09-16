# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LagouPipeline(object):
    def process_item(self, item, spider):
        """
        {
    "pageSize": 16,
    "start": "16",
    "result": [
        {
            "companyId": 28417,
            "companyFullName": "深圳市中北明夷科技有限公司",
            "companyShortName": "兔展RabbitPre",
            "companyLogo": "i/image/M00/53/CB/CgqKkVfACyyAV9xxAADSnYHS0Pw739.png",
            "city": "深圳",
            "industryField": "移动互联网",
            "companyFeatures": "企业级移动营销大数据平台。",
            "financeStage": "成长型(B轮)",
            "interviewRemarkNum": 175,
            "positionNum": 16,
            "processRate": 82,
            "approve": 1,
            "countryScore": 0,
            "cityScore": 0
        },
        item 格式
        """
        return item
