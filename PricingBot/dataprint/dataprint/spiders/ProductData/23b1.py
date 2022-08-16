import scrapy
import gspread
from datetime import datetime
from datetime import timedelta
from oauth2client.service_account import ServiceAccountCredentials
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '23_b1'
    allowed_domains = ['postageink']

    # B3 link
    start_urls = ['https://www.postageink.com/ISINK2-Red-Ink-Cartridge-p/isink2-red-ink-cartridge.htm']

    def parse(self, response):
        # Reading Time
        now = datetime.now()
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//font/span/text()').extract_first()
        print(title)

        # Reading Sale Price
        price = "$" + response.xpath(
            '//font[contains(@class,"pricecolor colors_productprice")]/div/b/span/text()').extract_first()
        price = price[1:]
        print(price)

        # Reading Manufacturer
        producer = (response.xpath(
            '//font[contains(@class,"pricecolor colors_productprice")]/div/b/font/b/text()').extract_first())[0:10]
        print(producer)

        # Reading Description
        desc_tmp = response.xpath('//span[contains(@id,"product_description")]/text()').extract()
        desc = "".join(desc_tmp[0:4])
        desc = desc.strip()  # output include "/n", code here to remove it
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

