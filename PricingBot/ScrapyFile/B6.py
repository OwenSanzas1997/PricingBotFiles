import scrapy
from scrapy import Request

class B65pider(scrapy.Spider):
    name = 'B6'
    allowed_domains = ['midwestmailingsupplies']

    # B6 link
    start_urls = ['https://www.midwestmailingsupplies.com/neopost-meter-ink-isink34/']

    def parse(self, response):
        # Reading Title
        title = response.xpath('//h1/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = (response.xpath('//span[contains(@class,"price price--withoutTax")]/text()').extract_first())[7:]
        print(price)
            
        # Reading Manufacturer
         # manufacturer's name only avaliable in image, hard coded
        producer = "MIDWEST"
        print(producer)

        # Reading Description
        desc= response.xpath('//div[contains(@class,"config-value")]/text()').extract_first()
        print(desc)


    