import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '21_b1'  # change this first!!!
    allowed_domains = ['postagemeterinkcartridges']
    start_urls = [
        # NeoPost IS6000
        'https://www.postagemeterinkcartridges.com/neopost-is6000-compatible-red-ink-tank/'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()  #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/section[2]/div[1]/h1/text()').extract_first()
        # title = title.strip()

        # Reading Sale Price
        price = response.xpath(
            '//span[contains(@class,"price price--withoutTax")]/text()').extract_first()
        price = price[1:]
        print(price)

        # Reading Manufacturer
        producer = (response.xpath(
            '/html/body/div[2]/div[2]/div[1]/div[1]/section[2]/div[1]/span/a/span/strong/text()').extract_first())

        # Reading Description
        description = response.xpath(
            '/html/body/div[2]/div[2]/div[1]/div[1]/section[2]/div[1]/div[6]/div/p/span/text()').extract()
        description = "".join(description[0:]).strip()

        # Check if price is null
        if price == None:
            price = "nan"

        product = {
            "time": time,
            "link": link,
            "titles": title,
            "prices": price,
            "producers": producer,
            "description": description
        }

        # writing to google sheets

        # data_info is our data set, including time, link, title, producer, description and price
        data_info = [str(product['time']), str(product['link']), str(product['titles']),
                     str(product['producers']), str(product['description']), str(product['prices'])]
        print(data_info)

        sheet_loader.sheet_loader(data_info, A_Spider.name[0:2])



