import scrapy
from scrapy import Request

class B4Spider(scrapy.Spider):
    name = 'B4'
    allowed_domains = ['emeraldrecycle']

    # B4 link
    start_urls = ['https://www.emeraldrecycle.com/Neopost-ISINK34-Surejet-4135554T-Red-Ink-Cartridge_p_12.html']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//h1/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = response.xpath('//div[contains(@class,"yourprice price")]/span/text()').extract_first()
        # price = response.xpath('//div[contains(@class,"retailprice")]/span/text()').extract_first()
        print(price)
            
        # Reading Manufacturer
        # manufacturer's name only avaliable in image, hard coded
        producer = "Emerald Recycle"
        print(producer)

        # Reading Description
        desc= response.xpath('//div[contains(@itemprop,"description")]/span[1]/text()').extract_first() + response.xpath('//div[contains(@itemprop,"description")]/span[2]/text()').extract_first() + response.xpath('//div[contains(@itemprop,"description")]/span[3]/text()').extract_first()
        print(desc)

    
