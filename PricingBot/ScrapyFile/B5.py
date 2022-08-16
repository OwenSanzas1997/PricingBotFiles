import scrapy
from scrapy import Request

class B5Spider(scrapy.Spider):
    name = 'B5'
    allowed_domains = ['postagemeterinkcartridges']

    # B5 link
    start_urls = ['https://www.postagemeterinkcartridges.com/quadient-compatible-isink34-red-ink-cartridge-for-is300-in360-is400-in600/']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//h1/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = response.xpath('//span[contains(@class,"price price--withoutTax")]/text()').extract_first()
        print(price)
            
        # Reading Manufacturer
        producer = (response.xpath('//span[contains(@itemprop,"name")]/strong/text()').extract_first())[0:8]
        print(producer)

        # Reading Description
        desc= response.xpath('//div[contains(@itemprop,"description")]/p/span/text()').extract_first()
        print(desc)

    