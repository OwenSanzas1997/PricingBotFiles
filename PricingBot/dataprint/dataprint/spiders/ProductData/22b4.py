import scrapy
import gspread
from datetime import datetime
from datetime import timedelta
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class B_Spider(scrapy.Spider):
    name = '22_b4'
    allowed_domains = ['emeraldrecycle']

    # B4 link
    start_urls = ['https://www.emeraldrecycle.com/Neopost-ISINK34-Surejet-4135554T-Red-Ink-Cartridge_p_12.html']

    def parse(self, response):
         # Reading Time
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//h1/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = response.xpath('//div[contains(@class,"yourprice price")]/span/text()').extract_first()
        # price = response.xpath('//div[contains(@class,"retailprice")]/span/text()').extract_first()
        price = price[1:]
        print(price)
            
        # Reading Manufacturer
        # manufacturer's name only avaliable in image, hard coded
        producer = "Emerald Recycle"
        print(producer)

        # Reading Description
        desc= response.xpath('//div[contains(@itemprop,"description")]/span[1]/text()').extract_first() + response.xpath('//div[contains(@itemprop,"description")]/span[2]/text()').extract_first() + response.xpath('//div[contains(@itemprop,"description")]/span[3]/text()').extract_first()
        print(desc)

         # Check if price is null
        if price == None:
            price = "nan"


        product =  {
            "time": time,
            "link": link,
            "titles": title,        
            "prices": price,
            "producers":producer,
            "description":desc       
        }
        # writing to google sheets

        # data_info is our data set, including time, link, title, producer, description and price
        data_info = [str(product['time']), str(product['link']), str(product['titles']),
                      str(product['producers']), str(product['description']), str(product['prices'])]
        print(data_info)

        sheet_loader.sheet_loader(data_info, B_Spider.name[0:2])

