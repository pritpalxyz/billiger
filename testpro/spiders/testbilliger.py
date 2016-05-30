# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
from testpro.items import TestproItem

class TestbilligerSpider(scrapy.Spider):
	name = "testbilliger"
	start_urls = ['http://www.billiger.de/']


	def __init__(self):
		self.searchString = dict(searchstring="Samsung ME733K",search="1",stat="1")

	def parse(self, response):
		return [FormRequest.from_response(response,
			formdata=self.searchString,
			callback=self.after_search, dont_filter=True)]

	def after_search(self,response):
		item = TestproItem()
		item['title'] = response.xpath("//h1/text()").extract()[0]
		prize = response.xpath("//span[@class='price']/text()").extract()[0]
		item['rating'] = response.xpath("//div[@class='star-count']/text()").extract()[0]
		item['pageurl'] = response.url
		prize = prize.replace("\r","")
		prize = prize.replace("\n","")
		item['prize'] = prize

		yield item
