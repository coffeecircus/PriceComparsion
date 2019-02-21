# -*- coding: utf-8 -*-
import scrapy
from SkincarePriceComparsion.items import SkincarepricecomparsionItem


class LookfantasticSpider(scrapy.Spider):
    name = 'lookfantastic'
    allowed_domains = ['lookfantastic.com']
    start_urls = ["https://www.lookfantastic.com/health-beauty/face/view-all-skincare.list?pageNumber=1"]

    def parse(self, response):
        item = SkincarepricecomparsionItem()
        # contents = response.xpath("//*[@id='divSearchResults']/div[1]/div[1]/div/span")
        # id = contents.xpath('@data-product-id').extract()
        # price = contents.xpath('@data-product-price').extract()
        # brand = contents.xpath('@data-product-title').extract()
        products = response.xpath("//*[@id='divSearchResults']/child::div/child::div/div")
        for product in products:
            id = product.xpath("span").xpath('@data-product-id').extract()[0]
            price = product.xpath("span").xpath('@data-product-price').extract()[0]
            brand = product.xpath("span").xpath('@data-product-brand').extract()[0]
            product_name = product.xpath("span").xpath('@data-product-title').extract()[0]
            in_stock = product.xpath("div[2]/a/text()").extract()[0] == "Add to basket"
            offer = product.xpath("div[2]/div[1]/div/div/a/div/p/text()").extract()
            img_url = product.xpath("div[1]/div/a[1]/img").xpath("@src").extract()[0]

            if offer != []:
                offer = offer[0].strip()
            else:
                offer = ""

            item["id"] = id
            item["price"] = price
            item["brand"] = brand
            item["product_name"] = product_name
            item["in_stock"] = in_stock
            item["offer"] = offer
            item["img_url"] = img_url
            yield item

        #calculate page numbers
        page_number_location = response.xpath("//*[@id='home']/div[1]/section/div/section/section/section[2]/div/div/div[5]/div/nav")
        page_number = int(page_number_location.xpath("@data-total-pages").extract()[0])

        #go to next page
        for i in range(2,page_number+1):
            url = "https://www.lookfantastic.com/health-beauty/face/view-all-skincare.list?pageNumber={}".format(str(i))
            yield scrapy.http.Request(url, callback=self.parse)
