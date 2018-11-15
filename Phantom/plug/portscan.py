import nmap
import threading

xj=open('save.txt','w')
xj.close()
def portscan():
    user=input('IP:')
    port=input('port:')
    nm = nmap.PortScanner()
    ret = nm.scan('{}'.format(user), '{}'.format(port))
    for host in nm.all_hosts():
        print('[+] Host:{}'.format(user))
        ld=nm[host]['tcp']
        for y in range(1,1024):
            try:
                number=ld[y]
                print('[+] ',y,number['state'],'',number['name'],number['version'])
                print(number['name'],file=open('save.txt','a'))
            except:
                pass

portscan()