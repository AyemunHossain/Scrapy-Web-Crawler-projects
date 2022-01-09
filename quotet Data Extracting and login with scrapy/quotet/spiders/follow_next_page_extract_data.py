
import scrapy
from ..items import QuotetItem


class LinkSpiderExDataNextPage(scrapy.Spider):
    """
    Follow the css page and extract data
    """

    name = "LinkSpiderExDataNextPage"
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