import scrapy

from urllib.parse import urljoin 
from scrapy.selector import Selector
from shreddedmeat.items import UrlItem


class VulnspiderSpider(scrapy.Spider):
    name = 'vulnspider'
    allowed_domains = []
    start_urls = []
    vurls = []

    def __init__(self, domain=None, *args, **kwargs):
        super(VulnspiderSpider, self).__init__(*args, **kwargs)

        if domain is None:
            return

        self.domain = domain
        self.base_url = f'http://{self.domain}'
        self.allowed_domains.append(self.domain)
        self.start_urls.append(self.base_url)

    def parse(self, response):
        item = UrlItem()

        item['url'] = response.url

        selector = Selector(response)

        urls_set = set()

        for uri in selector.xpath('//a/@href').extract():
            tmp_url = urljoin(response.url, uri)
            if tmp_url not in urls_set:
                urls_set.add(tmp_url)

        for url in urls_set:
            if url not in VulnspiderSpider.vurls:
                VulnspiderSpider.vurls.append(url)
                yield scrapy.Request(url=url, callback=self.parse)

        return item
