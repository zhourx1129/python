import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response)
