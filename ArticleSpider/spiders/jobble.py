# -*- coding: utf-8 -*-
import scrapy


class JobbleSpider(scrapy.Spider):
    name = 'jobble'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/113429/']

    def parse(self, response):
        re_selector = response.xpath('//*[@id="post-113429"]/div[2]/p/text()').extract()[0].strip().replace(' ·', '')
        pass
