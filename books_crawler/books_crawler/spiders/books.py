from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse

class BooksSpider(CrawlSpider):
    name = "books"
    allowed_domains = ["ernet.in"]
    start_urls = ["https://ernet.in"]

    # file_extensions_to_exclude = ['.pdf', '.doc', '.zip']
    # exclude_patterns = '|'.join([f'.*{ext}' for ext in file_extensions_to_exclude])


    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)

    def parse_page(self, response):
         yield {'URL': response.url}
        
        

            
