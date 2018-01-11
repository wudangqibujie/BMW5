import scrapy
from BMW_5.items import Bmw5Item

class BMWW_5_Spider(scrapy.Spider):
    name = "BMW5"
    url = "https://www.renrenche.com/cn/baoma_baoma5xi/p{page}/?brand=baoma&series=baoma5xi"

    def start_requests(self):
        for page in range(1,13):
            yield scrapy.Request(url=self.url.format(page=page),callback=self.parse_one)

    def parse_one(self,response):
        # item = Bmw5Item()
        qw = response.xpath('//div[@class="jscroll-added"]/div//ul/li')
        # print(qw)
        for one in qw:
            item = Bmw5Item()
            item['model'] = one.xpath('a/@title').extract()
            item['year_age'] = one.xpath('a/div[2]/span/text()').extract()
            item['price'] = one.xpath('a/div[3]/div/text()').extract()
            # item['car_url'] = one.xpath('a/@href').extract()
            # item['img_url'] = one.xpath('a/div/img/@src').extract()
            yield item



