#!/usr/bin/python
# -*- coding: utf-8 -*-
###说明###
#1.使用sqlite数据库
#2.place_out('新密')输出 河南省郑州市新密市
#3.province_out_only('新密')输出 河南省
#4.数据库参见2016年9月公式的区划代码
#5.采用模糊查询，仅输出第一个结果，如果对精准度有需求，请增加关键字
###
import sqlite3


def sql_query(str1):
    conn = sqlite3.connect('place.DB')
    c = conn.cursor()
    if isinstance(str1, str):
        c.execute('SELECT * FROM place WHERE name LIKE ?', ('%' + str1 + '%',))
        conn.commit()
        return c.fetchone()
    elif isinstance(str1, int):
        if str1 % 100 == 0:
            c.execute('SELECT * FROM place WHERE id = ?', (str(str1)[:2] + '0000',))
            conn.commit()
            return c.fetchone()
        else:
            c.execute('SELECT * FROM place WHERE id = ?', (str(str1)[:4] + '00',))
            conn.commit()
            return c.fetchone()
    conn.close()


def place_out_temp(address, list1=[]):
    res_temp = sql_query(address)
    n = res_temp[0]
    p = res_temp[1]
    if n % 1000 != 0:
        place_out_temp(n, list1)
    list1.append(p)
    return list1


def place_out(address, str1=''):
    try:
        for each in place_out_temp(address, []):
            str1 += each
        return str1
    except TypeError:
        return None

def province_out_only(address):
    try:
        res_temp = sql_query(address)
        n = res_temp[0]
        nn = int(str(n)[:2] + '0000')
        res = sql_query(nn)
        return res[1]
    except TypeError:
        return None

if __name__ == '__main__':
    for i in range(5):
        print(place_out('新密'))
    print(province_out_only('fff'))