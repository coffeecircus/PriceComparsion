# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SkincarepricecomparsionItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    brand = scrapy.Field()
    photo = scrapy.Field()
    product_name = scrapy.Field()
    id = scrapy.Field()
    in_stock = scrapy.Field()
    offer = scrapy.Field()
    img_url = scrapy.Field()
