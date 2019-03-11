#author:九世
#time:2019/3/11

import requests
import re
from urllib import parse

print('星盟安全-天眼查资产收集-九世 签名：此生此世，为情所困')
uk=input('天眼查的cookie：')
user=input('要查询的公司：')
urlbm = parse.quote('{}'.format(user))
number=[]
durl=[]
zon_page=0
page=6
class rqt:
    def __init__(self,headers,url,cookie):
        self.headers=headers
        self.url=url
        self.cookie=cookie

    def reqt(self):
        global zon_page
        try:
            rvq=requests.get(url=self.url,headers=self.headers,cookies=self.cookie)
            rhj=re.findall('https://www.tianyancha.com/search/p.*\?',str(rvq.text))
            for r in rhj:
                number.append(int(str(r).replace('https://www.tianyancha.com/search/p','').replace('?','')))

            number.sort()
            number.reverse()
            zon_page+=number[0]
            print('[+] 搜索结果的总页数为：{}'.format(zon_page))
        except Exception as r:
            print('[-] Error:{}'.format(r))

        for u in range(1,int(page)):
            url='https://www.tianyancha.com/search/p{}?key={}'.format(u,urlbm)
            try:
                rvq=requests.get(url=url,headers=self.headers,cookies=self.cookie)
                v=re.findall('https://www.tianyancha.com/company/.*"',str(rvq.text))
                if 'VIP会员' in rvq.text:
                    print(rvq.url)
                    print('[-] 你不是VIP会员，钱还没充够')
                    exit()
                if '机器人' in rvq.text:
                    self.roobot(url=url)
                for g in v:
                    rgt=requests.get(url=str(g).replace('"',''),headers=self.headers,cookies=self.cookie)
                    zz=re.findall('<h1 class="name">.*</h1>',rgt.text)
                    udr=re.findall('<a class="link-click icpinfo-width"\s+\s+href=".*"',rgt.text)
                    if len(udr)!=0:
                        for u in udr:
                            print('公司名称：{} 知识产权网址：{}'.format(str(zz[0]).replace('<h1 class="name">','').replace('</h1>',''),str(u).replace('<a class="link-click icpinfo-width"','').replace('href=','').replace('"','').strip().lstrip().rstrip()))
                            print('公司名称：{} 知识产权网址：{}'.format(str(zz[0]).replace('<h1 class="name">', '').replace('</h1>', ''),str(u).replace('<a class="link-click icpinfo-width"', '').replace('href=', '').replace('"', '').strip().lstrip().rstrip()),file=open('save.txt','a',encoding='utf-8'))

            except Exception as r:
                print('[-] Error:{}'.format(r))

    def roobot(self,url):
        print('[-] 发现检测是否为机器人，请手动验证')
        print('请在浏览器登录天眼查，验证：{}'.format(url))
        while True:
            try:
                rv=requests.get(url=url,headers=self.headers,cookies=self.cookie)
                if not '机器人' in rv.text:
                    print('[+] 已人工验证')
                    break
                else:
                    continue
            except Exception as r:
                print('[-] Error:{}'.format(r))

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Referer':'https://www.tianyancha.com/'}
    url='https://www.tianyancha.com/search?key={}'.format(urlbm)
    cookie="""
    {}
    """.format(uk).strip().replace('\n','').rstrip().lstrip()
    cookies={}
    for c in cookie.split(';'):
        key,value=c.split('=',1)
        cookies[key]=value

    obj=rqt(headers=headers,url=url,cookie=cookies)
    obj.reqt()