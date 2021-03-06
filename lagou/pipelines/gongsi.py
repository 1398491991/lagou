#coding=utf-8
from base import BasePipeline
import json

class GongSiPipelines(BasePipeline):
    sql = """insert into gongsi(company_id,detail) values(%s,%s) """
    def process_item(self, item, spider):
        if spider.name!="gongsi":
            return item
        """item 格式 字典
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

        """
        cur=None
        conn=None
        try:
            conn = item['conn']
            cur=conn.cursor()
            result_list=item['gongsi']['result']
            for result in result_list:
                companyId = result['companyId']
                cur.execute(self.sql,(companyId,json.dumps(result)))
                conn.commit()

        except KeyError:
            pass
        except Exception as e:
            print '\n\n\n################################\n\n\n',e
            if conn:conn.rollback()
        finally:
            if cur:cur.close()
            return item