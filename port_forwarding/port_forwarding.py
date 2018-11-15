import socket
import threading
import os

server_host='127.0.0.1'
server_port=4446

client_host='127.0.0.1'
client_port=80
def log(logs):
    print('[+] log:',logs)


log('{}:{} -> {}:{}'.format(client_host,client_port,server_host,server_port))
def jianting(host,port,client_host,client_port):
    try:
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(5)

        ss,addr=server.accept()
        client.connect((client_host,client_port))
        while True:
            mg = ss.recv(1024)
            if not mg:
                break
            client.sendall(mg)
            log(mg)

            buf=client.recv(1024)
            if not buf:
                break
            ss.sendall(buf)
            log(buf)


    except Exception as error:
        print('[-]Error {}'.format(error))
        log('[-]Error {}'.format(error))
        exit()



def run():
    s=threading.Thread(target=jianting,args=(server_host,server_port,client_host,client_port))
    s.start()
if __name__ == '__main__':
    run()