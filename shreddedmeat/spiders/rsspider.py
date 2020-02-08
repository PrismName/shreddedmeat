# -*- coding: utf-8 -*-
import scrapy


class RsspiderSpider(scrapy.Spider):
    name = 'rsspider'
    allowed_domains = []
    start_urls = []

    def __init__(self, domain=None, *args, **kwargs):
        super(RsspiderSpider, self).__init__(*args, **kwargs)

        if domain is None:
            print("[*] Error : You must provide a domain.")
            return

        self.domain = domain
        self.base_url = f'http://{self.domain}'
        self.allowed_domains.append(self.domain)
        self.start_urls.append(self.base_url)

    def parse(self, response):
        pass
