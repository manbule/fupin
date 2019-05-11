# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
#from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fupin.items import FupinItem
from scrapy.selector import Selector
import re

class CropsSpider(RedisCrawlSpider):
    name = 'crops'
    allowed_domains = ['shuju.aweb.com.cn']
    #start_urls = ['http://shuju.aweb.com.cn/breed/breed-14-1.shtml']
    redis_key = "CropsSpider:start_urls"
 #   def __init__(self,*args,**kwargs):
  #      domain = kwargs.pop('domain','')
  #      self.allowed_domains = filter(None,domain.split(','))
 #       super(CropsSpider,self).__init__(self,*args,**kwargs)

    page_link= LinkExtractor(allow=("http://shuju.aweb.com.cn/breed/breed-14-\d+.shtml"))
    content_link = LinkExtractor(allow=("http://shuju.aweb.com.cn/breed/\d+/\d+.html"))
    rules = (
        Rule(page_link),
        Rule(content_link,callback="parse_item")
    )

    def parse_item(self, response):
        item = FupinItem()

        response_selector = Selector(response)
        # 分类名称
        item['sort_name'] = self.get_sname(response)
        # 品种名称
        item['variety_name'] = self.get_vname(response)
        # 生育期
        item['growth_period'] = self.get_gperiod(response)
        # 播种时间
        item['sowing_time'] = self.get_stime(response)
        # 肥料管理
        item['fertilizer'] = self.get_fertilizer(response)
        # 水量管理
        item['water'] = self.get_water(response)
        # 产量
        item['output'] = self.get_output(response)
        # 产量对照时间
        item['control_time'] = self.get_ctime(response)
        # 适应区域
        item['adaptive_area'] = self.get_area(response)
        #内容链接
        item['content_url'] = response.url

        yield item
    # 分类名称
    def get_sname(self,response):
        sort_name = response.xpath("//*[@id='content']/div[1]/div[1]/div/ul/li[1]/text()").extract()
        if len(sort_name):
            sort_name=sort_name[0]
        else:
            sort_name = "NULL"
        return sort_name

    # 品种名称
    def get_vname(self, response):
        variety_name = response.xpath("//*[@id='content']/div[1]/div[1]/div/ul/li[2]/text()").extract()
        if len(variety_name):
            variety_name = variety_name[0]
        else:
            variety_name = "NULL"
        return variety_name

    # 生育期
    def get_gperiod(self, response):
        growth_period = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[2]").extract()
        if len(growth_period):
            growth_period = growth_period[0]
        else:
            growth_period = "NULL"
        return growth_period

    # 播种时间
    def get_stime(self, response):
        sowing_time = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[3]").extract()
        if len(sowing_time):
            sort_name = sowing_time[0]
        else:
            sowing_time = "NULL"
        return sowing_time

    # 肥料管理
    def get_fertilizer(self, response):
        fertilizer = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[3]").extract()
        if len(fertilizer):
            fertilizer = fertilizer[0]
        else:
            fertilizer = "NULL"
        return fertilizer

    # 水量管理
    def get_water(self, response):
        water = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[3]").extract()
        if len(water):
            water = water[0]
        else:
            water = "NULL"
        return water

    # 产量
    def get_output(self, response):
        output = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[5]/text()").extract()
        if len(output):
            output = output[0]
        else:
            output = "NULL"
        return output

    # 产量对照时间
    def get_ctime(self, response):
        control_time = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[5]/text()").extract()
        if len(control_time):
            control_time = control_time[0]
        else:
            control_time = "NULL"
        return control_time

    # 适应区域
    def get_area(self, response):
        adaptive_area = response.xpath("//*[@id='content']/div[1]/div[1]/div/p[6]").extract()
        if len(adaptive_area):
            adaptive_area = adaptive_area[0]
        else:
            adaptive_area = "NULL"
        return adaptive_area




