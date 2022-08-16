import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '29_b2'  # change this first!!!
    allowed_domains = ['compandsave']
    start_urls = [
        # WJ69INK
        'https://www.compandsave.com/hasler/4124705s-ink-cartridge-red/'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()  #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//*[@id="maincontent"]/div[1]/div/h1/text()').extract_first()
        title = title.strip()

        # Reading Sale Price
        price = response.xpath(
            '//*[@id="product-price-8780"]/span/text()').extract_first()
        price = price[1:]
        print(price)

        # Reading Manufacturer
        producer = 'Hasler'#(response.xpath(
            #'//*[@id="product-attribute-specs-table"]/tbody/tr[9]/td/text()').extract_first())

        # Reading Description
        desc = response.xpath('//*[@id="maincontent"]/div[3]/div/div[3]/div[1]/div[1]/div/div/text()').extract_first().strip()
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



