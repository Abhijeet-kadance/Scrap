import scrapy.downloadermiddlewares.httpcompression as httpcompression

class ContentTypeFilterMiddleware(httpcompression.HttpCompressionMiddleware):

    def process_response(self, request, response, spider):
        content_type = response.headers.get('Content-Type', b'').decode('utf-8').lower()
        
        # Check if the content type is 'text/html'
        if 'text/html' not in content_type:
            spider.logger.info(f'Ignoring non-text/html content for URL: {response.url}')
            return None  # Return None to drop the response
        
        return super().process_response(request, response, spider)
