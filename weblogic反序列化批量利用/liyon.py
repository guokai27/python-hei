#author:九世
#time:2019/2/6

class Weblogic:
    def read(self,files):
        dk=open(files,'r')
        for r in dk:
            sc="".join(r.split('\n'))
            yield sc

    def jiance(self):
        faq=__import__('plugin.jiance',fromlist=True)
        faq2=__import__('plugin.filepd',fromlist=True)
        daoru=getattr(faq,'reqt')
        daoru2=getattr(faq2,'pd')
        xz=input('文件或单个(单个输入1/批量检测输入2):')
        if xz=='1':
            user=input('url:').rstrip('/').strip()
            fang=daoru(user)
            print(fang)
        elif xz=='2':
            user=input('file:')
            file_pd=daoru2(user)
            if file_pd==1:
                for v in self.read(user):
                    fnag=daoru(v)
                    print(fnag)
            elif file_pd==0:
                print('[-] 不存在此文件')
        else:
            print('[-] 没有此选择')

    def exp(self):
        jq=__import__('plugin.exploit',fromlist=True)
        jq2=__import__('plugin.filepd',fromlist=True)
        gt=getattr(jq,'exploit')
        gt2=getattr(jq2,'pd')
        xz=input('文件或单个(单个输入1/批量检测输入2):')
        if xz=='1':
            users=input('IP:')
            prott=input('port:')
            gt(users,int(prott),0)
        elif xz=='2':
            mz=input('file:')
            fz=gt2(mz)
            if fz==1:
                import re
                for l in self.read(mz):
                    host=re.findall('.*:',str(l))
                    ports=re.findall(':.*',str(l))
                    hosts=str(host[0]).replace(':','').strip()
                    port=str(ports[0]).replace(':','').strip()
                    gt(hosts,int(port),0)
            else:
                print('[-] 不存在此文件')
        else:
            print('[-] 不存在此选择')

    def zoomeye(self):
        ipo=__import__('plugin.search',fromlist=True)
        search=getattr(ipo,'zoomeye')
        search()

    def portscan(self):
        jr=__import__('plugin.portscan',fromlist=True)
        pd=__import__('plugin.filepd',fromlist=True)
        port=getattr(jr,'portscan')
        jc=getattr(pd,'pd')
        xz=input('单个或批量(单个检测输入1批量检测输入2):')
        if xz=='1':
            user=input('IP:')
            port(user,7001)

        elif xz=='2':
            user=input('file:')
            pds=jc(user)
            if pds==1:
                for v in self.read(user):
                    port(v,7001)
            else:
                print('[-] 不存在此文件')
        else:
            print('[-] 不存在此选项')


if __name__ == '__main__':
    obj=Weblogic()
    print('weblogic 反序列化检测 by 九世')
    jg=['1.通过网页关键字来判断是否为weblogic','2.检测是否存在weblogic反序列化','3.从zoomeye采集目标','4.7001端口扫描判断是否开放']
    jgs={'1':obj.jiance,'2':obj.exp,'3':obj.zoomeye,'4':obj.portscan}
    while True:
        for j in jg:
            print(j)

        user=input('选择：')
        if user in jgs:
            jgs.get(user)()
            print('')
        else:
            print('[-] 不存在这个选择')
            continue