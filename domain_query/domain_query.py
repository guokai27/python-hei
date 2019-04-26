#author:jiushi
#time:2019/4/8

import requests
import asyncio
import re
import time
import os
import socket
import gevent
from gevent import monkey;monkey.patch_all()

domains__list=[]
gdr=os.listdir('file')

class Domain:
    def __init__(self,headers):
        self.headers=headers

    async def domain_query(self,url,domain):
        rqt=requests.get(url=url,headers=self.headers)
        if 'chinaz.com' in rqt.url:
            time.sleep(1)
            await asyncio.sleep(1)
            page=re.findall('共.*?页',rqt.text)
            if len(page)==0:
                while True:
                    rqw=requests.get(url=url, headers=self.headers)
                    time.sleep(1)
                    page = re.findall('共.*?页', rqw.text)
                    if len(page)>0:
                        break
            page=str(page[0]).replace('共','').replace('页','')
            for j in range(1,int(page)+1):
                urls='{}{}'.format(rqt.url,j)
                rqts = requests.get(url=urls,headers=self.headers)
                cz=re.findall('<div class="w23-0"><a .*>.*</div>',rqts.text)
                for c in cz:
                    doma=re.findall('"_blank">.*?</a>',str(c))
                    for d in doma:
                        domains__list.append(str(d).replace('"_blank">','').replace('</a>',''))

        elif 'site.ip138.com' in rqt.url:
            await asyncio.sleep(1)
            zz=re.findall('<a href="/.*/" target="_blank">.*</a></p>',rqt.text)
            for a in zz:
                th=str(a).replace('</a></p>','')
                th=re.sub('<a href="/.*/" target="_blank">','',th)
                domains__list.append(th)

        elif 'sbd.ximcx.cn' in rqt.url:
            await asyncio.sleep(1)
            data={'domain':'{}'.format(domain)}
            rgb=requests.post(url=url,headers=self.headers,data=data)
            jn=rgb.json()['data']
            for j in jn:
                domains__list.append(j['domain'])

        elif 'ce.baidu.com' in rqt.url:
            await asyncio.sleep(1)
            data=rqt.json()['data']
            for d in data:
                domains__list.append(d['domain'])

    async def file_baopo(self,file_name,domain):
        for r in file_name:
            dks=open('file/{}'.format(r),'r')
            for r in dks:
                qc="".join(r.split('\n'))
                urls='http://{}.{}'.format(qc,domain)
                thead6=self.baod(urls)
                tasks.append(asyncio.ensure_future(thead6))

    async def baod(self,url):
        jg=str(url).replace('http://','')
        try:
            s=socket.gethostbyname_ex(jg)
            if 'baidu.com' in s[0]:
                 print(s)
        except:
            pass

    def sc(self):
        if len(domains__list)>0:
            for v in list(set(domains__list)):
                print(v)

    async def main(self,domain,uuid):
        global tasks
        thad=self.domain_query('http://site.ip138.com/{}/domain.htm'.format(domain),domain)
        thad2=self.domain_query('http://tool.chinaz.com/subdomain?domain={}&page='.format(domain),domain)
        thad3=self.domain_query('http://sbd.ximcx.cn/DomainServlet',domain)
        thad4=self.domain_query('http://ce.baidu.com/index/getRelatedSites?site_address={}'.format(domain),domain)
        thad5=self.file_baopo(gdr,domain)
        tasks=[] #确认添加任务
        if uuid==1:
            tasks.append(asyncio.ensure_future(thad))
            tasks.append(asyncio.ensure_future(thad2))
            tasks.append(asyncio.ensure_future(thad3))
            tasks.append(asyncio.ensure_future(thad4))
        elif uuid==2:
            tasks.append(asyncio.ensure_future(thad5))
        elif uuid==3:
            tasks.append(asyncio.ensure_future(thad))
            tasks.append(asyncio.ensure_future(thad2))
            tasks.append(asyncio.ensure_future(thad3))
            tasks.append(asyncio.ensure_future(thad4))
            tasks.append(asyncio.ensure_future(thad5))
        else:
            pass
        await asyncio.wait(tasks)#等待

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    obj=Domain(headers=headers)
    loop=asyncio.get_event_loop() #事件列表
    loop.run_until_complete(obj.main('baidu.com',2)) #运行直到完全的结束
    obj.sc()