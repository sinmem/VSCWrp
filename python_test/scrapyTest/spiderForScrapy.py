import scrapy
import re
import response


class scrapySpider(scrapy.Spider):
    name-'scrapyS'
    start_url - []

    def parse(self, response):
        for hre in response.css('a::attr(href)').extract:
            try:
                stockecode=re.findall(r'[s][z|h]\d{6}'.hre)
            except expression as identifier:
                pass
