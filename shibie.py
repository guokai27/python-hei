import os
import optparse
import re
def main():
    parser=optparse.OptionParser()
    parser.add_option('-j',dest='jiance',help='-j[file] Check all')
    parser.add_option('-7',dest='windows7',help='-7[file] inspect windows7')
    parser.add_option('-8',dest='windowsserver2008',help='-8 [file] inspect windows server 2008')
    parser.add_option('-2',dest='windowserver2012',help='-2 [file] inspect windows server 2012')
    parser.add_option('-3',dest='windowsserver2003',help='-3 [file] inspect windows server 2003')
    parser.add_option('-x',dest='windowsXP',help='-x [file] inspect windows XP')
    parser.add_option('-0',dest='windows10',help='0 [file] inspect windows 10')
    (options,args)=parser.parse_args()
    if options.jiance:
        file=options.jiance
        jiance(file)
    elif options.windows7:
        file2=options.windows7
        windows7(file2)
    elif options.windowsserver2008:
        file3=options.windowsserver2008
        windowsserver2008(file3)
    elif options.windowserver2012:
        file4=options.windowserver2012
        windowsserver2012(file4)
    elif options.windowsserver2003:
        file5=options.windowsserver2003
        windowsserver2003(file5)
    elif options.windowsXP:
        file6=options.windowsXP
        windowsxp(file6)
    elif options.windows10:
        file7=options.windows10
        windows10(file7)
    else:
        parser.print_help()
        exit()

def jiance(file):
    pd=os.path.exists(file)
    if pd == True:
        print('[*]{}existence'.format(file))
    else:
        print('[-]Sorry{}not existence'.format(file))
        exit()

    pd2=os.path.exists('list.txt')
    if pd2==True:
        print('[*]list.txt existence')
    else:
        print('[-]not existence list.txt')
        exit()

    lists=open('list.txt','r').read()
    fg=open('{}'.format(file),'r').read()
    pow="{}".format(fg)
    lgw=re.findall('KB\d+',lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]",v)

def windows7(file2):
    pd = os.path.exists(file2)
    if pd == True:
        print('[*]{}existence'.format(file2))
    else:
        print('[-]Sorry{}not existence'.format(file2))
        exit()

    pd2 = os.path.exists('windows7.txt')
    if pd2 == True:
        print('[*]windows 7.txt existence')
    else:
        print('[-]not existence windows 7.txt')
        exit()

    lists = open('windows7.txt', 'r').read()
    fg = open('{}'.format(file2), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)

def windowsserver2008(file3):
    pd = os.path.exists(file3)
    if pd == True:
        print('[*]{}existence'.format(file3))
    else:
        print('[-]Sorry{}not existence'.format(file3))
        exit()

    pd2 = os.path.exists('windows server 2008.txt')
    if pd2 == True:
        print('[*]windows server 2008.txt existence')
    else:
        print('[-]not existence windows server 2008.txt')
        exit()

    lists = open('windows server 2008.txt', 'r').read()
    fg = open('{}'.format(file3), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)

def windowsserver2012(file4):
    pd = os.path.exists(file4)
    if pd == True:
        print('[*]{}existence'.format(file4))
    else:
        print('[-]Sorry{}not existence'.format(file4))
        exit()

    pd2 = os.path.exists('windows server 2012.txt')
    if pd2 == True:
        print('[*]windows server 2012.txt existence')
    else:
        print('[-]not existence windows server 2012.txt')
        exit()

    lists = open('windows server 2012.txt', 'r').read()
    fg = open('{}'.format(file4), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)

def windowsserver2003(file5):
    pd = os.path.exists(file5)
    if pd == True:
        print('[*]{}existence'.format(file5))
    else:
        print('[-]Sorry{}not existence'.format(file5))
        exit()

    pd2 = os.path.exists('windows server 2003.txt')
    if pd2 == True:
        print('[*]windows server 2003.txt existence')
    else:
        print('[-]not existence windows server 2003.txt')
        exit()

    lists = open('windows server 2003.txt', 'r').read()
    fg = open('{}'.format(file5), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)

def windowsxp(file6):
    pd = os.path.exists(file6)
    if pd == True:
        print('[*]{}existence'.format(file6))
    else:
        print('[-]Sorry{}not existence'.format(file6))
        exit()

    pd2 = os.path.exists('windows XP.txt')
    if pd2 == True:
        print('[*]windows XP.txt existence')
    else:
        print('[-]not existence windows XP.txt')
        exit()

    lists = open('windows XP.txt', 'r').read()
    fg = open('{}'.format(file6), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)

def windows10(file7):
    pd = os.path.exists(file7)
    if pd == True:
        print('[*]{}existence'.format(file7))
    else:
        print('[-]Sorry{}not existence'.format(file7))
        exit()

    pd2 = os.path.exists('windows 10.txt')
    if pd2 == True:
        print('[*]windows 10.txt existence')
    else:
        print('[-]not existence windows 10.txt')
        exit()

    lists = open('windows 10.txt', 'r').read()
    fg = open('{}'.format(file7), 'r').read()
    pow = "{}".format(fg)
    lgw = re.findall('KB\d+', lists)
    print('[*]There are no patched patches')
    for v in lgw:
        if v in str(pow):
            pass
        else:
            print("[*]", v)
if __name__ == '__main__':
    main()