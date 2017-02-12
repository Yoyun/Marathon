# -*- coding: utf-8 -*-
import scrapy
import json
import re
from Marathon.items import MatchItem


class RunchinaSpider(scrapy.Spider):
    name = "runchina"
    allowed_domains = ["runchina.org.cn"]
    start_urls = [
        'http://www.runchina.org.cn/portal.php?mod=calendar&ac=search'
    ]
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'http://www.runchina.org.cn/portal.php?mod=calendar&ac=list',
    }
    formdata = {
        'starttime': '2016-01-01',
        'endtime': '2016-12-18'
    }
    item_detail_url = 'http://www.runchina.org.cn/portal.php?mod=calendar&ac=detail&id='
    encode_str = 'utf-8'
    info_keys = {
        '比赛项目': 'xiang_mu',
        '项目规模': 'gui_mo',
        '比赛时间': 'shi_jian',
        '比赛城市': 'cheng_shi',
        '路线类型': 'lei_xing',
        '赛事网站': 'guan_wang',
        '联系电话': 'dian_hua',
        '微信公众号': 'wechat_number',
        '主办单位': 'zhu_ban',
        '承办单位': 'cheng_ban',
        '推广单位': 'tui_guang',
        '平均温度': 'wen_du',
        '平均湿度': 'shi_du',
    }

    def start_requests(self):
        return [
            scrapy.FormRequest(self.start_urls[0],
                               headers=self.headers,
                               formdata=self.formdata,
                               callback=self.parse_search)
        ]

    def parse_search(self, response):
        items = json.loads(response.body)
        num = 1
        for item in items:
            fid = item['fk_comp_id']
            new_url = self.item_detail_url + fid
            yield scrapy.Request(new_url,
                             headers=self.headers,
                             callback=self.parse_detail)

    def parse_detail(self, response):
        match_item = MatchItem()
        for k in match_item.items():
            match_item[k] = '/'
        # 标题
        title = response.css('div.match-title>h2.name::text')[0].extract().encode(self.encode_str)
        # 比赛日期
        date = response.css('div.match-title>div.date::text')[0].extract().encode(self.encode_str)
        date = re.match('.*(\d{4}年\d{1,2}月(\d{1,2}日)?).*', date).group(1)

        match_item['name'] = title
        match_item['date'] = date

        items = response.css('div.match-content>p.item')
        for item in items:
            lbl = item.css('span.lbl::text')[0].extract().encode(self.encode_str)
            for k, v in self.info_keys.items():
                if re.search(k, lbl) is not None:
                    info = ''.join(item.xpath('descendant::text()').extract()[1:]).encode(self.encode_str).strip()
                    match_item[v] = info
                    break

        yield match_item

