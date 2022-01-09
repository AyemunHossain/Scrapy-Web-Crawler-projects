# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    bookName = scrapy.Field()
    bookAuthor = scrapy.Field()
    bookPrice = scrapy.Field()
    bookImageLink = scrapy.Field()
    
    
