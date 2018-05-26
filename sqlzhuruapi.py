import requests
import json
import platform
import os
logo="#sqlmap api制作" \
     "#九世制作"
print(logo)
print('[1]Manually open sqlmapapi')
print('[2]Automatically open sqlmapapi')
while True:
    start=input("Please choose:")
    if start == "1":
        print('[*]You choose to open sqlmapapi manually')
        break
    elif start == "2":
        print('[*]You choose to automatically open sqlmapapi')
        os.system('sqlmapapi.py -s')
        break
    else:
        print('[-]There is no choice')
        continue

while True:
    user=input('Please enter the web site you want to scan:')
    if user==None:
        print('[-]You have nothing to enter')
        continue
    else:
        break

vsersion=platform.uname()
for p in vsersion:
    print('[*]Your operating system type is:{}'.format(p))

print(' ')

def sqlmap(host):
    urlnew="http://127.0.0.1:8775/task/new"
    urlscan="http://127.0.0.1:8775/scan/"
    headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
    pd=requests.get(url=urlnew,headers=headers)
    print('[*]New task')
    jsons=pd.json()
    print("[*]id:",jsons['taskid'])
    print("[*]success:",jsons["success"])
    id=jsons['taskid']
    scan=urlscan+id+"/start"
    print("[*]scanurl:",scan)
    data=json.dumps({"url":"{}".format(host)})
    headerss={"Content-Type":"application/json"}
    scans=requests.post(url=scan,headers=headerss,data=data)
    swq=scans.json()
    print('--------SCAN-----------')
    print('[*]scanid:',swq["engineid"])
    print('[*]scansuccess:',swq["success"])
    print('--------STATUS---------')
    status="http://127.0.0.1:8775/scan/{}/status".format(id)
    print(status)
    while True:
        staw=requests.get(url=status,headers=headers)
        if staw.json()['status'] == 'terminated':
            datas=requests.get(url='http://127.0.0.1:8775/scan/{}/data'.format(id))
            dat=datas.json()['data']
            print('[*]data:',dat)
            break
        elif staw.json()['status'] == 'running':
            continue

sqlmap(user.strip())