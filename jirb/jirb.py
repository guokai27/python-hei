#author:九世
#time:2019/3/3

import requests
import random
import configparser
import os
import threading

black_list=[]
result=[]
result_ufck=[]

threadsq=10
xianchen = threading.BoundedSemaphore(threadsq)
def banner():
    banners = '''
           ___                      ___                   
  /  /\       ___          /  /\         _____    
 /  /:/      /  /\        /  /::\       /  /::\   
/__/::\     /  /:/       /  /:/\:\     /  /:/\:\  
\__\/\:\   /__/::\      /  /:/~/:/    /  /:/~/::\ 
   \  \:\  \__\/\:\__  /__/:/ /:/___ /__/:/ /:/\:|
    \__\:\    \  \:\/\ \  \:\/:::::/ \  \:\/:/~/:/
    /  /:/     \__\::/  \  \::/~~~~   \  \::/ /:/ 
   /__/:/      /__/:/    \  \:\        \  \:\/:/  
   \__\/       \__\/      \  \:\        \  \::/   
                           \__\/         \__\/  

   author：九世
   version：1.0
       '''
    print('\033[1;33m {} \033[0m'.format(banners))

class baopo:
    def __init__(self,rhost):
        self.rhost=rhost

    def read_config(self):
        if os.path.exists('config'):
            print('\033[1;32m [+] \33[0m 配置文件路径存在')
        else:
            print('\033[1;31m [-] \33[0m 配置文件路径不存在')
            exit()

        global default_folder,threadsq,status_code,default,xianchen,value
        value=0
        default=''
        conf=configparser.ConfigParser()
        conf.read('config/config.ini',encoding='utf-8')
        default_folder=conf.get('setup','default_folder')
        default_file=conf.get('setup','default_file')
        if len(default_folder)==0 and len(default_file)!=0:
            value+=0
            default+=str(default_file)

        elif len(default_folder)!=0 and len(default_file)==0:
            value+=1
            default+=str(default_folder)

        status_code=conf.get('setup','status_code')
        try:
            dk=open('config/black.txt','r',encoding='utf-8')
            for r in dk.readlines():
                r="".join(r.split('\n'))
                black_list.append(r)
        except:
            print('\033[1;31m [-] \33[0m 黑名单读取失败')
            exit()

        print('\033[1;32m [+] \33[0m 配置文件与黑名单读取成功')
        print('\033[1;32m [+] \33[0m 指定爆破路径或字典：{}'.format(default))
        print('\033[1;32m [+] \33[0m 最大线程为：{}'.format(threadsq))
        print('\033[1;32m [+] \33[0m 匹配状态码为：{}'.format(status_code))


    def jiance(self):
        try:
            requests.get(url=self.rhost)
            print('\033[1;32m [+] \33[0m 网站存活：{}'.format(self.rhost))
            t = threading.Thread(target=jb.blst_default, args=(value,))
            t.start()
        except:
            print('\033[1;31m [-] \033[0m 网络连接失败....')
            print('\033[1;31m [-] \033[0m 无法爆破：{}'.format(self.rhost))

    def rdheaders(self):
        headers_list=['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0']

        random.shuffle(headers_list)
        return headers_list[0]

    def blst_default(self,value):
        if value==1:
            dq=os.listdir(default)
            headers = {'user-agent':'{}'.format(self.rdheaders())}
            for f in dq:
                dk=open('{}/{}'.format(default,f),'rb')
                for d in self.reay(dk):
                    try:
                        url = '{}/{}'.format(str(self.rhost).strip(), d).strip()
                        rqts=requests.get(url=url,headers=headers,timeout=3)
                        if rqts.status_code==int(status_code):
                            for b in black_list:
                                if b not in rqts.text and b not in rqts.content.decode('utf-8'):
                                    if rqts.url in result:continue
                                    result.append(rqts.url)
                                elif b in rqts.text or b in rqts.content.decode('utf-8'):
                                    if rqts.url in result_ufck:continue
                                    result_ufck.append(rqts.url)
                            self.echo()
                    except TimeoutError:
                        print('\033[1;31m [-] \033[0m 超时：{}'.format(rqts.url))
                        pass
            xianchen.acquire()
        elif value==0:
            dk=open(default,'rb')
            headers = {'user-agent': '{}'.format(self.rdheaders())}
            for d in dk.readlines():
                d="".join(bytes.decode(d).split('\n'))
                try:
                    url='{}/{}'.format(str(self.rhost).strip(),d).strip()
                    rqts=requests.get(url=url,headers=headers,timeout=3)
                    if rqts.status_code==int(status_code):
                        for b in black_list:
                            if b not in rqts.text and b not in rqts.content.decode('utf-8'):
                                if rqts.url in result:continue
                                result.append(rqts.url)
                            elif b in rqts.text or b in rqts.content.decode('utf-8'):
                                if rqts.url in result_ufck:continue
                                result_ufck.append(rqts.url)
                        self.echo()
                    else:
                        print('\033[1;31m [-] \033[0m URL：{} 状态码不匹配：{}'.format(rqts.url,rqts.status_code))
                except Exception as r:
                    print('\033[1;31m [-] \033[0m URL:{} Error：{}'.format(rqts.url,r))
                    pass
            xianchen.acquire()

    def reay(self,fi):
        for d in fi.readlines():
            d="".join(bytes.decode(d).split('\n'))
            yield d

    def echo(self):
        if len(result_ufck)==0:
            for k in result:
                print('\033[1;32m [+] \33[0m ok_URL:{}'.format(k))
                print(k,file=open('save.txt','a'))
                result.clear()
        else:
                for n in result_ufck:
                    print('\033[1;31m [-] \033[0m no_URL:{}'.format(n))


if __name__ == '__main__':
    banner()
    user=input('要爆破的URL：').rstrip('/')
    jb=baopo(rhost='{}'.format(user))
    jb.read_config()
    jb.jiance()
