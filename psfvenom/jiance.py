daoru=__import__('colour',fromlist=True)
red=getattr(daoru,'red')

import re

ipzz='(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)'

def numbers(user_payload):
    if user_payload == 'x86':
        return 'x86'
    elif user_payload == 'x64':
        return 'x64'
    elif user_payload == 'x86_64':
        return 'x86_64'
    else:
        print(red('[-]'), 'No such digits')
        return ''


def ips(user_ip):
    zz = re.findall(ipzz, user_ip)
    if zz:
        for y in zz:
            qc = str(y).replace("'", '').replace(',', '.').replace('(', '').replace(')', '').strip().rstrip().lstrip()
            qc = "".join(qc.split(' '))
            return qc
    else:
        print(red('[-]'), 'IP format error')
        return ''

def ports(user_port):
    if int(user_port) <= 65535:
        return user_port
    else:
        print(red('[-]'), 'Incorrect port range')
        return ''


def type_ofs(user_typeof):
    if user_typeof == 'dll':
        return 'dll'
    elif user_typeof == 'exe':
        return 'exe'
    elif user_typeof == 'txt':
        return 'txt'
    elif user_typeof == 'c':
        return 'c'
    elif user_typeof == 'py':
        return 'py'
    elif user_typeof=='elf':
        return 'elf'
    elif user_typeof=='macho':
        return 'macho'
    else:
        print(red('[-]'),'Not Type')
        return ''

def names(user_name):
    if user_name == '':
        return 'haq520'
    elif user_name != '':
        return user_name