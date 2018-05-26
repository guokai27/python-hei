import requests,time
def poc():
    user=input('Please enter the web site to be tested:')
    user2=input('Please enter the parameters you want to bring in:')
    values=user2.strip().split('?')[-1]
    params={}
    for line in values.split('&'):
        key,value=line.split('=',1)
        params[key]=value
    print('URL:',user)
    print('The parameters you have taken are:',params)
    time.sleep(0.2)
    print('If you want to change the parameters, please enter y')
    print('Do not need to change to enter n')
    user3=input('Do you want to change your parameters[y/n]:')
    if user3 == 'y':
        while True:
          print('Please enter the name of the parameter you want to change{name: value}')
          print(params)
          user4=input('Please fill in the name:')
          user5=input('Please enter the value you want to change:')
          params['{}'.format(user4)]='{}'.format(user5)
          print('The change is done, and your current parameter is',params)
          user6=input('Do you want to continue to love the parameters more[y/n]?:')
          if user6 == 'y':
              continue
          elif user6 == 'n':
              break
          elif user6 == '':
              break

    url=user.strip()
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    rest=requests.get(url=url,headers=headers,timeout=6,params=params, allow_redirects=False)
    print('Http_code:',rest.status_code)
    print(rest.headers)
    try:
        print(rest.headers['Location'])
        if rest.headers['Location'] == 'http://www.baidu.com':
            print('[*]There is a URL redirection vulnerability in this link')
        else:
            print('[+]There is no URL redirection vulnerability in this link')
    except:
        print('[-]not Location head')
poc()
