#author:九世
#time:2019/4/14

import requests
from bs4 import BeautifulSoup
import asyncio
from aiohttp import ClientSession
import re
import xlwt
import time
import os

new_cve=[]
bh_cve=[]
jg_cve=[]

class Demon:
    def __init__(self,headers,url):
        self.headers=headers
        self.url=url

    def zx(self):
        try:
            rgt=requests.get(url=self.url,headers=headers,timeout=3)
            zg=BeautifulSoup(rgt.text,'html.parser')
            for c in zg.find_all('a'):
                href=c.get('href')
                new_cve.append(href)
        except Exception as r:
            print('[-] Error {}'.format(r))


    async def zhuaqu(self,url):
        async with ClientSession() as reqt:
            try:
                async with reqt.get(url=url,headers=self.headers,timeout=2) as respone:
                    url=respone.url
                    jg_cve.append(url)
                    zz=re.findall('[0-9]{1,}-.*',str(url))
                    bh_cve.append('CVE-{}'.format(zz[0]))

            except:
                pass

    def writes(self):
        workbook=xlwt.Workbook(encoding='utf-8')
        sheet=workbook.add_sheet("今天更新的CVE")
        sheet.write(0,0,"CVE编号")
        sheet.write(0,1,"URL")
        for i in range(0,len(bh_cve)):
            sheet.write(int(i)+1,0,bh_cve[i])
            sheet.write(int(i)+1,1,'{}'.format(jg_cve[i]))

        sz=time.time()
        workbook.save('{}.xls'.format(sz))
        if os.path.exists('{}.xls'.format(sz)):
            print('[+] 保存成功')
        else:
            print('[-] 保存失败')

    async def main(self):
        td=[]
        for n in new_cve:
            jc=asyncio.ensure_future(self.zhuaqu(n))
            td.append(jc)

        await asyncio.wait(td)


if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    urls='https://cassandra.cerias.purdue.edu/CVE_changes/today.html'
    obj=Demon(headers=headers,url=urls)
    obj.zx()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.main())
    loop.close()
    obj.writes()