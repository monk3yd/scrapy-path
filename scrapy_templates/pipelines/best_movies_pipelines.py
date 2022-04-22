# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
import sqlite3


class MongodbPipeline(object):
    collection_name = "best_movies"
    # @classmethod  # Let you access values from settings.py
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        # logging.warning("SPIDER OPENED FROM PIPELINE")
        self.client = pymongo.MongoClient("mongodb+srv://monk3yd:raftel12345@cluster0.z6pty.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    def close_spider(self, spider):
        # logging.warning("SPIDER CLOSED FROM PIPELINE")
        self.client.close()

    def process_item(self, item, spider):
        # Insert into db
        self.db[self.collection_name].insert(item)
        return item


class SQLlitePipeline(object):

    def open_spider(self, spider):
        # Create and connect to db
        self.connection = sqlite3.connect("imdb.db")
        self.db = self.connection.cursor()
        # Create table
        try:
            self.db.execute('''
                CREATE TABLE best_movies(
                    title TEXT,
                    year TEXT,
                    duration TEXT,
                    genre TEXT,
                    rating TEXT,
                    movie_url TEXT
                );
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # Insert into db
        self.db.execute('''
            INSERT INTO best_movies (title, year, duration, genre, rating, movie_url) VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            item["title"],
            item["year"],
            item["duration"],
            item["genre"],
            item["rating"],
            item["movie_url"]
        ))
        self.connection.commit()
        return item

