import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rules = (Rule(LinkExtractor(),callback='parse_page',follow=False),)

    def parse_page(self, response):
        pass

