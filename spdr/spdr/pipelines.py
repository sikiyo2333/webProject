# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import spdr.settings


class SpdrPipeline(object):
    def process_item(self, item, spider):
        return item


class NewsPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        logging.debug(query)
        return item
        # insert the data to databases

    def _conditional_insert(self, tx, item):
        parms = (item['myurl'], item['picture'], item[
            'title'], item['date'], item['summary'])
        sql = "insert into news values('%s','%s','%s','%s','%s') " % parms
        # logging.debug(sql)
        tx.execute(sql)

