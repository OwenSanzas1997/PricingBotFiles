import scrapy
import gspread
from datetime import datetime
from datetime import timedelta
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '16_b1'
    allowed_domains = ['americanmailingsolutions']

    # B1 link
    start_urls = [
        'https://americanmailingsolutions.net/products/neopost-ij25ink-ink-cartridge-3300028d'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/h1/text()').extract_first()
        title = title.strip()  # output include "/n", code here to remove it
        print(title)

        # Reading Sale Price
        price = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div[2]/div/div[2]/span[2]/text()').extract_first()
        price = price.strip()  # output include "/n", code here to remove it
        price = price[1:]
        print(price)

        # Reading Manufacturer
        producer = response.xpath('//div[contains(@class,"product-vendor")]/a/text()').extract_first()
        print(producer)

        # Reading Description
        # content included in seperate d
        desc = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/p[1]/text()[1]').extract_first()
        print(desc)

        # Check if price is null
        if price == None:
            price = "nan"

        product = {
            "time": time,
            "link": link,
            "titles": title,
            "prices": price,
            "producers": producer,
            "description": desc
        }
        # writing to google sheets

        # data_info is our data set, including time, link, title, producer, description and price
        data_info = [str(product['time']), str(product['link']), str(product['titles']),
                     str(product['producers']), str(product['description']), str(product['prices'])]
        print(data_info)

        sheet_loader.sheet_loader(data_info, A_Spider.name[0:2])




