import scrapy
from scrapy import Request

class B3Spider(scrapy.Spider):
    name = 'B3'
    allowed_domains = ['postageink']

    # B3 link
    start_urls = ['https://www.postageink.com/ISINK34-Red-Ink-Cartridge-p/isink34-red-ink-cartridge.htm']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//font/span/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = "$"+response.xpath('//font[contains(@class,"pricecolor colors_productprice")]/div/b/span/text()').extract_first()
        print(price)
            
        # Reading Manufacturer
        producer = (response.xpath('//font[contains(@class,"pricecolor colors_productprice")]/div/b/font/b/text()').extract_first())[0:10]
        print(producer)

        # Reading Description
        desc_tmp = response.xpath('//span[contains(@id,"product_description")]/text()').extract()
        desc = "".join(desc_tmp[0:4])
        desc = desc.strip()   # output include "/n", code here to remove it
        print(desc)

    