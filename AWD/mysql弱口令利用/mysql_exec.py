#author:九世
#time:2019/3/28

import os
import requests
import re

hosts=[]
username=[]
passwords=[]
datast=[]

class Exec:
    def __init__(self,headers):
        self.headers=headers
    def dan(self):
        user=input('IP:')
        user2=input('username:')
        user3=input('password:')
        user4=input('command:')
        data={'pwd':'admin','host':user,'user':user2,'password':user3,'command':user4}
        urls='http://127.0.0.1/exec.php'
        rgt=requests.post(url=urls,headers=self.headers,data=data)
        print(rgt.text)
    def shuang(self):
        usq=input('请输入文件路径:')
        if os.path.exists(usq):
            print('[+] 找到文件:{}'.format(usq))
            dk=open(usq,'r',encoding='utf-8')
            for v in dk.readlines():
                sc="".join(v.split('\n'))
                host=re.findall('host=.*',sc)
                user=re.findall('user=.*',sc)
                pwd=re.findall('password=.*',sc)
                for k in host:
                    hosts.append(str(k).replace('host=',''))

                for u in user:
                    username.append(str(u).replace('user=','').strip())

                for p in pwd:
                    passwords.append(str(p).replace('password=',''))

            user = input('command:')
            for g in range(0,len(hosts)):
                data = {'pwd': 'admin', 'host': hosts[g], 'user': username[g], 'password': passwords[g], 'command': user}
                datast.append(data)

            for d in datast:
                urls = 'http://127.0.0.1/exec.php'
                rgt = requests.post(url=urls, headers=self.headers, data=d)
                print(rgt.text)
        else:
            print('[-] 找不到文件')

if __name__ == '__main__':
    headers = {'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    obj=Exec(headers)
    cl=['1.单个利用','2.批量利用']
    clt={'1':obj.dan,'2':obj.shuang}
    for c in cl:
        print(c)

    user=input('>')
    if user in clt:
        clt[user]()



