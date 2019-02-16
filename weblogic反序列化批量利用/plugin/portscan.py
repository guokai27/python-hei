#author:九世
#time:2019/2/16

import socket

def portscan(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip,port))
        print('[+] {}:{}/open'.format(ip,port))
        print('{}:{}'.format(ip,port),file=open('file/portscan.txt','a',encoding='utf-8'))
    except:
        pass

