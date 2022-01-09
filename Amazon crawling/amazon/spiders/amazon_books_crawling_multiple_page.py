import scrapy
from scrapy import item
from scrapy import Request

class AmazonBooksSpider2(scrapy.Spider):
    name = 'AmazonBooksSpider2'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/gp/new-releases/books/ref=zg_bsnr_pg_2?ie=UTF8&pg=1']
        
    def parse(self, response):
        
        all_div = response.css('li.zg-item-immersion')
        for div in all_div:
            title = str(
                div.css("div.p13n-sc-line-clamp-1::text").get()).strip()
            author = div.css("a.a-link-child::text").get()
            if not author:
                author = div.css('span.a-color-base::text').get()
            price = div.css('span.p13n-sc-price::text').get()
            img = ','.join(div.css('div.a-section img::attr(src)').extract())

            item['bookName'] = title
            item['bookAuthor'] = author
            item['bookPrice'] = price
            item['bookImageLink'] = img
            yield item

        # next_page = response.css('div.a-text-center li.a-last a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)