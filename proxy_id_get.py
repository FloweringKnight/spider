#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import re

def proxy_id_get():
    url = ['http://www.kuaidaili.com/proxylist/'+str(x) for x in range(1,11)]
    proxy_id = []
    for every_url in url:
        a = urllib.request.urlopen(every_url)
        b = a.read().decode('utf-8')
        str1 = re.compile(r'data\-title\=\"IP\"\>(\d+?\.\d+?\.\d+?\.\d+?)\<\/td[\s\S]+?\"PORT\"\>(\d+?)\<\/td\>')
        res = str1.findall(b)
        for each in res:
            str2 = str(each[0]) + ':' + str(each[1])
            proxy_id.append(str2)
    return proxy_id

if __name__ == '__main__':
    print(proxy_id_get())

