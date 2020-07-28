#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
from fake_useragent import UserAgent
'''
    Usage：
    print(ua.ie)
    print(ua.opera)
    print(ua.chrome)
    print(ua.firefox)
    print(ua.safari)
    print(ua.random)
'''

# 实例化 UserAgent 类
ua = UserAgent()

# 通用headers配置
headers={"User-Agent":ua.random}

if __name__ == '__main__':
    print(headers)