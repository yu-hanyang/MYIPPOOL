# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests


class MyippoolPipeline:
    def process_item(self, item, spider):
        if self.judge(item):
            print(item)
        else:
            print('meiyong',item)


        return item


    def judge(self,d):
        ip=d['ip']
        port=d['port']
        url='https://www.baidu.com'
        proxies = {
            'https': 'https://{}:{}'.format(ip, port),
            'http': 'http://{}:{}'.format(ip, port)
        }
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

        }

        try:
            rep=requests.get(url=url,proxies=proxies,headers=headers,timeout=3).status_code
            print(rep)
            if rep==200:
                return True
            else:return False
        except:
            return False
