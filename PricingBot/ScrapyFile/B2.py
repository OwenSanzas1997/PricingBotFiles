import scrapy
from scrapy import Request

class B2Spider(scrapy.Spider):
    name = 'B2'
    allowed_domains = ['ldproducts']

    # B2 link
    start_urls = ['https://www.ldproducts.com/compatible-neopost-4135554t-red-ink-cartridge-4135554t']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//h1/span/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = response.xpath('//span[contains(@class,"special-price")]/span/span[2]/span/text()').extract_first()
        # price = response.xpath('//div[contains(@class,"price-box price-final_price")]/span/span[2]/span/text()').extract_first()
        print(price)
            
        # Reading Manufacturer
        producer = response.xpath('//table[contains(@class,"data table additional-attributes")]/tbody/tr[6]/td/text()').extract_first()
        print(producer)

        # Reading Description
        desc = response.xpath('//div[contains(@class,"product attribute description")]/div/text()').extract_first()
        print(desc)

    
