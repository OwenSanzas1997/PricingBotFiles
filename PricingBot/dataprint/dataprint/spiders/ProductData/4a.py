import scrapy
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '4_a'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/Compatible-Pitney-Cartridge-Postage-Machine/dp/B01N11YBS5',
        'https://www.amazon.com/Pitney-Compatible-Cartridge-Postage-Machine/dp/B07934TPV1'
        #'https://www.amazon.com/797-M-Red-Cartridge-Mailstation2TM-K7M0/dp/B09J6R8614',
        #'https://www.amazon.com/NuPost-NPTK700-Replacement-Mailstation-Mailstation2/dp/B001CE4XA6'
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
        price = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]/text()').extract_first()
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

        sheet_loader.sheet_loader(data_info, A_Spider.name[0])



