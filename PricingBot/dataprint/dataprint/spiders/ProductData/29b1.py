import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '29_b1'  # change this first!!!
    allowed_domains = ['inkcartridges']
    start_urls = [
        # WJ69INK
        'https://www.inkcartridges.com/remanufactured-hasler-wj69ink-red-ink-cartridge/'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()  #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[1]/h1/span/text()').extract_first()
        title = title.strip()

        # Reading Sale Price
        price = response.xpath(
            '//*[@id="product-price-51690"]/span/text()').extract_first()
        price = price[1:]
        print(price)

        # Reading Manufacturer
        producer = (response.xpath(
            '//*[@id="product-attribute-specs-table"]/tbody/tr[9]/td/text()').extract_first())

        # Reading Description
        desc = response.xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div/text()').extract_first()
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



