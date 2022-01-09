
import scrapy

class GetCSRFtoken(scrapy.Spider):
    """
    From login page extract the csrf token value
    """

    name = "GetCSRFtoken"
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response, **kwargs):
        token = response.css('form input::attr(value)').extract_first()
        print(token)