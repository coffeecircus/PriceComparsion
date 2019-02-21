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
            fb = open("/Users/coffeecircus/Desktop/PriceComparisonWebsite/SkincarePriceComparsion/result.txt","a+")
            fb.write(id+price+brand+'\n')
            fb.close()
        except:
            pass

        return item
