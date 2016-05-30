# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
from testpro.items import TestproItem
from bs4 import BeautifulSoup

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

		vendors = []
		for ii in response.xpath("//div[@class='offer-row row']").extract():
			vendordict = {}
			soup = BeautifulSoup(ii)
			vendorname = soup.find('div',{'class':'shop-logo'}).find('img').get('title')
			prize = soup.find('span',{'class':'offer-price'}).text
			vendorlink =  soup.find('div',{'class':'shop-logo'}).find('a').get('href')
			vendordict = {'vendorname':vendorname,'prize':prize,'link':vendorlink}
			vendors.append(vendordict)

			print "*"*100
		item['vendors'] = vendors

		yield item
