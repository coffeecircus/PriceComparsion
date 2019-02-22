# -*- coding: utf-8 -*-
import scrapy
from SkincarePriceComparsion.items import SkincarepricecomparsionItem


class DebenhamsSpider(scrapy.Spider):
    name = 'debenhams'
    allowed_domains = ['debenhams.ie']
    start_urls = ['https://www.debenhams.ie/beauty/skin-care']

    def parse(self, response):
        item = SkincarepricecomparsionItem()

        products = response.css("div.c-product-tile")

        for product in products:

         brand = product.css("span[itemprop = 'brand']::text").extract()[0]
         product_name = product.css("span[itemprop = 'name']::text").extract()[0]
         img_url = product.css("a.u-flex-none::attr(href)").extract()[0]
         price = product.css("span[itemprop = 'price']::text").extract()[0]
         in_stock = product.css("link[itemprop = 'availability']::attr(href)").extract()[0]
         offer = product.css(".dbh-save::text").extract()

         item["brand"] = brand
         item["offer"] = offer
         item["in_stock"] = in_stock.split("/")[-1] == "InStock"
         item["product_name"] = product_name
         item["price"] = ''.join(price.split()) if price.startswith("€") else "€" + ''.join(price.split())
         item["img_url"] = "https://debenhams.scene7.com/is/image/Debenhams/{}?wid=333&amp;hei=333&amp;qlt=80&amp;op_usm=1.1,0.5,0,0&amp;fmt=pjpeg".format(img_url.split("_")[-2])

         yield item

