# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests
import pymysql
from .settings import *
import datetime

class MyippoolPipeline:
    def process_item(self, item, spider):

        print(item)


        return item


class MyippoolmysqlPipeline:
    def open_spider(self,spider):
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, database=MYSQL_DB, passwd=MYSQL_PWD, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self,item, spider):
        ins = "insert into myippool('ip','port','protocal') values(%s %s %s)"
        x = datetime.datetime.now()
        now = str(x.strftime("%Y")) + '-' + str(x.strftime("%m")) + '-' + str(x.strftime("%d"))
        li = [item['ip'],item['port'],item['protocol']]
        #self.cur.execute(ins, li)
        self.cur.execute(f"insert into myippool('ip','port','protocal') values('{item['ip']}' '{item['port']}' '{item['protocol']}')")
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.db.close()


    # def judge(self,d):
    #     ip=d['ip']
    #     port=d['port']
    #     url='https://www.baidu.com'
    #     proxies = {
    #         'https': 'https://{}:{}'.format(ip, port),
    #         'http': 'http://{}:{}'.format(ip, port)
    #     }
    #     headers={
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    #
    #     }
    #
    #     try:
    #         rep=requests.get(url=url,proxies=proxies,headers=headers,timeout=3).status_code
    #         print(rep)
    #         if rep==200:
    #             return True
    #         else:return False
    #     except:
    #         return False
