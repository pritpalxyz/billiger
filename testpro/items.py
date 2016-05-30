# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestproItem(scrapy.Item):
	title = scrapy.Field()
	prize = scrapy.Field()
	rating = scrapy.Field()
	pageurl = scrapy.Field()
	vendors = scrapy.Field()
