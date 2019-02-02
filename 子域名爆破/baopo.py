#author:九世
#time:2019/2/1

import requests
import threading
import os
import time

dict=[]

class Rkst:
    def __init__(self,headers):
        self.headers=headers

    def shenc(self,file):
            for k in file.readlines():
                qc="".join(k.split('\n'))
                yield qc

    def one_domain(self,ssl,url):
        for q in dict:
            urls='{}'.format(ssl)+q+'.'+url
            yield urls

    def two_domain(self,ssl,url):
        for v in dict:
            for v2 in dict:
                urls='{}'.format(ssl)+v+'.'+v2+'.'+url
                yield  urls

    def san_domain(self,ssl,url):
        for u in dict:
            for u1 in dict:
                for u2 in dict:
                    urls='{}'.format(ssl)+u+'.'+u1+'.'+u2+'.'+url
                    yield urls

    def si_domain(self,ssl,url):
        for s in dict:
            for s1 in dict:
                for s2 in dict:
                    for s3 in dict:
                        urls='{}'.format(ssl)+s+'.'+s1+'.'+s2+'.'+s3+'.'+url
                        yield urls

    def wu_domain(self,ssl,url):
        for b in dict:
            for b1 in dict:
                for b2 in dict:
                    for b3 in dict:
                        for b4 in dict:
                            urls='{}'.format(ssl)+b+'.'+b1+'.'+b2+'.'+b3+'.'+b4+'.'+url
                            yield urls

    def bao(self,url):
        try:
            reqt=requests.get(url=url,headers=self.headers,timeout=3)
            if reqt:
                print('[+] Found domain:{}'.format(url))
                print(url,file=open('save.txt','a'))
        except:
            pass

        lock.release() #Unlock the thread

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    if os.path.exists('file/one.txt'):
        print('[+] Found dict.txt')
    else:
        print('[-] Not Found dict.txt...')
        exit()

    dk=open('file/one.txt','r')

    user=input('domain>:')
    ssl=input('http/https>:')
    obj=Rkst(headers=headers)
    if ssl=='http':
        ht='http://'
    elif ssl=='https':
        ht='https://'

    print('[!] Test the first level domain name')
    for o in obj.shenc(dk):
        dict.append(o)


    lock=threading.BoundedSemaphore(100) #Set the thread to 100
    print('[!] Write the generated first-level domain name to the list')
    for y in obj.one_domain(ht,user):
        lock.acquire() #Lock the thread
        t = threading.Thread(target=obj.bao, args=(y,))
        t.start()

    print('[!] Write the generated second-level domain name to the list')
    for y2 in obj.two_domain(ht,user):
        lock.acquire()
        t = threading.Thread(target=obj.bao, args=(y2,))
        t.start()

    print('[!] Write the generated third-level domain name to the list')
    for y3 in obj.san_domain(ht,user):
        lock.acquire()
        t = threading.Thread(target=obj.bao, args=(y3,))
        t.start()

    print('[!] Write the generated four-level domain name to the list')
    for y4 in obj.si_domain(ht,user):
        lock.acquire()
        t = threading.Thread(target=obj.bao, args=(y4,))
        t.start()

    print('[!] Write the generated five-level domain name to the list')
    for y5 in obj.wu_domain(ht,user):
        lock.acquire()
        t = threading.Thread(target=obj.bao, args=(y5,))
        t.start()