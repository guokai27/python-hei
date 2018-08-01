import os


ml=['uname -a','cat /etc/issue','hostname','cat /etc/hosts','who',"awk -F ':' '{print $1,$3,$4,$6;}' /etc/passwd",'cat /etc/group','cat /etc/shadow','grep -v -E "^#" /etc/passwd','cat ~/.bash_history','w','netstat','ps -aux','dpkg -l','netstat -antpu','arp -a','uname -a 2>/dev/null','hostname','lastlog','for i in $(cat /etc/passwd 2>/dev/null',"grep -v '^[^:]*:[x]' /etc/passwd 2>/dev/null",'grep -v "^#" /etc/passwd','cat /etc/shadow 2>/dev/null','cat /etc/master.passwd 2>/dev/null','echo ''sudo -S -l 2>/dev/null','ls -ahl /root/ 2>/dev/null','ls -ahl /home/ 2>/dev/null','find / -writable -not -user \`whoami\` -type f -not -path "/proc/*" -exec ls -al {} \; 2>/dev/null','find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts" -o -name "authorized_keys" 2>/dev/null |xargs -r ls','''grep "PermitRootLogin " /etc/ssh/sshd_config 2>/dev/null | grep -v "#" | awk '{print  $2}''','echo $PATH 2>/dev/null','cat /etc/shells 2>/dev/null','cat /etc/login.defs 2>/dev/null | grep "PASS_MAX_DAYS\|PASS_MIN_DAYS\|PASS_WARN_AGE\|ENCRYPT_METHOD" 2>/dev/null | grep -v "#" 2>/dev/null','ls -la /etc/cron* 2>/dev/null','cat /etc/crontab 2>/dev/null','cat /etc/passwd | cut -d ":" -f 1 | xargs -n1 crontab -l -u 2>/dev/null','cat /etc/resolv.conf 2>/dev/null"','route 2>/dev/null','netstat -antp 2>/dev/null','netstat -anup 2>/dev/null','ps aux 2>/dev/null',"ps aux","'ls -la /etc/init.d 2>/dev/null'","find /etc/init.d/ \! -uid 0 -type f 2>/dev/null","mysql --version 2>/dev/null","sudo -V 2>/dev/null","mysqladmin -uroot -proot version 2>/dev/null","psql -V 2>/dev/null","apache2 -v 2>/dev/null; httpd -v 2>/dev/null","""awk '{sub(/.*\export /,"")}1""",'ifconfig']
shuomin=['内核(是否为x64还是x86)','版本','主机名','hosts','目前登录系统的用户信息','获取用户名','获取用户组','获取hash','列出超级用户','查看用户操作','获取在线用户','端口','进程','程序','敏感文件','交互通信的ip','arp缓存','基础内核信息','主机名','最后用户登录的信息','列出所有用户的组','查询是否有hash存储在/etc/passwd(*nix中)','根据uid列出本地用户','读取shadow文件','bsd的shadow文件','能够sudo不需要提供密码','检查root目录是否存在','显示home目录情况','寻找文件我们能写但是不属于我们的文件','寻找ssh公钥','root是否能登录ssh,如果返回yes则可以登录','环境变量','列出能用的shells','hash的密码加密政策','所有的计划任务配置文件','获取计划任务内容','获取每个用户的计划任务','dns设置','路由配置','正在监听的tcp端口','udp端口','正在运行的程序','查看进程路径和权限','获取inetd.conf文件(监视网络的守护进程)','列举各种服务的管理脚本','寻找不是root的','获取mysql版本','获取sudo版本','测试root/root能否登录','postgres版本','apache详情','apache的运行用户','ip']

def poc():
    xk = open('save.txt', 'w')
    xk.close()
    for i in range(0,len(ml)):
        zx=os.popen(ml[i])
        print('[+]{}'.format(shuomin[i]))
        print('[+]{}'.format(shuomin[i]),file=open('save.txt','a'))
        for z in zx:
            print(z,file=open('save.txt','a'))
poc()