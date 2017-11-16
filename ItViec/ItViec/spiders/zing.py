# from scrapy import Spider
# from scrapy.selector import Selector
# import scrapy
# from ItViec.items import ItviecItem
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# import sys
#
# class CarbuiSpider(CrawlSpider):
#     name = "itviec"
#     allowed_domains = ["itviec.com"]
#     start_urls = [
#         "https://itviec.com/viec-lam-it/senior-backend-developer-nodejs-athena-studio-1236",
#     ]
#
#     rules = (
#         [Rule(LinkExtractor(allow='.*itviec.com/viec-lam-it/.*'), callback="parse_item", follow=True),]
#     )
#
#
#     def parse_item(self, response):
#         questions = response.xpath('//h2[@class="title"]/a/@href').extract()
#
#         for question in questions:
#            full_url = response.urljoin(question)
#            yield scrapy.Request(full_url, callback=self.parse_question)
#
#     def parse_question(self, response):
#         item = ItviecItem()
#         item["content"] = response.xpath('//div[@class="job_info"]/h1/text()').extract()
#         yield item