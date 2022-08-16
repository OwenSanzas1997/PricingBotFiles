Instructions on how to use this scraper:
1. Install scrapy on the environment that you want to run
2. Install gspread for using googlesheets
3. Install schedule for running the script for every given time interval
4. Install pandas and html5lib for reading tables of Amazon pages
5. Execute the file autorun2.py to run the script every 15 seconds. Time can be set in the file.
6. To modify the urls to be visied, modify the start_urls in autopriceSpider.py in spiders folder.
7. To modify the output googlesheets, modify the creds.json and the googlesheets name in function parse of the autopriceSpider.py
8. To modify the parsing process of the spider, modify the parse function in autopriceSpider