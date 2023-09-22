import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['https://bhashanet.in']

    def start_requests(self):
        urls = ["https://bhashanet.in"]

        for url in urls:
           yield scrapy.Request(url = url, callback = self.parse)


           # Get anchor tags
    def parse(self, response):
      
        # Extra feature to get title
        title = response.css('title::text').extract_first() 
        
        # Get anchor tags
        links = response.css('a::attr(href)').extract()     
        
        for link in links:
            yield 
            {
                'title': title,
                'links': link
            }
            
            if 'geeksforgeeks' in link:         
                yield scrapy.Request(url = link, callback = self.parse)
    # def parse(self, response):
        # QUOTE_SELECTOR = 'a'
        # TEXT_SELECTOR = '.text::text'
        # # AUTHOR_SELECTOR = '.author::text'
        # # ABOUT_SELECTOR = '.author + a::attr("href")'
        # # TAGS_SELECTOR = '.tags > .tag::text'
        # NEXT_SELECTOR = '.next a::attr("href")'

        # for quote in response.css(QUOTE_SELECTOR):
        #     yield {
        #         'text': quote.css(TEXT_SELECTOR).extract_first(),
        #         # 'author': quote.css(AUTHOR_SELECTOR).extract_first(),
        #         # 'about': 'https://quotes.toscrape.com' + 
        #         #         quote.css(ABOUT_SELECTOR).extract_first(),
        #         # 'tags': quote.css(TAGS_SELECTOR).extract(),
        #     }

        # next_page = response.css(NEXT_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #     )