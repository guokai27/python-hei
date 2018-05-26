import requests,tqdm,time,optparse
def main():
    usage='dianjijieci.py [-u url]'
    parser=optparse.OptionParser(usage)
    parser.add_option('-u',dest='url',help='The web site to be tested URL')
    (options,args)=parser.parse_args()
    if options.url:
        url=options.url
        jiechi(url)
    else:
        parser.print_help()
def jiechi(url):
    urls="{}".format(url)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    reqst=requests.get(url=urls,headers=headers,timeout=6)
    if reqst.status_code == 200:
      print('[+]Target stability')
      try:
          hea=reqst.headers
          print(hea['X-FRAME-OPTIONS'])
          print('[n]X-FRAME-OPTIONS header, no click hijacking vulnerability can be used')
      except:
          print('[+]There is no X-FRAME-OPTIONS header. There is a clicking hijacking vulnerability')
          print('[!]Remind:It may be a defense against JS. Please test it yourself')
    else:
        print('[n]bjective instability')

if __name__ == '__main__':
    main()