import scrapy
from datetime import datetime
from PricingBot.dataprint.dataprint.spiders import sheet_loader


class A_Spider(scrapy.Spider):
    name = '8_a' # change this first!!!
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/Pitney-Bowes-Compatible-Inkjet-Cartridges/dp/B00280H1FC'
    ]

    def parse(self, response):
       
        # Reading Time
        now = datetime.now() #
        time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Reading url
        link = response.url
        
        # Reading Title
        title = response.xpath('//span[contains(@class,"a-size-large product-title-word-break")]/text()').extract_first()
        title = title.strip()
         
        # Reading Sale Price
        price = response.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]/text()').extract_first()
        price = price[1:]
        print(price)
        
        # Reading Manufacturer
        producer = (response.xpath('//a[contains(@id,"bylineInfo")]/text()').extract_first())[7:]
        
        # Reading Description
        desc_tmp = response.xpath('//ul[contains(@class,"a-unordered-list a-vertical a-spacing-mini")]/li/span/text()').extract()
        description = "".join(desc_tmp[3:]).strip()

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

        sheet_loader.sheet_loader(data_info, A_Spider.name[0])



