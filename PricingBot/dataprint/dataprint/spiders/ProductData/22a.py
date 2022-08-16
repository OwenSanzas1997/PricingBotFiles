import scrapy
import gspread
from datetime import datetime
from datetime import timedelta
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '22_a'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/Quadient-Neopost-ISINK34-4135554T-Cartridge/dp/B08DVFCNL4',
        'https://www.amazon.com/Neopost-ISINK34-Warranty-Compatible-Cartridge/dp/B01LVYN122',
        'https://www.amazon.com/ecoPost-Compatible-Cartridge-Replacement-4135554T/dp/B07XJRK97X/ref=sr_1_6?gclid=CjwKCAjwv-GUBhAzEiwASUMm4hqPOBGlUtHOJ_QR2KzeTfaCDBySDGzQiuKzffk79T4gIKD_coN0nRoCmy0QAvD_BwE&hvadid=410047060241&hvdev=c&hvlocphy=9004392&hvnetw=g&hvqmt=b&hvrand=1074579371867825832&hvtargid=kwd-383471047184&hydadcr=11782_11121843&keywords=4135554t+neopost&qid=1654196896&sr=8-6',
        'https://www.amazon.com//Neopost-ISINK34-Cartridge-Postage-Meters/dp/B01H63ZGTS/ref=ice_ac_b_dpb',
        'https://www.amazon.com//ecoPost-ECO34-Compatible-Cartridge-Replacement/dp/B009A3K6FM'
    ]

    def parse(self, response):
       
        # Reading Time
        now = datetime.now() #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url
        
        # Reading Title
        title = response.xpath('//span[contains(@class,"a-size-large product-title-word-break")]/text()').extract_first()
        title = title.strip()
         
        # Reading Sale Price
        price = response.xpath('//div[contains(@class,"a-section a-spacing-none aok-align-center")]/span/span/text()').extract_first()
        price = price[1:]
        
        # Reading Manufacturer
        producer = (response.xpath('//a[contains(@id,"bylineInfo")]/text()').extract_first())[7:]
        
        # Reading Description
        desc_tmp = response.xpath('//ul[contains(@class,"a-unordered-list a-vertical a-spacing-mini")]/li/span/text()').extract()
        description = "".join(desc_tmp[3:]).strip()

        # Check if price is null
        if price == None:
            price = "nan"

           
        product =  {
            "time": time,
            "link": link,
            "titles": title,        
            "prices": price,
            "producers":producer,
            "description":description       
        }

        # writing to google sheets

        # data_info is our data set, including time, link, title, producer, description and price
        data_info = [str(product['time']), str(product['link']), str(product['titles']),
                     str(product['producers']), str(product['description']), str(product['prices'])]
        print(data_info)

        sheet_loader.sheet_loader(data_info,  A_Spider.name[0:2])
 
