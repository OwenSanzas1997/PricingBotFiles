import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '28_b1'  # change this first!!!
    allowed_domains = ['mybinding']
    start_urls = [
        # WJ20INK
        'https://www.mybinding.com/compatible-red-ink-cartridge-wj20ink-33000262x-for-hasler-wj20-postage-meter-1pk.html/'
    ]

    def parse(self, response):
        # Reading Time
        now = datetime.now()  #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url

        # Reading Title
        title = response.xpath('//*[@id="maincontent"]/div[3]/div/div[1]/h1/span/text()').extract_first()
        print(title)
        # title = title.strip()

        # Reading Sale Price
        price1 = response.xpath('/html/body/div[4]/main/div[3]/div/div[2]/div/form/div[2]/div/div[1]/div/p/span/span/text()').extract_first()
        price2 = response.xpath('//*[@id="product-price-59156"]/sup[2]/text()').extract_first()
        price = str(price1.strip()) + str(price2)
        print(price)

        # Reading Manufacturer
        producer =  (response.xpath('//*[@id="product_addtocart_form"]/div[1]/div[1]/div[2]/span[2]/a/text()').extract_first())

        # Reading Description
        description = response.xpath('//*[@id="product_tabs_description_contents"]/div[1]/div/text()').extract_first()
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



