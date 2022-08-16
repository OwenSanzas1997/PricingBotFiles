import scrapy
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class B_Spider(scrapy.Spider):
    name = '22_b2'
    allowed_domains = ['ldproducts']

    # B2 link
    start_urls = ['https://www.ldproducts.com/compatible-neopost-4135554t-red-ink-cartridge-4135554t']

    def parse(self, response):
         # Reading Time
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//h1/span/text()').extract_first()
        title = title.strip()
        print(title)

        # Reading Sale Price
        price = response.xpath('//span[contains(@class,"special-price")]/span/span[2]/span/text()').extract_first()
        # price = response.xpath('//div[contains(@class,"price-box price-final_price")]/span/span[2]/span/text()').extract_first()
        price = price[1:]
        print(price)
            
        # Reading Manufacturer
        producer = response.xpath('//table[contains(@class,"data table additional-attributes")]/tbody/tr[6]/td/text()').extract_first()
        print(producer)

        # Reading Description
        desc = response.xpath('//div[contains(@class,"product attribute description")]/div/text()').extract_first()
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

