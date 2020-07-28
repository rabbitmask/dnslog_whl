# dnslog_whl
A whl for dnslog  from dnslog.cn

### WHL调度 
```
def getcookie():
    q=requests.get('http://dnslog.cn/getdomain.php',headers=headers)
    dns=q.text
    ck=requests.utils.dict_from_cookiejar(q.cookies)
    print('获得临时DNGLOG地址：{}'.format(dns))
    savebypickle(dns,'temp/dns')
    savebypickle(ck,'temp/ck')
    return dns


python dnslog.py
获得临时DNGLOG地址：fdyf5f.dnslog.cn
```
```
def dnslogcheck(keyword):
    ck=getbypickle('temp/ck')
    q=requests.get('http://dnslog.cn/getrecords.php',headers=headers,cookies=ck)
    res=json.dumps(q.text)
    print(res)
    if keyword in res:
        print('yes')
        return 1
    else:
        return 0


ping -n 1 23333.fdyf5f.dnslog.cn
python dnslog.py
yes
```
### WHL细节
cookiejar的存储和读取由pickle序列化与反序列化完成，headers采用随机库。
