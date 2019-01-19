#coding:utf-8
'''
@author:九世
@time:2019/1/1
'''
import requests
def search():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='https://music.163.com/#/search/m/?s=%E5%A4%8F%E8%87%B3%E6%9C%AA%E8%87%B3&type=1'
    rqt=requests.get(url=url,headers=headers)
    print(rqt.text)
search()