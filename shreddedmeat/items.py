# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#class VulhubItem(scrapy.Item):
#    name = scrapy.Field()
#    level = scrapy.Field()
#    vuln_link = scrapy.Field()
#    payload = scrapy.Field()
#    response_content = scrapy.Field()
#    request_content = scrapy.Field()


class UrlItem(scrapy.Item):
    url = scrapy.Field()


class ShreddedmeatItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
