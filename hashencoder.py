from __future__ import unicode_literals
import hashlib
import time
import os
import hmac
import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
import telethon

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
		
a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

from base64 import b16encode
from base64 import b32encode
from base64 import b64encode
from binascii import hexlify
os.system ('clear')

import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os

puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

__banner__ = b+"""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ┏━┓ ┏┓┏ ┳┈┈ ┳ ┏┓┏ ┏━┓          
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒       ┃┈┃ ┃┃┃ ┃┈┈ ┃ ┃┃┃ ┣┫┈           
▒▒█▒▒▒▄██████████▄▒▒▒▒       ┗━┛ ┛┗┛ ┻━┛ ┻ ┛┗┛ ┗━┛            
▒█▐▒▒▒████████████▒▒▒▒           
▒▌▐▒▒██▄▀██████▀▄██▒▒▒           
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒           
▐┼▐▒▒██████████████▒▒▒       ONLINE HASH ENCODE          
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒       created by @janob_darknet    
▒▒█████──────────▐███▌       telegram channel: @kalinethunteruz 
▒▒█▀▀██▄█─▄───▐─▄███▀▒           
▒▒█▒▒███████▄██████▒▒▒         
▒▒▒▒▒██████████████▒▒▒           
▒▒▒▒▒██████████████▒▒▒       ┳┈┳ ┏━┓ ┏━┓ ┳┈┳          
▒▒▒▒▒█████████▐▌██▌▒▒▒       ┣━┫ ┣━┫ ┗━┓ ┣━┫       
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒       ┻┈┻ ┻┈┻ ┗━┛ ┻┈┻        
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒            
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒             
"""
__muallif__ = a+"""\tkanalimiz: @KaliNethunterUz\n\tdasturchi: @janob_darknet"""

clearscreen()
print(__banner__)
print(__muallif__)
time.sleep(1)
def b16_encode(item):
    
    try:
        return (b16encode(item.encode('utf-8'))).decode()
    except:
        return ''
def sha256(item):
    
    try:
        return (hashlib.sha256(item.encode("utf-8")).hexdigest())
    except:
        return ''
def sha516(item):
    
    try:
        return (hashlib.sha512(item.encode("utf-8")).hexdigest())
    except:
        return ''
def b32_encode(item):
    
    try:
        return (b32encode(item.encode('utf-8'))).decode()
    except:
        return ''
def b64_encode(item):
    
    try:
        return (b64encode(item.encode('utf-8'))).decode()
    except:
        return ''
def rsa_encode(item):
    
    
    n_modulus_hex_string = 'd7190a042cd2db97ebc2ab4da366f2a7085556ed613b5a39c9fdd2bb2595d1dc'
    e_exponent_hex_string = '1091'

    if len(item) < 1:
        print("[!]exception item:[%s]" % item)
        return item
    public_modulus = int(n_modulus_hex_string, 16)
    public_exponent = int(e_exponent_hex_string, 16)
    item = int(hexlify(item[::-1].encode('utf-8')).decode(), 16)
    item = pow(item, public_exponent, public_modulus)
    return '%X' % item
def sha1_encode(item):
    
    try:
        return hashlib.sha1(item.encode("utf-8")).hexdigest()
    except:
        return ''
def md516_encode(item):
    
    try:
        return hashlib.md5(item.encode("utf-8")).hexdigest()[8:-8]
    except:
        return ''
def sha512_encode(item):
    
    try:
        return hashlib.sha512(item.encode("utf-8")).hexdigest()
    except:
        return ''
def hmac_encode(item):
    
    key = "random_key_in_html_js_or_other_place_if_it_is_not_changed"
    item = md5_encode(item)
    return hmac.new(key.encode("utf-8"), item.encode("utf-8"), hashlib.md5).hexdigest()
a=input(a+'\n\nHohlagam sózingizni yozing:')
print(a+'\n---------------------------------------\n sha1 shifrlandi •••>\n',sha1_encode(a),'\n---------------------------------------\n\n sha256 shifrlandi •••> ',sha256(a),'\n---------------------------------------\n\n sha516 shifrlandi •••> ',sha516(a),'\n---------------------------------------\n\n sha512 shifrlandi •••> ',sha512_encode(a))
print('\n---------------------------------------\n\n b32 shifrlandi •••> ',b32_encode(a),'\n---------------------------------------\n\n b64 shifrlandi •••> ',b64_encode(a),'\n---------------------------------------\n\n rsa shifrlandi •••> ',rsa_encode(a),'\n---------------------------------------\n\n sha1 shifrlandi •••> ',sha1_encode(a),'\n---------------------------------------\n\n md516 shifrlandi •••> ',md516_encode(a),'\n---------------------------------------')
