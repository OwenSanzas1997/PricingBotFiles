import scrapy
from scrapy import Request

class B1Spider(scrapy.Spider):
    name = 'B1'
    allowed_domains = ['americanmailingsolutions']

    # B1 link
    start_urls = ['https://americanmailingsolutions.net/products/neopost-isink34-inink67-ink-cartridge-4135554t?_pos=2&_sid=26aa152b3&_ss=r']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//h1/text()').extract_first()
        title = title.strip()   # output include "/n", code here to remove it
        print(title)

        # Reading Sale Price
        price = response.xpath('//div[contains(@class,"price--main")]/span[2]/text()').extract_first()
        price = price.strip()   # output include "/n", code here to remove it
        print(price)
            
        # Reading Manufacturer
        producer = response.xpath('//div[contains(@class,"product-vendor")]/a/text()').extract_first()
        print(producer)

        # Reading Description
        # content included in seperate d
        desc = response.xpath('//div[contains(@class,"product-description rte")]/p/span/text()').extract_first() + response.xpath('//div[contains(@class,"product-description rte")]/p/span/strong/text()').extract_first()
        print(desc)

    
