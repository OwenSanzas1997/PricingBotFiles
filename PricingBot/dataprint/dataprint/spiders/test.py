# import gspread

# gc = gspread.service_account(filename = 'creds.json')
# sh = gc.open('DataPrint Web Scraper Data Storage ').sheet1


class A_Spider():
    name = '2_a'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/Pitney-Bowes-Compatible-769-0-Cartridge/dp/B003B4UFOI'
    ]

print(A_Spider.name[0:2])