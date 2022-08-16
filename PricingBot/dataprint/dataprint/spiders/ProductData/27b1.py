import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '27_b1'  # change this first!!!
    allowed_domains = ['mindfulpostage']
    start_urls = [
        # IMINK 34
        'https://mindfulpostage.com/products/imink4hc-im-4-series-hi-capacity-ink-cartridge-genuine-compatible/'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()  #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//*[@id="add-item-form-template--14213914099798__main"]/div[1]/h1/text()').extract_first()
        print(title)
        # title = title.strip()

        # Reading Sale Price
        price = response.xpath('//*[@id="price-template--14213914099798__main"]/text()').extract_first()
        price = price.strip()[2:]
        print(price)

        # Reading Manufacturer
        producer = 'Hasler' # (response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/section[2]/div[1]/span/a/span/strong/text()').extract_first())

        # Reading Description
        description = response.xpath('//*[@id="description"]/div/p/span/text()').extract_first()
        #description = "".join(description[0:]).strip()

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



