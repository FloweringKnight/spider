#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import http.cookiejar


def save_cookie(url):
    cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
    handle = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handle)
    res = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    res1 = res.read().decode('utf-8')
    return res1


if __name__ == '__main__':
    result = save_cookie('http://www.zhihu.com')


