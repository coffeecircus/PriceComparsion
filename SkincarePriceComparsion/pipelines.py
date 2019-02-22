# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SkincarepricecomparsionPipeline(object):
    def process_item(self, item, spider):
        try:
            id = str(item["id"])
            price = str(item["price"])
            brand = str(item["brand"])
            product_name = str(item["product_name"])
            in_stock = str(item["in_stock"])
            offer = str(item["offer"])

            fb = open("result.txt","a+")
            fb.write(id+price+brand+product_name+in_stock+offer+'\n')
            fb.close()
        except:
            pass

        return item
