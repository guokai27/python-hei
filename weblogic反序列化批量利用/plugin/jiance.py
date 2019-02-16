#author:九世
#time:2019/2/16

guanjianzi='The server has not found anything'
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
import requests

def reqt(url):
    try:
        rqt=requests.get(url=url,headers=headers,timeout=3)
        if guanjianzi in rqt.text:
            js='[+] 存在weblogic的关键字,url:{}'.format(rqt.url)
            print(js)
            print(rqt.url,file=open('file/jiance.txt','a',encoding='utf-8'))
            return js
        else:
            jg='[-] 不存在weblogc关键字,url:{}'.format(rqt.url)
            return jg
    except Exception as r:
        return "报错:{}".format(r)
        pass