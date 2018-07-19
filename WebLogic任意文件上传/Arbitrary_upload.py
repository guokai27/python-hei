import requests
import threading
import os

error=['404','Not Found','找不到','安全狗','无权访问','403']
ok=[]
bad=[]
def exploit():
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    path='/ws_utc/config.do'
    print('[+]Weblogic arbitrary file upload detection POC,data:https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247484311&idx=1&sn=14da21743a447449896292bb367a322e&chksm=96f41cfaa18395ec6182af2353ac55079ca9376ea8d2a2f8a1816c12e7e79b1081b0bc01d2fe&mpshare=1&scene=1&srcid=0719et8NMmpFCRlu8vcgqreh#rd')
    user=input('Imported files:')
    if os.path.exists(user):
        print('[+]file {} ok'.format(user))
    else:
        print('[-]Not Found {}'.format(user))
        exit()

    ops=open('{}'.format(user),'r')
    for o in ops.readlines():
        sc="".join(o.split('\n'))
        urls=sc+path
        try:
            reques=requests.get(url=urls,headers=headers,allow_redirects=False,timeout=3)
            for e in error:
                if reques.status_code==200 and e not in reques.text:
                    pd='[+]debug url:{}'.format(sc)
                    if pd in ok:continue
                    ok.append(pd)
                    print(pd)
                else:
                    nos='[-]Not debug url:{}'.format(sc)
                    if nos in bad:continue
                    bad.append(nos)
                    print(nos)
        except:
            pass
exploit()