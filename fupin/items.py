# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class FupinItem(Item):
    # 分类名称
    sort_name = Field()
    # 品种名称
    variety_name=Field()
    #生育期
    growth_period = Field()
    #播种时间
    sowing_time = Field()
    #肥料管理
    fertilizer = Field()
    #水量管理
    water = Field()
    #产量
    output = Field()
    #产量对照时间
    control_time = Field()
    #适应区域
    adaptive_area = Field()
    #内容链接
    content_url = Field()