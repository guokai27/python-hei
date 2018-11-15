import requests
import threading
import os

xj=open('save.txt','w')
xj.close()

oklist=[]
notlist=[]

def route(files,url):
    guolist=['404','Error','Not Found','500','error','360','Hacking','安全狗','防火墙','云锁','违法','无权限','403','D盾']
    urls=url+files
    headers={'user-aget':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    reqt=requests.get(url=urls,headers=headers,timeout=10)
    for g in guolist:
        if not g in reqt.content.decode('utf-8'):
            ok='[+] (status_code:{}|url:{})'.format(reqt.status_code,reqt.url)
            if ok in oklist:continue
            oklist.append(ok)
        else:
            no='[-] >>> status_code:{}|url:{}'.format(reqt.status_code,reqt.url)
            if no in notlist:continue
            notlist.append(no)

    if len(notlist)==0:
        for y in oklist:
            print(y)
            print(y,file=open('save.txt','a'))
    else:
        for n in notlist:
            print(n)

if __name__ == '__main__':
    while True:
        us=input('dict:')
        if os.path.exists(us):
            print('[+] open {} ok !'.format(us))
            break
        else:
            print('[-]  not {}'.format(us))
            continue

    urs=input('url:')
    dk=open('{}'.format(us),'r')
    for r in dk.readlines():
        qc="".join(r.split('\n'))
        t=threading.Thread(target=route,args=(qc,urs.rstrip('/')))
        t.start()