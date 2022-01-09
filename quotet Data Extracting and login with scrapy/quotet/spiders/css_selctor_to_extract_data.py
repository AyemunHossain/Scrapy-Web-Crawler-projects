
import scrapy
from ..items import QuotetItem


class LinkSpider2(scrapy.Spider):
    """
    Follow the css page and extract data
    """

    name = "LinkSpider2"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
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

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class LinkSpider3(scrapy.Spider):
    """
    Follow the next page and extract data
    """

    name = "LinkSpider3"
    nextPageNumber = 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response, **kwargs):
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

        #next_page = response.css('li.next a::attr(href)').get()

        next_page = f"http://quotes.toscrape.com/page/{self.nextPageNumber}/"
        if self.nextPageNumber < 11:
            self.nextPageNumber += 1
            yield response.follow(next_page, callback=self.parse)
