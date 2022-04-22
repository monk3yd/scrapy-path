# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongodbPipeline(object):
    collection_name = "best_movies"
    # @classmethod  # Let you access values from settings.py
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        # logging.warning("SPIDER OPENED FROM PIPELINE")
        self.client = pymongo.MongoClient("")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        # logging.warning("SPIDER CLOSED FROM PIPELINE")
        self.client.close()

    def process_item(self, item, spider):
        # Insert into db
        self.db[self.collection_name].insert(item)
        return item
