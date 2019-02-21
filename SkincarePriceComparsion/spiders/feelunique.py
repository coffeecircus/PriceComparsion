# -*- coding: utf-8 -*-
import scrapy
from SkincarePriceComparsion.items import SkincarepricecomparsionItem


class FeeluniqueSpider(scrapy.Spider):
    name = 'feelunique'
    allowed_domains = ['lookfantastic.com']
    start_urls = ["https://www.lookfantastic.com/health-beauty/face/view-all-skincare.list?pageNumber=1"]

    def parse(self, response):
        item = SkincarepricecomparsionItem()
        # contents = response.xpath("//*[@id='divSearchResults']/div[1]/div[1]/div/span")
        # id = contents.xpath('@data-product-id').extract()
        # price = contents.xpath('@data-product-price').extract()
        # brand = contents.xpath('@data-product-title').extract()
        products = response.xpath("//*[@id='divSearchResults']/child::div/child::div/div/span")
        for product in products:
            id = product.xpath('@data-product-id').extract()
            price = product.xpath('@data-product-price').extract()
            brand = product.xpath('@data-product-title').extract()
            print()
            item["id"] = id
            item["price"] = price
            item["brand"] = brand
            yield item

        #calculate page numbers
        page_number_location = response.xpath("//*[@id='home']/div[1]/section/div/section/section/section[2]/div/div/div[5]/div/nav")
        page_number = int(page_number_location.xpath("@data-total-pages").extract()[0])

        #go to next page
        for i in range(2,page_number+1):
            url = "https://www.lookfantastic.com/health-beauty/face/view-all-skincare.list?pageNumber={}".format(str(i))
            yield scrapy.http.Request(url, callback=self.parse)
