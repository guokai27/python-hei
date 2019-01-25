#author:九世
#time:2019/1/25

import os
import requests

filelist=[]
class Files:
    def __init__(self,url,headers):
        self.url=url
        self.headers=headers

    def rqt(self):
        print('[h] search file in windows data')
        rqt=requests.get(url=self.url,headers=self.headers)
        for b in rqt.text.split('\n'):
            filelist.append(b)

        self.panduan()
    def panduan(self):
        for f in filelist:
            if os.path.exists(f):
                print('[a] Found path:{}'.format(f))
if __name__ == '__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    wen=input('url:')
    obj=Files(headers=headers,url=wen.strip())
    obj.rqt()