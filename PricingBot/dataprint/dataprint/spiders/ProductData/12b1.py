import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '12_b1' # change this first!!!
    allowed_domains = ['pitneybowes']
    start_urls = [
        # 787-E
        'https://www.pitneybowes.us/shop/postage-meter-ink-supplies/postage-meter-magenta-ink-cartridge-standard-for-sendpro-p-connect-plus-series-787-E/en-us/storeus?parentCategoryId=60443'
    ]

    def parse(self, response):
       
        # Reading Time
        now = datetime.now() #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url
        
        # Reading Title
        title = response.xpath('/html/body/div[3]/section[3]/div[2]/div[2]/div[1]/h1/text()').extract_first()
        print(title)
        #title = title.strip()
         
        # Reading Sale Price
        price = response.xpath('//*[@id="itemPrice_body"]/text()').extract_first()
        price = price[1:]
        print(price)
        
        # Reading Manufacturer
        producer = 'Pitney Bowes' #(response.xpath('//*[@id="app"]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/a/span/text()').extract_first())
        
        # Reading Description
        desc_tmp = response.xpath('/html/body/div[3]/section[3]/div[2]/div[2]/div[1]/div[7]/ul/li/text()').extract()
        description = "".join(desc_tmp[0:]).strip()
        print(description)

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



