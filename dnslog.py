#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import json

import requests

from config_io import savebypickle, getbypickle
from config_requests import headers


def getcookie():
    q=requests.get('http://dnslog.cn/getdomain.php',headers=headers)
    dns=q.text
    ck=requests.utils.dict_from_cookiejar(q.cookies)
    print('获得临时DNGLOG地址：{}'.format(dns))
    savebypickle(dns,'temp/dns')
    savebypickle(ck,'temp/ck')
    return dns



def dnslogcheck(keyword):
    ck=getbypickle('temp/ck')
    q=requests.get('http://dnslog.cn/getrecords.php',headers=headers,cookies=ck)
    res=json.dumps(q.text)
    if keyword in res:
        print('yes')
        return 1
    else:
        return 0





if __name__ == '__main__':
    # getcookie()
    dnslogcheck('23333')