#!/usr/bin/python
import sys
import os
import webbrowser
from datetime import datetime

def handle_error(error_string):
    if error_string == 'cnn_error':
        print 'Usage: [--headlines -h] [--read -r][headline number] [--open -o][headline number]'
    if error_string == 'hn_error':
        print 'Usage: [--headlines -h] [--open -o][headline number] [--copy -cp][dest filename]'
    sys.exit(1)

def go_to_page(url):
    print 'Opening: ' + url + ' in Chrome...'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def copy_file(dest, htmlfile):
    currentdir = os.path.abspath('.')
    print 'Writing article to: ' + currentdir + '/' + dest
    writefile = open(currentdir + '/' + dest, 'w+')
    writefile.write(htmlfile)

def cnn_headlines(article_list):
    print '======= Command Line News ======='
    print '========= CNN Headlines ========='
    print '== ' + str(datetime.now()) + ' =='
    print '================================='
    i = 0
    while i < 25:
        print str(i + 1) + '. ' + article_list[i]['headline']
        i += 1

def hn_headlines(storylinks):
    print '======== Command Line News ========='
    print '===== HackerNews Headlines for ====='
    print '==== ' + str(datetime.now()) + ' ====\n'
    print '===================================='
    print '=HackerNews atricles open in Chrome='
    print '====================================\n'
    i = 0
    while i < len(storylinks):
        print str(i + 1) + '. ' + storylinks[i][1]
        i += 1
