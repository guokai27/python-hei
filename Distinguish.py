import requests
import re
import socket
from bs4 import BeautifulSoup
import optparse

def main():
	parser=optparse.OptionParser()
	parser.add_option('-p',dest='host',help='ip port scanner')
	parser.add_option('-w',dest='whois',help='Whois query')
	parser.add_option('-d',dest='dns',help='dns query')
	parser.add_option('-z',dest='domain',help='Domain name query')
	parser.add_option('-f',dest='fw',help='Bypass query')
	(options,args)=parser.parse_args()
	if options.host:
		ip=options.host
		portscanner(ip)
	elif options.whois:
		ws=options.whois
		whois(ws)
	elif options.dns:
		dn=options.dns
		dnsquery(dn)
	elif options.domain:
		domain=options.domain
		domains(domain)
	elif options.fw:
		pz=options.fw
		bypass(pz)
	else:
		parser.print_help()
		exit()
def portscanner(ip):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	for port in range(1,65535):
		try:
			s.connect((ip,port))
			print('[+]',ip,':',port,'open')
		except:
			pass

def whois(ws):
	url = "http://whoissoft.com/{}".format(ws)
	rest = requests.get(url=url)
	csd = rest.content.decode('utf-8')
	fsd = BeautifulSoup(csd, 'html.parser')
	wsd = fsd.get_text()
	comp = re.compile(
		r'a:link, a:visited {.*? }|a:hover {.*?}|white-space: .*?;|font-family:.*?;|function\s+s|window.location.href\s+=\s+".*?"|return\s+false;| var _sedoq\s+=\s+_sedoq|_sedoq.partnerid\s+=\s+''316085'';| _sedoq.locale\s+=\s+''zh-cn'';|var\s+s\s+=\s+document.createElement|s.type\s+=\s+''text/javascript'';|s.async\s+=\s+true;|s.src\s+=\s+''.*?'';|var\s+f\s+=\s+document.getElementsByTagName|f.parentNode.insertBefore|/.*?/|pre\s+{|word-wrap:\s+break-word;|}|\s*\(str1\){|\s+\+\s+str1;|\s+\|\s+\|\|\s+{;|\s+\|\|\s+{;|_sedoq.partnerid|\s+=|''316085''|\s+'';|\s+enter\s+your\s+partner\s+id|_sedoq.locale\s+=\s+|zh-cn|language\s+locale|\(function\(\)\s+{|\[0\];|s.type|text/javascript|script|s,\s+f|document.getElementById\(.*?\)|.style.marginLeft|=window|\|\||\s+{|;|en-us,|en-uk,|de-de,|es-er-fr,|pt-br,|\s+.innerWidth2|es-|er-|fr|.innerWidth2|er|-,')
	tih = re.sub(comp, "", wsd)
	wrs = open('whois.txt', 'w')
	wrs.write(tih)
	wrs.close()
	wrr = open('whois.txt', 'r')
	rr = wrr.read()
	xin = rr.replace("''", '')
	xin2 = xin.replace("(", '')
	xin3 = xin2.replace(")", '')
	xin4 = xin3.replace("er-,", '')
	xin5 = xin4.replace('.innWidth2+"px"', '')
	xin6 = xin5.replace('window.onresize=function{', '')
	xin7 = xin6.replace('.innWidth2+"px"', '')
	print(xin7, end='')
def dnsquery(dn):
	url = "https://jiexifenxi.51240.com/web_system/51240_com_www/system/file/jiexifenxi/get/?ajaxtimestamp=1526175925753"
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'}
	params = {'q': '{}'.format(dn), 'type': 'a'}
	reqst = requests.post(url=url, headers=headers, params=params)
	content = reqst.content.decode('utf-8')
	bd = BeautifulSoup(content, 'html.parser')

	print('---[+]A record---')
	print(bd.get_text())

	print('---[+]MX record---')
	params2 = {'q': '{}'.format(dn), 'type': 'mx'}
	rest = requests.post(url=url, headers=headers, params=params2)
	content2 = BeautifulSoup(rest.content.decode('utf-8'), 'html.parser')
	print(content2.get_text())

	print('---[+]CNAME record---')
	params3 = {'q': '{}'.format(dn), 'type': 'cname'}
	rest2 = requests.post(url=url, headers=headers, params=params3)
	content3 = BeautifulSoup(rest2.content.decode('utf-8'), 'html.parser')
	print(content3.get_text())

	print('---[+]NS record---')
	params4 = {'q': '{}'.format(dn), 'type': 'ns'}
	rest3 = requests.post(url=url, headers=headers, params=params4)
	content4 = BeautifulSoup(rest3.content.decode('utf-8'), 'html.parser')
	print(content4.get_text())

	print('---[+]TXT record---')
	params5 = {'q': '{}'.format(dn), 'type': 'txt'}
	rest4 = requests.post(url=url, headers=headers, params=params5)
	content5 = BeautifulSoup(rest4.content.decode('utf-8'), 'html.parser')
	print(content5.get_text())

def domains(domain):
	print('---[+]Domain name query---')
	url = "http://i.links.cn/subdomain/"
	headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'}
	params = {'domain': '{}'.format(domain), 'b2': '1', 'b3': '1', 'b4': '1'}
	reqst = requests.post(url=url, headers=headers, params=params)
	vd = reqst.content.decode('gbk')
	rw = re.findall('<div class=domain><input type=hidden name=.*? id=.*? value=".*?">', vd)
	rw2 = "".join(str(rw))
	bwdw = BeautifulSoup(str(rw2), 'html.parser')
	pw = bwdw.find_all('input')
	for l in pw:
		isd = l.get("value")
		print(isd)

def bypass(pz):
	url = "http://www.webscan.cc/?action=query&ip={}".format(pz)
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'}
	wd = requests.get(url=url, headers=headers)
	rcy = wd.content.decode('utf-8')
	res = re.findall('"domain":".*?"', str(rcy))
	lis = "".join(res)
	rmm = lis.replace('"', '')
	rmm2 = rmm.replace(':', '')
	rmm3 = rmm2.replace('/', '')
	rmm4 = rmm3.replace('domain', '')
	rmm5 = rmm4.replace('http', '')
	print(rmm5)

if __name__ == '__main__':
    main()
