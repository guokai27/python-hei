#author:九世
#time:2019/3/27

import winreg
import os
import re

class Close:
    def __init__(self,command):
        self.command=command
    def commands(self):
        print('[+] 关闭445端口设置完成后需要重启计算机(按任意键继续/N退出)')
        user=input('>')
        if user=='N':
            exit()
        zx=os.popen(self.command[0])
        zhi=re.findall('[A-Z]{1,}[$]',zx.read())
        for v in zhi:
            dele=os.popen('{} {} /del'.format(self.command[0],v))
            print(dele.read())

        closes=os.popen('net stop Server')
        jyon=os.popen('sc config LanmanServer start= disabled')
        print('[+] 关闭并禁用Server服务')
        print(closes.read())
        print(jyon.read())
        print('[+] 1 秒后重启计算机')
        reboot=os.popen('shutdown -t 1 -r')
        reboot.read()

    def dreg(self):
        jc=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'System\CurrentControlSet\Services\LanmanServer\Parameters',0,winreg.KEY_ALL_ACCESS)
        jc2=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'System\CurrentControlSet\Control\Lsa',0,winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(jc,'AutoShareServer',1,winreg.REG_DWORD,0)
        winreg.SetValueEx(jc, 'AutoShareWKs', 1, winreg.REG_DWORD, 0)
        winreg.SetValueEx(jc2,'restrictanonymous',1,winreg.REG_DWORD,1)
        print('[+] 永久关闭盘符的默认共享，设置HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanmanServer\Parameters里的AutoShareServer键值为:0')
        print('[+] 永久关闭admin$的默认共享，设置HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanmanServer\Parameters里的AutoShareWKs键值为:0')
        print('[+] 永久关闭IPC$的默认共享，设置HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa里的restrictanonymous键值为1')

if __name__ == '__main__':
    comman=['net share']
    obj=Close(command=comman)
    obj.commands()
    obj.dreg()
