import scrapy
from scrapy import Request

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Quadient-Neopost-ISINK34-4135554T-Cartridge/dp/B08DVFCNL4',
    'https://www.amazon.com/Neopost-ISINK34-Warranty-Compatible-Cartridge/dp/B01LVYN122',
    'https://www.amazon.com/ecoPost-Compatible-Cartridge-Replacement-4135554T/dp/B07XJRK97X/ref=sr_1_6?gclid=CjwKCAjwv-GUBhAzEiwASUMm4hqPOBGlUtHOJ_QR2KzeTfaCDBySDGzQiuKzffk79T4gIKD_coN0nRoCmy0QAvD_BwE&hvadid=410047060241&hvdev=c&hvlocphy=9004392&hvnetw=g&hvqmt=b&hvrand=1074579371867825832&hvtargid=kwd-383471047184&hydadcr=11782_11121843&keywords=4135554t+neopost&qid=1654196896&sr=8-6']


    def parse(self, response):
        # Reading Title
        title = response.xpath('//span[contains(@class,"a-size-large product-title-word-break")]/text()').extract()
        print(title)

        # Reading Sale Price
        price = response.xpath('//div[contains(@class,"a-section a-spacing-none aok-align-center")]/span/span/text()').extract_first()
        print(price)
            
        # Reading Manufacturer
        producer = response.xpath('//a[contains(@id,"bylineInfo")]/text()').extract()
        print(producer)

        # Reading Description
        desc_tmp = response.xpath('//ul[contains(@class,"a-unordered-list a-vertical a-spacing-mini")]/li/span/text()').extract()
        #print(desc_tmp)
        description = "".join(desc_tmp[3:])
        print(description)
