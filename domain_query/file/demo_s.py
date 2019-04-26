import gevent
from gevent import monkey;monkey.patch_all()
import socket
from multiprocessing import Process

port_lit=[80,443,8080]
texts=[]

class domain_bao:
    def __init__(self,headers):
        self.headers=headers

    def demo(self,doamin):
        g=socket.gethostbyname_ex(doamin)
        if domain_ex in g[0]:
            s=socket.socket()
            try:
                for k in port_lit:
                    s.connect((g[0],k))
                    zk='域名:{}'.format(g[0])
                    if zk in texts:continue
                    texts.append(zk)
            except:
                pass

        else:
            pass

        self.echo()

    def echo(self):
        if len(texts)>0:
            for t in texts:
                print(t)


    def xc(self,ld):
        go=[]
        for l in ld:
            go.append(gevent.spawn(self.demo,l))

        gevent.joinall(go)

    def djc(self):
        global domain_ex
        domain_ex='huazhu.com'
        doamin_list=[]
        calc=0
        with open('/root/Jb/domain_query/file/phpinfo_me_dict.txt','r') as r:
            for g in r.readlines():
                qc="".join(g.split('\n'))+'.'+domain_ex
                doamin_list.append(qc)
                calc+=1
                if calc==500:
                    p=Process(target=self.xc,args=(doamin_list,))
                    p.start()
                    doamin_list.clear()
                    calc=0

if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    obj=domain_bao(headers=headers)
    obj.djc()