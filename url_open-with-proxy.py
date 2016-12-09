#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import random
import urllib.error
import socket
from proxy_id_get import proxy_id_get


def url_open(url, data=None):
    '''若响应的数据是json格式，需要调用json.loads()来处理一下，否则接收是以字符串型式'''
    agent1 = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML, like Gecko) Version/7.2.1.0 Safari/536.2+',
        'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; qihu theworld)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
        'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62'
    ]
    proxy_id = proxy_id_get()
    for each in proxy_id:
        socket.setdefaulttimeout(5)
        try:
            proxy_support = urllib.request.ProxyHandler({'http':each})
            opener = urllib.request.build_opener(proxy_support)
            a = random.choice(agent1)
            opener.addheaders.append(('User-Agent', a))
            if data:
                data = urllib.parse.urlencode(data).encode('utf-8')
            b = opener.open(url, data)
            c = b.read()
            d = c.decode('utf-8')
            print(each,'正确')
        except urllib.error.HTTPError as e:
            print(each, "错误：错误代码：", e.code)
            print("错误内容：", e.read().decode("utf8"))
        except urllib.error.URLError as e:
            print(each, '错误：未能获取服务器信息.')
            print('错误原因: ', e.reason)
        except:
            print(each, "错误：其他未知错误！")


if __name__ == '__main__':
    url_open('http://www.baidu.com')