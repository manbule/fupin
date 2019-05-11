#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import MySQLdb
import json
from redis import Redis


def process_item():
    #创建redis数据库连接
    rediscli: Redis =redis.Redis(host= "127.0.0.1",port= 6379,db= 0)
    #创建mysql数据库连接
    mysqlcli = MySQLdb.connect(host="127.0.0.1",port = 3306,\
                     user="root",passwd = "123456",db = "fupinsql")
    offsrt = 0
    while True:
        source,data =rediscli.blpop("fupin:items")
        item = json.load(data)
        cursor = mysqlcli.cursor()
        cursor.execute("insert into crops (sort_name,variety_name,growth_period,sowing_time,fertilizer,water,utput,control_time,adaptive_area)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)") % (item['sort_name'],item['variety_name'],\
                        item['growth_period'],item['sowing_time'],item['fertilizer'],\
                        item['water'],item['utput'],item['control_time'],item['adaptive_area'])
        mysqlcli.commit()
        cursor.close()
        offsrt+=1
        print(offsrt)

if  __name__ == "__main__":
    process_item()
