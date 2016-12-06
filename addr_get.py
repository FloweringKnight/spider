#!/usr/bin/python
# -*- coding: utf-8 -*-
from url_open import url_open
import re


def addr_get(n):
    '''获取address列表'''
    url_list = []
    for i in range(0, n):
        if i:
            url_temp = 'http://www.gapp.gov.cn/govservice/1980_' + str(i+1) + '.shtml'
            url_list.append(url_temp)
        else:
            url_list.append('http://www.gapp.gov.cn/govservice/1980.shtml')
    need_str = re.compile(r'\<li\>\<a href=\"\/(govservice\/198.+?shtml)\".+?\d\d\d\d年\d+?月份.+?审批信息.+?\<\/li\>')
    addr_temp = []
    for each in url_list:
        b = url_open(each)
        temp = need_str.findall(b)
        for every_element in temp:
            addr_temp.append(every_element)
    str1 = 'http://www.gapp.gov.cn/'
    addr_list = [str1 + i for i in addr_temp]
    return addr_list
