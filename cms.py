import requests
import json
import hashlib
import os
import optparse
def main():
    usage="[-q MD5DE-CMS] " \
          "[- p URL gets CMS]"
    parser=optparse.OptionParser(usage)
    parser.add_option('-q',dest='md5',help='md5 cms')
    parser.add_option('-p',dest='url',help='url cms')
    (options,args)=parser.parse_args()
    if options.md5:
        log=options.md5
        panduan(log)
    elif options.url:
        log2=options.url
        panduan2(log2)
    else:
        parser.print_help()


def op():
    global lr
    if os.path.exists('data.json'):
        print('[+]Existing data.json file')
        js=open('data.json','r')
        lr=json.load(js,encoding='utf-8')
    else:
        print('[-]Not data.json')
        exit()

op()

def panduan(log):
    global headers
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    for b in lr:
        url = log.rstrip('/') + b["url"]
        rest = requests.get(url=url, headers=headers, timeout=5)
        text = rest.text
        if rest.status_code != 200:
            print('[-]Not Found 200', rest.url)
        md5=hashlib.md5()
        md5.update(text.encode('utf-8'))
        g=md5.hexdigest()
        print(g)
        if g == b["md5"]:
            print("[+]CMS:",b["name"],"url:",b["url"])
            print("[+]CMS:",b["name"],"url:",b["url"],file=open('cms.txt','w'))
        else:
            print('[-]not md5:',b["md5"])



def panduan2(log2):
    for w in lr:
      headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
      url = log2.rstrip('/') + w["url"]
      rest=requests.get(url=url,headers=headers,timeout=5)
      text=rest.text
      if rest.status_code !=200:
          pass
      if w["re"]:
          if(text.find(w["re"]) != -1):
              print('[+]CMS:',w["name"],"url:",w["url"])
              print('[+]CMS:', w["name"], "url:", w["url"],file=open('cms.txt','w'))

if __name__ == '__main__':
    main()