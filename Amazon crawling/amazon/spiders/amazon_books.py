import scrapy
from scrapy import item



class AmazonBooksSpider(scrapy.Spider):
    name = 'AmazonBooksSpider'
    start_urls = [
        'https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2']

    def parse(self, response):
        all_div = response.css('li.zg-item-immersion')
        print(all_div)
        for div in all_div:
            title = str(div.css("div.p13n-sc-line-clamp-1::text").get()).strip()
            author = div.css("a.a-link-child::text").get()
            if not author:
                author = div.css('span.a-color-base::text').get()
            price = div.css('span.p13n-sc-price::text').get()
            img = ','.join(div.css('div.a-section img::attr(src)').extract())
            print(f"----Title:{title},Author:{author},Price:{price},img:{img}----")
        
        yield None
