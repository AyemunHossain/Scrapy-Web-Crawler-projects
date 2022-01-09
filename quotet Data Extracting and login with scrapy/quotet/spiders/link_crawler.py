import scrapy

class LinkSpider1(scrapy.Spider):
    """To list all the hadings of the website
    """
    name = "LinkSpider1"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    
    def parse(self, response, **kwargs):
        title = response.xpath("//div[@class='col-md-8']/div[@class='quote']/span[@class='text']/text()").extract()
        yield {"Title" :title}
        
