import os

def search():
    print('[+] searchsploit')
    dk=open('save.txt','r')
    for r in dk.readlines():
        qc="".join(r.split('\n'))
        os.system('searchsploit {}'.format(qc))
search()