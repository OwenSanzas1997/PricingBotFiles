import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '17_b1'  # change this first!!!
    allowed_domains = ['ldproducts']
    start_urls = [
        'https://www.ldproducts.com/compatible-neopost-ijink678h-red-ink-cartridge'
    ]

    def parse(self, response):
       
        # Reading Time
        now = datetime.now() #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url
        
        # Reading Title
        title = response.xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div[1]/h1/span/text()').extract_first()
        title = title.strip()
         
        # Reading Sale Price
        price = response.xpath('//*[@id="product-price-51685"]/span/text()').extract_first()
        price = price[1:]
        print(price)
        
        # Reading Manufacturer
        producer = (response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[7]/td/text()').extract_first())  # [7:]
        
        # Reading Description
        description = response.xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div/text()').extract_first()
        #description = "".join(desc_tmp[3:]).strip()

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



