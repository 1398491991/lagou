#coding=utf-8
import MySQLdb
from ..settings import DB_CONFIG
import scrapy

class BaseSpider(scrapy.Spider):
    conn=MySQLdb.connect(**DB_CONFIG)
    name = None