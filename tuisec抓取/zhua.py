#author:九世
#time:2019/2/10

import requests
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import base64
from bs4 import BeautifulSoup

dk_d=[]
xin_d=[]
zon_title=[]
zon_url=[]
zon_time=[]
zrl='https://paper.tuisec.win'
gg=[]
zj=[]
username='你的邮箱'
password='你的密码'

class Reqt:
    def __init__(self,headers,url):
        self.headers=headers
        self.url=url

    def clear(self):
        xj=open('save.txt','w',encoding='utf-8')
        xj2=open('save2.txt','w',encoding='utf-8')
    def reads(self,file):
        for r in file.readlines():
            sc="".join(r.split('\n'))
            yield sc

    def reqt(self):
        try:
            rqt=requests.get(url=self.url,headers=self.headers)
            text=rqt.text
            jg=re.findall('<td><a href=".*" target="_blank">.*</a></td>',text)
            for v in jg:
                bq=BeautifulSoup(str(v),'html.parser')
                for r in bq.find_all('a'):
                    zon_title.append(r.get_text())
                    zon_url.append(zrl+r['href'])

            zz_time=re.findall('(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-8])',text)
            for z in zz_time:
                zon_time.append(str(z).replace('(','').replace(')','').replace(',','-').replace("'",'').strip())
        except Exception as r:
            print('[-] 故障：{}'.format(r))
    def sr(self):
        for w in range(0,len(zon_url)):
            rqt=requests.get(url=zon_url[w],headers=self.headers)
            strong=re.findall('原文链接：.*',rqt.text)
            for s in strong:
                bq=BeautifulSoup(str(s),'html.parser')
                for j in bq.find_all('a'):
                    js=str(base64.b64decode(j.get('href'))).replace("b'\\xfe\\n?",'').replace("'",'')
                    print('时间：{} 标题：{} 文章：{}'.format(zon_time[w], zon_title[w], js),file=open('save.txt','a',encoding='utf-8'))
                    zj.append(js)
        zon_time.clear()
        zon_title.clear()
        zon_url.clear()
    def panxie(self):
        for w in range(0,len(zon_url)):
            neiron='时间：{} 标题：{} 文章：{}'.format(zon_time[w],zon_title[w],zj[w])
            if neiron in dk_d:continue
            xin_d.append(neiron)

        for n in xin_d:
            print(n, file=open('save.txt', 'a', encoding='utf-8'))
            print(n, file=open('save2.txt', 'a', encoding='utf-8'))

        zon_time.clear()
        zon_title.clear()
        zon_url.clear()
        dk_d.clear()
        xin_d.clear()

    def email(self,user, pwd,title,text):
        try:
            print('[+] 网络连接正常')
            if title==1 and text==1:
                biaoti="九世发送今日早报"
                neiron=open('save.txt','r',encoding='utf-8').read()
            elif title==2 and text==2:
                biaoti="早报更新"
                neiron=open('save2.txt','r',encoding='utf-8').read()
                gg.clear()
            mb = ['接收邮箱']
            msg = MIMEMultipart()
            msg['Subject'] = Header('{}'.format(biaoti), 'utf-8')
            msg['From'] = Header(user)

            content = MIMEText("{}".format(neiron), 'plain', 'utf-8')
            msg.attach(content)

            s = smtplib.SMTP('smtp.sina.com')
            s.set_debuglevel(1)
            s.starttls()
            s.login(user, pwd)
            s.sendmail(user, mb, msg.as_string())
            s.close()
        except Exception as r:
            print('[-] 故障：{}'.format(r))

    def read2s(self,file2):
        dk=open(file2,'r',encoding='utf-8')
        for k in dk.readlines():
            qc="".join(k.split('\n'))
            gg.append(qc)
        if len(gg)>0:
            return 1
        else:
            return 0

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='https://paper.tuisec.win/search.jsp?keywords=&&search_by_html=title&&page=1'
    obj=Reqt(url=url,headers=headers)

    u=0
    while True:
        if u==0:
            obj.clear()
            obj.reqt()
            obj.sr()
            obj.email(user=username,pwd=password,title=1,text=1)
            u+=1

        else:
            obj.reqt()
            dk=open('save.txt','r',encoding='utf-8')
            for u in obj.reads(dk):
                dk_d.append(u)

            obj.panxie()
            dd=obj.read2s('save2.txt')
            if dd==1:
                print(1)
                obj.email(user=username,pwd=password,title=2,text=2)
                xxj=open('save2.txt','w',encoding='utf-8')
        time.sleep(5)
