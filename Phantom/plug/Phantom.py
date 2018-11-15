import sys
import platform
import os
sys.path.append('Python/Phantom/plug')
banner='''
 ____    __                       __                          
/\  _`\ /\ \                     /\ \__                       
\ \ \L\ \ \ \___      __      ___\ \ ,_\   ___     ___ ___    
 \ \ ,__/\ \  _ `\  /'__`\  /' _ `\ \ \/  / __`\ /' __` __`\  
  \ \ \/  \ \ \ \ \/\ \L\.\_/\ \/\ \ \ \_/\ \L\ \/\ \/\ \/\ \ 
   \ \_\   \ \_\ \_\ \__/.\_\ \_\ \_\ \__\ \____/\ \_\ \_\ \_/
    \/_/    \/_/\/_/\/__/\/_/\/_/\/_/\/__/\/___/  \/_/\/_/\/_/
'''
print(banner)
def phantom():
    while True:
        alist=['[1] portscan','[2] nmap_script','[3] searchsploit','[4] baidu_search','[5] Sensitive path scanning','[6] CSRF_scanner']
        for v in alist:
            print(v)
        getlist={'1':scan,
                 '2':nmap_script,
                 '3':searchsploit,
                 '4':baidu_search,
                 '5':Sensitivepathscanning,
                 '6':csrf}


        user=input('Choice:')

        if user in getlist:
            getlist.get(user)()

        elif user=='q':
            exit()
        else:
            continue

def scan():
    import portscan
    print('')
def nmap_script():
    import nmp_script
    print('')
def searchsploit():
    pass
def baidu_search():
    import caiji
    print('')
def Sensitivepathscanning():
    sstyr=platform.system()
    if sstyr=='Windows':
        os.system('python Route.py')
        print('')
    elif sstyr=='Linux':
        os.system('python3 Route.py')
        print('')
def csrf():
    import scanner
    print('')

if __name__ == '__main__':
    phantom()