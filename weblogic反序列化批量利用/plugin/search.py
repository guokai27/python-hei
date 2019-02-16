#author:九世
#time:2019/2/16

import requests
import configparser

cn=configparser.ConfigParser()
cn.read('config/search.ini')
zoomeye_username=cn.get('zoomeye','username')
zoomeye_password=cn.get('zoomeye','password')
zoomeye_page=cn.get('zoomeye','page')
zoomeye_yufa=cn.get('zoomeye','yufa')
def zoomeye():
    url_login='https://api.zoomeye.org/user/login'
    data={'username':zoomeye_username,'password':zoomeye_password}
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    rqt=requests.post(url=url_login,headers=headers,json=data)
    access_token=rqt.json()['access_token']
    headers_2={'Authorization': 'JWT {}'.format(access_token)}
    print('[+] zoomeye抓取到的IP')
    for p in range(1,int(zoomeye_page)):
        url_search='https://api.zoomeye.org/host/search?query=port:21%20city:beijing&page={}&facets={}'.format(p,zoomeye_yufa)
        rqts=requests.get(url=url_search,headers=headers_2)
        jg=rqts.json()['matches']
        for g in jg:
            print(g['ip'])
            print(g['ip'],file=open('file/zoomeye.txt','a',encoding='utf-8'))