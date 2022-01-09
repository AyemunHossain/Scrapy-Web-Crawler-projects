import scrapy
from scrapy.http import FormRequest
from ..items import QuotetItem

class LinkSpiderLogin(scrapy.Spider):
    """
    Remotely login through crawler
    """
    name = "LinkSpiderLogin"
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response, **kwargs):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'afasdfsdfddfdsaf',
            'password':'asfdffsfsdfsdf',},callback=self.start_crawling_after_login)

    def start_crawling_after_login(self,response):
        items = QuotetItem()
        all_div = response.css('div.quote')

        for div in all_div:
            title = div.css('span.text::text').extract()
            author = div.css('.author::text').extract()
            tag = div.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items