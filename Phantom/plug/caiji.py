import requests
import threading
from bs4 import BeautifulSoup
import re
import json
import os

urlsd=[]
user=input('file:')
if os.path.exists(user):
    print('[+] {} ok'.format(user))
else:
    print('[-]Not found {}'.format(user))
    exit()

def zhuaqu(urls):
    try:
        xj = open('save.txt', 'w')
        xj.close()
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        reqt = requests.get(url=urls, headers=headers)
        if reqt.status_code == 200:
            ce = re.findall('<a target="_blank" href=".*" class="c-showurl" style="text-decoration:none;">.*</a>',
                            reqt.content.decode('utf-8'))
            for c in ce:
                dw = re.findall('href=".*"', str(c))
                for l in dw:
                    dw = BeautifulSoup(str(l), 'html.parser')
                    ds = dw.find_all('div')
                    for c in ds:
                        tools = c.get('data-tools')
                        ld = json.loads(tools)
                        kv = requests.get(url=ld['url'], headers=headers)
                        print('url:{} title:{}'.format(kv.url, ld['title']))
                        print('url:{} title:{}'.format(kv.url, ld['title']),file=open('save.txt','a'))
    except:
        pass


if __name__ == '__main__':
    wb=open('{}'.format(user),'r',encoding='utf-8')
    for r in wb.readlines():
        lwd="".join(r.split('\n'))
        a = 10
        for y in range(75):
            pg=a*y
            ux='https://www.baidu.com/s?wd={}&pn={}&oq=ddd&tn=baiduhome_pg&ie=utf-8&rsv_idx=2&rsv_pq=f2d1ced40003b684&rsv_t=4f19k3bzHVjtUBB3yIGpe%2BUvHsvN0dZxuzIUvndbpIXRm2FRWWLbkeXdOLWooLYqUDxM'.format(lwd,pg)
            t=threading.Thread(target=zhuaqu,args=(ux,))
            t.start()
