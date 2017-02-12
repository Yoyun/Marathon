# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MarathonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MatchItem(scrapy.Item):
    name = scrapy.Field()           # 名称
    date = scrapy.Field()           # 日期
    xiang_mu = scrapy.Field()       # 比赛项目
    gui_mo = scrapy.Field()         # 比赛规模
    shi_jian = scrapy.Field()       # 比赛时间
    cheng_shi = scrapy.Field()      # 比赛城市
    lei_xing = scrapy.Field()       # 路线类型
    guan_wang = scrapy.Field()      # 赛事官网
    dian_hua = scrapy.Field()       # 联系电话
    wechat_number = scrapy.Field()  # 微信公众号
    zhu_ban = scrapy.Field()        # 主办单位
    cheng_ban = scrapy.Field()      # 承办单位
    tui_guang = scrapy.Field()      # 推广单位
    wen_du = scrapy.Field()         # 平均温度
    shi_du = scrapy.Field()         # 平均湿度
















