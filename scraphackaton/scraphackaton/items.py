# -*- coding: utf-8 -*-
import scrapy

class ScraphackatonItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
