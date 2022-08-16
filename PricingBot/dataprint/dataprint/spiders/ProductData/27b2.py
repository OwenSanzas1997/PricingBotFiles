import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '27_b2'  # change this first!!!
    allowed_domains = ['postagemeterinkcartridges']
    start_urls = [
        # Hasler IMINK2
        'https://www.postagemeterinkcartridges.com/hasler-imink4hc-compatible-high-capacity-ink-cartridge/'
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
        desc = response.xpath('//*[@id="product_description"]/text()').extract_first()
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



