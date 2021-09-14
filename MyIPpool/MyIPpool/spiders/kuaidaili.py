import scrapy
from ..items import MyippoolItem
import requests


class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com/free/inha/1/']

    # start_urls = ['http://www.kuaidaili.com/free/inha/1/']
    def start_requests(self):
        for i in range(1, 2):
            u = f'https://www.kuaidaili.com/free/inha/{i}/'
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        li_IP = response.xpath('.//table[@class="table table-bordered table-striped"]/tbody/tr')
        for i in li_IP:
            item = MyippoolItem()
            item['ip'] = i.xpath('./td[@data-title="IP"]/text()').get()
            item['port'] = i.xpath('./td[@data-title="PORT"]/text()').get()
            item['protocol'] = i.xpath('./td[@data-title="类型"]/text()').get()
            #if self.judge(item):
            yield item

    def judge(self, d):
        ip = d['ip']
        port = d['port']
        url = 'https://www.baidu.com'
        proxies = {
            'https': 'https://{}:{}'.format(ip, port),
            'http': 'http://{}:{}'.format(ip, port)
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'

        }

        try:
            rep = requests.get(url=url, proxies=proxies, headers=headers, timeout=3).status_code
            print(rep)
            if rep == 200:
                return True
            else:
                return False
        except:
            return False
