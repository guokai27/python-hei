#uathor:九世
#time:2019/429

import gevent
from gevent import monkey;monkey.patch_all()
import requests
from multiprocessing import Process
import os
import optparse
import chardet
import time

black_list = []
oklit=[]


class pirbs:
    def __init__(self,headers):
        self.headers=headers

    def parse(self):
        usage='usage:[-u 地址] [-f 文件夹] [-s 匹配的状态码] 【- b 黑名单】 [-t 延时]'
        parser=optparse.OptionParser(usage)
        parser.add_option('-u',dest='url',help='指定目标url')
        parser.add_option('-f',dest='file',help='存放目录字典的文件夹')
        parser.add_option('-s',dest='status_code',help='匹配指定的状态码')
        parser.add_option('-b',dest='black',help='过滤掉黑名单里的字符')
        parser.add_option('-t',dest='sleeps',help='扫描延时')
        (option,args)=parser.parse_args()
        if option.url and option.file and option.status_code and option.black and option.sleeps:
            url=option.url
            file=option.file
            code=option.status_code
            black=option.black
            sleeps=option.sleeps
            self.djc(url,file,code,black,sleeps)
        else:
            parser.print_help()
            exit()

    def webscan(self,url,ps,code,sleeps):
        urls='{}{}'.format(str(url).strip().rstrip('/'),ps)
        try:
            rqt=requests.get(url=urls,headers=self.headers,timeout=3)
            g=chardet.detect(rqt.content)
            if rqt.status_code==int(code):
                for k in black_list:
                    if k in rqt.content.decode(g['encoding']) or k in rqt.text:
                        print('-->:{} 关键字:{}'.format(urls,k))
                        oklit.append(urls)
                        break

                if urls not in oklit:
                    print('+找到路径:{}'.format(urls))
                    print('+找到路径:{}'.format(urls),file=open('save.txt','a',encoding='utf-8'))
            else:
                print('--- {} 状态码:{}'.format(urls,rqt.status_code))

            time.sleep(int(sleeps))
        except requests.exceptions.ConnectionError:
            print('-- 请检查是否因请求过快，被封IP')
            exit()

    def xc(self,url,path,code,sleeps):
        xw=[]
        for f in path:
            xw.append(gevent.spawn(self.webscan,url,f,code,sleeps))

        gevent.joinall(xw)

    def djc(self,url,file,code,black,sleeps):
        if os.path.exists(black):
            print('[+] 成功加载黑名单')
            dk=open('{}'.format(black),'r')
            for b in dk.readlines():
                qc="".join(b.split('\n'))
                black_list.append(qc)
            print(black_list)
        else:
            print('[-] 找不到黑名单')
            exit()

        if os.path.exists(file):
            path_list=[]
            calc=0
            print('[+] 找到了字典文件夹')
            dg=os.listdir(file)
            for d in dg:
                dk=open('{}{}'.format(file,d),'r')
                for r in dk.readlines():
                    qc="".join(r.split('\n'))
                    calc+=1
                    path_list.append(qc)
                    if calc == 10000:
                        p = Process(target=self.xc, args=(url, path_list,code,sleeps))
                        p.start()
                        path_list.clear()
                        calc = 0



        else:
            print('[-] 找不到字典文件夹')
            exit()

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    obj=pirbs(headers=headers)
    obj.parse()