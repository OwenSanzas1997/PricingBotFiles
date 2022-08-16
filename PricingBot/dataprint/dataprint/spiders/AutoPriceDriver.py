import time

from scrapy.utils.project import get_project_settings
import sys
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

"""
This project is directed by Ariel Tavor from DataPrint Tech. 

Made and updated by: Frank Cheng, Hunter Shen and Ze Sheng From DataPrint Tech.

If you have any question, feel free to mail:

Ze Sheng: zesheng@seas.upenn.edu
"""

"""
This program is an initiator, you should run this to fetch all data from websites. 

If there is any new product, it should be added to this script.
"""
if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]
configure_logging()
runner = CrawlerRunner(get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl('32_a')
    yield runner.crawl('32_a2')
    yield runner.crawl('22_b2')
    yield runner.crawl('22_b3')
    yield runner.crawl('22_b4')
    yield runner.crawl('22_b5')
    yield runner.crawl('22_b6')

    # Product name: Pitney Bowes™ 769-0 Compatible Ink Cartridge
    yield runner.crawl('2_a')

    # Product name: Pitney Bowes™ 767-1 Compatible Ribbon Cassette
    yield runner.crawl('3_a')
    
    # Product name: Pitney Bowes™ 797-M Compatible Ink Cartridge
    yield runner.crawl('4_a')
    yield runner.crawl('4_b')

    # Product name: Pitney Bowes™ 793-5 Compatible Ink Cartridge
    yield runner.crawl('5_a')

    # Product name: Pitney Bowes™ 765-9 Compatible Ink Cartridge
    yield runner.crawl('6_a')

    # Product name: Pitney Bowes™ 621-1 Compatible Ink Cartridge
    yield runner.crawl('7_a')

    # Product name: Pitney Bowes™ 766-8 Compatible Ink Cartridge
    yield runner.crawl('8_a')

    # Product name: Pitney Bowes™ 772-1 Compatible Ink Cartridge
    yield runner.crawl('9_a')

    # Product name: Pitney Bowes™ 787-1, 78P-K - Connect+ Production Series
    yield runner.crawl('10_a')

    # Product name: Pitney Bowes™ 787-D - Connect+ Large Series
    yield runner.crawl('11_b1')  # 787-8
    yield runner.crawl('11_b2')  # 787-3

    # Product name: Pitney Bowes™ 787-E - Connect+ Standard Series
    yield runner.crawl('12_a')  # 787-D
    yield runner.crawl('12_b1')  # 787-E

    # Product name: FP™ My Mail Printer Remanufactured Ink Cartridge
    yield runner.crawl('14_b1')  # 787-E

    # FP™ Ultimail Remanufactured Ink Cartridge
    yield runner.crawl('15_b1')  # 787-E
    yield runner.crawl('15_b2')  # 787-E

    # Neopost™ 3300028D New Compatible Ink Cartridge
    yield runner.crawl('16_a')
    yield runner.crawl('16_b1')

    # Neopost™ IJINK678H New Compatible Ink Cartridge
    yield runner.crawl('17_b1')
    yield runner.crawl('17_b2')

    # Neopost™ IJINK3456H New Compatible Ink Cartridge
    yield runner.crawl('19_b1')
    yield runner.crawl('19_b2')

    # Neopost™ IJINK3456S New Compatible Ink Cartridge
    yield runner.crawl('20_b2')

    # Neopost™ IS500/IS6000 Remanufactured Ink Tank
    yield runner.crawl('21_b1')
    yield runner.crawl('21_b2')

    # Product name: ISINK34(22)
    yield runner.crawl('22_a')
    yield runner.crawl('22_b1')
    yield runner.crawl('22_b2')
    yield runner.crawl('22_b3')
    yield runner.crawl('22_b4')
    yield runner.crawl('22_b5')
    yield runner.crawl('22_b6')

    # Neopost™ ISINK2 New Compatible Ink Cartridge
    yield runner.crawl('23_a')
    yield runner.crawl('23_b1')

    # Hasler™ IM56INK Remanufactured Ink Tank
    yield runner.crawl('24_a')
    yield runner.crawl('24_b1')

    # Hasler™ IMINK2 New Compatible Ink Cartridge
    yield runner.crawl('25_a')
    yield runner.crawl('25_b1')

    # Hasler™ IMINK34 New Compatible Ink Cartridge
    yield runner.crawl('26_a')
    yield runner.crawl('26_b1')

    # Hasler™ INK4HC New Compatible Ink Cartridge
    yield runner.crawl('27_b1')
    yield runner.crawl('27_b2')

    # Hasler™ WJ20INK-1 New Compatible Ink Cartridge
    yield runner.crawl('28_b1')

    # Hasler™ WJ69INK New Compatible Ink Cartridge
    yield runner.crawl('29_b1')
    yield runner.crawl('29_b2')

    # Hasler™ WJINK-1 New Compatible Ink Cartridge
    yield runner.crawl('30_b1')
    yield runner.crawl('30_b2')

    # FP™ Postbase PIC10 Compatible Ink Cartridge
    yield runner.crawl('31_a')
    yield runner.crawl('31_b1')

    # FP™ Postbase PIC40 Compatible Ink Cartridge
    yield runner.crawl('32_a')

    # FP™ Postbase Mini Compatible Ink Cartridge
    yield runner.crawl('33_a')





    # Add new product here like this:
    # Product name: new name
    # yield runner.crawl('product id')
    print("All Prices are up to date !!!")
    reactor.stop()


def main():
    time_start = time.time()
    crawl()
    reactor.run()
    time_stop = time.time()

    print('Time cost: ', time_stop - time_start, 's')



if __name__ == "__main__":
    main()
