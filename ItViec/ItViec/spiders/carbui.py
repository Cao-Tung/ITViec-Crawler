# from scrapy import Spider
# from scrapy.selector import Selector
# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# import sys
#
# class CarbuiItem(scrapy.Item):
#     title = scrapy.Field()
#
# class CarbuiSpider(CrawlSpider):
#     name = "carbui"
#     allowed_domains = ["careerbuilder.vn"]
#     start_urls = [
#         "http://careerbuilder.vn/viec-lam/cntt-phan-mem-c1-vi.html",
#     ]
#
#     rules = (
#         [Rule(LinkExtractor(allow='.*careerbuilder.vn/viec-lam/cntt-phan-mem-c1-.*vi.html'), callback="parse_item", follow=True),]
#     )
#
#
#     def parse_item(self, response):
#         questions = response.xpath('//span[@class="jobtitle"]/h3/a/@href').extract()
#
#         for question in questions:
#            full_url = response.urljoin(question)
#            yield scrapy.Request(full_url, callback=self.parse_question)
#
#     def parse_question(self, response):
#         item = CarbuiItem()
#         item["title"] = response.xpath('//p[@class="title_comp"]/text()').extract()
#         yield item