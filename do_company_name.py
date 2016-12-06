#!/usr/bin/python
# -*- coding: utf-8 -*-
from addr_get import addr_get
from form_get import form_get


n = 2
res1 = addr_get(n)
res2 = form_get(res1)
with open('result.txt', 'w', encoding='utf-8') as a:
    for each in res2:
        str1 = each[0]+' '+each[1]+' '+each[2]+' '+each[3]+'\n'
        a.write(str1)
