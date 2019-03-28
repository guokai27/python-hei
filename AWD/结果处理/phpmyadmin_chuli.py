#author:九世
#time:2019/3/28

import os
import re

jg=[]

class Chuli:
    def __init__(self,path):
        self.path=path
    def cl(self):
        dk=open(self.path,'r',encoding='utf-8')
        for j in dk.readlines():
            qc="".join(j.split('\n'))
            host=re.findall('(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',qc)
            jh=str(host[0]).replace("('",'').replace("')",'').replace(',','.').replace("'",'').replace(' ','')
            print('host={}'.format(jh),file=open('cl.txt','a'))
            usern=re.findall('用户名:.* 密',qc)
            print('user={}'.format(str(usern[0]).replace('用户名:','').replace('密','')),file=open('cl.txt','a'))
            pwd=re.findall('密码:.*',qc)
            pwds=str(pwd[0]).replace('密码:','')
            print('password={}'.format(pwds),file=open('cl.txt','a'))
        print('[+] 处理完成')
if __name__ == '__main__':
    user=input('输入你的路径:')
    if os.path.exists(user):
        print('[+] 找到文件:{}'.format(user))
        obj=Chuli(user)
        obj.cl()
    else:
        print('[-] 文件不存在')