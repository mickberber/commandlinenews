#!/usr/bin/python
import sys
import webbrowser
import datetime

def handle_error(error_string):
    if error_string == 'cnn_error':
        print 'Usage: [--headlines -h] [--read -r][headline number] [--copy -cp][filename]'
    if error_string == 'hn_error':
        print 'Usage: [--headlines -h] [--open -o][headline number] [--copy -cp][filename]'
    sys.exit(1)

def go_to_page(url):
    print 'Opening: ' + url + ' in Chrome...'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
