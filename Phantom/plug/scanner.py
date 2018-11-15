import requests
import threading
import re

def scanner():
    oklist=[]
    notlist=[]
    tokenlist=['__csrf','token','验证码','Verification Code']
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    cos=input('cookie:')
    url=input('url:').strip()
    if cos=='':
        reqt=requests.get(url=url,headers=headers)
        for g in tokenlist:
            if not g in reqt.text:
                ok='[+] csrf debug :{}'.format(reqt.url)
                if ok in oklist:continue
                oklist.append(ok)
            else:
                no='[-] not csrf debug :{}'.format(reqt.url)
                if no in notlist:continue
                notlist.append(no)

        if len(notlist)==0:
            for o in oklist:
                print(o)
                print('')
        else:
            for g in notlist:
                print(g)
    else:
        cookies={}
        cookie=cos.strip()
        for y in cookie.split(';'):
            key,value=y.split('=',1)
            cookies[key]=value

        reqt = requests.get(url=url, headers=headers,cookies=cookies)
        for g in tokenlist:
            if not g in reqt.text:
                ok = '[+] csrf debug :{}'.format(reqt.url)
                if ok in oklist: continue
                oklist.append(ok)
            else:
                no = '[-] cookie not csrf debug :{}'.format(reqt.url)
                if no in notlist: continue
                notlist.append(no)

        if len(notlist) == 0:
            for o in oklist:
                print(o)
                print('')
        else:
            for g in notlist:
                print(g)

scanner()
