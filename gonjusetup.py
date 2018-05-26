import os
import time
import threading
import re
import optparse
logo="######################" \
     "#此脚本将安装以下所有工具 #" \
     "#制作人：即刻安全-九世   # " \
     "#####################           "
print(logo)
def main():
    usage="-x 安装信息收集工具包" \
          "-s 数据库扫描器"
    parser=optparse.OptionParser(usage)
    parser.add_option('-x',action='store_true',dest='xs',help='-x')
    parser.add_option('-s',action='store_true',dest='sj',help='-s')
    (options,args)=parser.parse_args()
    if options.xs:
        x=threading.Thread(target=xs,args=())
        x.start()
    elif options.sj:
        s=threading.Thread(target=sj,args=())
        s.start()
    else:
        parser.print_help()
        exit()

def xs():
    vis=open('mulu.txt','r').read()
    print('[*]将安装:')
    print(vis)
    time.sleep(1)
    print('[+]清空')
    os.system('clear')

    print('[+]开始安装')
    vss=open('mulu.txt','r')
    for w in vss.readlines():
        sq=re.findall('[a-zA-z]+://[^\s]*',w)
        for w in sq:
            print('[+]正在安装:{}'.format(w))
            os.system('git clone {}'.format(w))
            print('')

if __name__ == '__main__':
    main()