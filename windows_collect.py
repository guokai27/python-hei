import os

def collect():
    xj=open('save.txt','w')
    xj.close()

    print('[+]什么是操作系统和架构？它缺少任何补丁吗？')
    systeminfo=os.popen('systeminfo')
    wmic_qfe=os.popen('wmic qfe')
    for s in systeminfo:
        print(s,file=open('save.txt','a'))
    for c in wmic_qfe:
        print(c,file=open('save.txt','a'))

    print('[+]环境变量有什么有趣的吗？域控制器在LOGONSERVER？')
    set=os.popen('set')
    #Get_chiditem=os.popen('Get-ChildItem Env: | ft Key,Value')
    for e in set:
        print(e,file=open('save.txt','a'))
    #for t in Get_chiditem:
        #print(t,file=open('save.txt','a'))

    print('[+]还有其他连接的驱动器吗？')
    net_use=os.popen('net use')
    wmic_log=os.popen('wmic logicaldisk get caption,description,providername')
    #psd=os.popen('Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| ft Name,Root')
    for ne in net_use:
        print(ne,file=open('save.txt','a'))
    for g in wmic_log:
        print(g,file=open('save.txt','a'))
    #for d in psd:
        #print(d,file=open('save.txt','a'))

    print('[+]你是谁？')
    whoami=os.popen('whoami')
    username=os.popen('echo %USERNAME%')
    for whoa in whoami:
        print(whoa,file=open('save.txt','a'))
    for m in username:
        print(m,file=open('save.txt','a'))

    print('[+]任何有趣的用户权限？注意：“状态”列并不表示用户具有或无权访问此权限。如果列出了该权限，则该用户拥有该权限。')
    priv=os.popen('whoami /priv')
    for i in priv:
        print(i,file=open('save.txt','a'))

    print('[+]用户在系统上有什么用途？任何未清理的旧用户配置文件？')
    ur=os.popen('net users')
    bw=os.popen('dir /b /ad "C:/Users/"')
    #bs=os.popen('dir /b /ad "C:/Documents and Settings/" # Windows XP and below')
    for r in ur:
        print(r,file=open('save.txt','a'))
        for w in bw:
            print(w,file=open('save.txt','a'))
            #for s in bs:
                #print(s,file=open('save.txt','a'))

    print('[+]还有其他人登录吗？')
    qwinsta=os.popen('qwinsta')
    for w in qwinsta:
        print(w,file=open('save.txt','a'))

    print('[+]系统上有哪些组？')
    net_localgroup=os.popen('net localgroup')
    for group in net_localgroup:
        print(group,file=open('save.txt','a'))

    print('[+]Administrators组中是否有任何用户？')
    net_localgroup_Administrators=os.popen('net localgroup Administrators')
    for administrator in net_localgroup_Administrators:
        print(administrator,file=open('save.txt','a'))

    print('[+]用户自动登录注册表中的任何内容？')
    reg_query=os.popen('reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"')
    for v in reg_query:
        print(v,file=open('save.txt','a'))

    print('[+]在Credential Manager中有什么有趣的东西吗？')
    cmdkey_list=os.popen('cmdkey /list')
    for l in cmdkey_list:
        print(l,file=open('save.txt','a'))

    print('[+]cmdkey /list我们可以访问SAM和SYSTEM文件吗？')
    lg=['%SYSTEMROOT%/repair/SAM','%SYSTEMROOT%/System32/config/RegBack/SAM','%SYSTEMROOT%/System32/config/SAM','%SYSTEMROOT%/repair/system','%SYSTEMROOT%/System32/config/SYSTEM','%SYSTEMROOT%/System32/config/RegBack/system']
    for k in lg:
        system=os.popen(k)
        for q in system:
            print(q,file=open('save.txt','a'))

    print('[+]安装了什么软件？')
    rj=['dir /a "C:\Program Files"','dir /a "C:\Program Files (x86)"','reg query HKEY_LOCAL_MACHINE\SOFTWARE']
    for j in rj:
        qw=os.popen(j)
        for w in qw:
            print(w,file=open('save.txt','a'))

    print('[+]程序文件夹中每个人或用户的完全权限？')
    icacls=['icacls "C:\Program Files\*" 2>nul','icacls "C:\Program Files (x86)\*" 2>nul','icacls "C:\Program Files\*" 2>nul ','icacls "C:\Program Files (x86)\*"']
    for aw in icacls:
        qdw=os.popen(aw)
        for rs in qdw:
            print(rs,file=open('save.txt','a'))


    print('[+]系统上正在运行的进程/服务是什么？内部服务没有暴露吗？如果是这样，我们可以打开它吗？')
    tasklist=['tasklist /svc','tasklist /v','net start','sc query',]
    for t in tasklist:
        wx=os.popen(t)
        for p in wx:
            print(p,file=open('save.txt','a'))

    print('[+]有没有不带引号的服务路径？')
    wmcs=os.popen('wmic service get name,displayname,pathname,startmode 2>nul |findstr /i "Auto" 2>nul |findstr /i /v "C:\Windows\\" 2>nul |findstr /i /v """')
    for m in wmcs:
        print(m,file=open('save.txt','a'))

    print('[+]那里有什么预定的任务？什么定制实施？')
    xw=os.popen('schtasks /query /fo LIST 2>nul | findstr TaskName')
    print(xw,file=open('save.txt','a'))

    print('[+]启动时跑了什么？')
    qz=['wmic startup get caption,command','reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run','reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce','reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run','reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce','dir "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"','dir "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"']
    for z in qz:
        xq=os.popen(z)
        for r in xq:
            print(r,file=open('save.txt','a'))

    print('[+]连接了哪些NIC？有多个网络吗？')
    ipconfig_all=os.popen('ipconfig /all')
    for all in ipconfig_all:
        print(all,file=open('save.txt','a'))

    print('[+]我们有什么路线？')
    xpo=os.popen('route print')
    for o in xpo:
        print(o,file=open('save.txt','a'))

    print('[+]ARP缓存中的任何内容？')
    arp=os.popen('arp -a')
    for p in arp:
        print(p,file=open('save.txt','a'))

    print('[+]是否有与其他主机的连接？')
    sw=os.popen('netstat -ano')
    for b in sw:
        print(b,file=open('save.txt','a'))

    print('[+]防火墙是否已打开？如果是这样配置的是什么？')
    fq=['netsh firewall show state','netsh firewall show config','netsh advfirewall firewall show rule name=all','netsh advfirewall export "firewall.txt"']
    for u in fq:
        fhq=os.popen(u)
        for f in fhq:
            print(f,file=open('save.txt','a'))

    print('[+]还有其他有趣的界面配置吗？')
    netsh_dump=os.popen('netsh dump')
    for ump in netsh_dump:
        print(ump,file=open('save.txt','a'))

    print('[+]注册表中的任何密码？')
    lv=['reg query HKCU /f password /t REG_SZ /s','reg query HKLM /f password /t REG_SZ /s ']
    for pasw in lv:
        passwd=os.popen(pasw)
        for pd in passwd:
            print(pd,file=open('save.txt','a'))

    print('[+]是否有可用的sysprep或无人值守文件？')
    zi=os.popen('dir /s *sysprep.inf *sysprep.xml *unattended.xml *unattend.xml *unattend.txt 2>nul')
    for nb in zi:
        print(nb,file=open('save.txt','a'))

    print('[+]有待观察的有趣文件吗？可能在用户目录（桌面，文档等）中？')
    sl=os.popen('dir /s *pass* == *vnc* == *.config* 2>nul')
    for lw in sl:
        print(lw,file=open('save.txt','a'))
    print('')
    print('')

    print('[*]判断是否存在以下路径')
    lss=[]
    if os.path.exists('list.txt'):
        print('[+]存在list.txt')
    else:
        print('[-]不存在list.txt')
        exit()

    dk=open('list.txt','r')
    for r in dk.readlines():
        qk="".join(r.split('\n'))
        lss.append(qk)

    for g in lss:
        if os.path.exists(g):
            print('[+]存在 {}'.format(g))
        else:
            print('[-]不存在{}'.format(g))

collect()