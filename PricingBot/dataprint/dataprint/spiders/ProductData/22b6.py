import scrapy
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class B_Spider(scrapy.Spider):
    name = '22_b6'
    allowed_domains = ['midwestmailingsupplies']

    # B6 link
    start_urls = ['https://www.midwestmailingsupplies.com/neopost-meter-ink-isink34/']

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
        price = (response.xpath('/html/body/div[4]/div[1]/div/div[1]/section/div[2]/div[1]/div/div[3]/span[1]/text()').extract_first())[7:]
        price = price[1:]
        print(price)
            
        # Reading Manufacturer
         # manufacturer's name only avaliable in image, hard coded
        producer = "MIDWEST"
        print(producer)

        # Reading Description
        desc= response.xpath('//div[contains(@class,"config-value")]/text()').extract_first()
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


    