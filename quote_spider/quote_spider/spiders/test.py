import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.http import Request


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["bhashanet.in"]
    start_urls = ["https://bhashanet.in"]

    def __init__(self):
        self.links=[]
   
    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)

    # def parse_item(self, response):
    # # My Page Saver    
    #     filename = response.url.split("/")[-1] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #         return
