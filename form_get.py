#!/usr/bin/python
# -*- coding: utf-8 -*-
from url_open import url_open
import re


def form_get(list_needed):
    '''获取结果列表，列表里每个元组有四个元素，分别是：游戏名，研发公司，发行公司，时间（精确到月）'''
    a = re.compile(r'pageNodeID\=(\d\d\d\d).+?\=(\d+).+?\=(\d+).+?\=([a-zA-Z]+).+?\=(\w+).+?\=(\w+).+?\=(\w+equals00equals0)')
    d = re.compile(r'\<tr\>\W*\<td\Wstyle\=\".+?none;\"\>\W*(.+)\W*\<\/td\>\W*.+\W*(.+)\W*.+\W*.+\W*(.+)[\s\S]+?(\d\d\d\d年\d+?月)\d+?日[\s\S]+?\<\/tr\>')
    data_send = {}
    url_shin = 'http://www.gapp.gov.cn/sitefiles/services/wcm/dynamic/output.aspx?publishmentSystemID=35&'
    msg_needed = []
    for each in list_needed:
        b = url_open(each)
        c = a.findall(b)
        data_send['pageNodeID'] = c[0][0]
        data_send['pageContentID'] = c[0][1]
        data_send['pageTemplateID'] = c[0][2]
        data_send['isPageRefresh'] = c[0][3]
        data_send['pageUrl'] = c[0][4]
        data_send['ajaxDivID'] = c[0][5]
        data_send['templateContent'] = c[0][6]
        res1 = url_open(url_shin, data_send)
        res2 = d.findall(res1)
        for every_element in res2:
            msg_needed.append(every_element)
    return msg_needed
