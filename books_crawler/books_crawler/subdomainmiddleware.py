import scrapy
from urllib.parse import urlparse
import scrapy.downloadermiddlewares.httpcompression as httpcompression
# class SubdomainFilterMiddleware:

#     def __init__(self, allowed_domains):
#         self.allowed_domains = [d.lower() for d in allowed_domains]

#     @classmethod
#     def from_crawler(cls, crawler, *args, **kwargs):
#         middleware = cls(crawler.settings.get('ALLOWED_DOMAINS'))
#         return middleware

#     def process_request(self, request, spider):
#         parsed_url = urlparse(request.url)
#         domain = parsed_url.netloc.lower()
#         if domain not in self.allowed_domains:
#             raise scrapy.exceptions.IgnoreRequest(f"URL's domain ({domain}) is not allowed.")

# class SubdomainFilterMiddleware(httpcompression.HttpCompressionMiddleware):

#     def __init__(self, allowed_domain):
#         self.allowed_domain = allowed_domain.lower()

#     def process_request(self, request, spider):
#         parsed_url = urlparse(request.url)
#         domain = parsed_url.netloc.lower()

#         if domain != self.allowed_domain:
#             spider.logger.info(f'Ignoring subdomain URL: {request.url}')
#             return None


class SubdomainFilterMiddleware:

    def process_request(self, request, spider):
        # Get the netloc (domain) from the request URL
        netloc = urlparse(request.url).netloc.lower()

        # Get the main domain from the start URL
        main_domain = urlparse(spider.start_urls[0]).netloc.lower()

        # Check if the netloc is not equal to the main domain
        if netloc != main_domain:
            raise scrapy.exceptions.IgnoreRequest(f"URL's subdomain ({netloc}) is not allowed.")