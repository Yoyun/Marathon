# coding: utf-8

from scrapy import cmdline
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

cmdline.execute('scrapy crawl runchina'.split())
