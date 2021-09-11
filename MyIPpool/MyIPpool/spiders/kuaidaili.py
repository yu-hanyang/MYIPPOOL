import scrapy
from ..items import MyippoolItem

class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com/free/inha/1/']
    # start_urls = ['http://www.kuaidaili.com/free/inha/1/']
    def start_requests(self):
        for i in range(1,6):
            u = f'https://www.kuaidaili.com/free/inha/{i}/'
            yield scrapy.Request(url=u,callback=self.parse)

    def parse(self, response):
        li_IP=response.xpath('.//table[@class="table table-bordered table-striped"]/tbody/tr')
        for i in li_IP:
            item=MyippoolItem()
            item['ip']=i.xpath('./td[@data-title="IP"]/text()').get()
            item['port']=i.xpath('./td[@data-title="PORT"]/text()').get()
            item['protocol']=i.xpath('./td[@data-title="类型"]/text()').get()
            yield item