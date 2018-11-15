import os
def zx():
    ip=input('ip:')
    print('[+] nmap script-all')
    os.system('nmap --script all {}'.format(ip))
zx()