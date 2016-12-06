#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sqlite3


with open('place.html.txt', 'r' ,encoding='gbk') as k:  #数据来自http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201608/t20160809_1386477.html
    kk = k.read()
str1 = re.compile(r'\<p\Wclass\=\"MsoNormal\"\>[\s\S]+?(\d\d\d\d\d\d)[\s\S]+?宋体\"\>\s+?(\S+?)\<\/span\>\<\/p\>')
res = str1.findall(kk)
conn = sqlite3.connect('place.DB')
c = conn.cursor()
for each in res:
    c.execute('INSERT INTO place VALUES (?,?)',each)
conn.commit()
conn.close()
