import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '15_b2' # change this first!!!
    allowed_domains = ['postagemachinesupplies.com']
    start_urls = [
        # FP – Ultimail Ink Cartridge – #58.0033.3138.00
        'https://postagemachinesupplies.com/products/fp-ultimail-ink-cartridge-58-0033-3138-00'
    ]

    def parse(self, response):
       
        # Reading Time
        now = datetime.now() #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url
        
        # Reading Title
        title = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/h1/text()').extract_first()
        title = title.strip()
         
        # Reading Sale Price
        price = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div[2]/div/div[2]/span/text()').extract_first()
        price = price.strip()
        price = price[1:]
        print(price)
        
        # Reading Manufacturer
        producer = (response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[1]/div[1]/a/text()').extract_first())
        
        # Reading Description
        description = response.xpath('//*[@id="shopify-section-static-product"]/section/article/div[2]/div[3]/p[1]/text()[1]').extract_first()
        #description = "".join(desc_tmp[0:]).strip()

        # Check if price is null
        if price == None:
            price = "nan"

           
        product =  {
            "time": time,
            "link": link,
            "titles": title,        
            "prices": price,
            "producers":producer,
            "description":description       
        }

        # writing to google sheets

        # data_info is our data set, including time, link, title, producer, description and price
        data_info = [str(product['time']), str(product['link']), str(product['titles']),
                     str(product['producers']), str(product['description']), str(product['prices'])]
        print(data_info)

        sheet_loader.sheet_loader(data_info, A_Spider.name[0:2])



