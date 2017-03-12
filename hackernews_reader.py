#!/usr/bin/python
import sys
import os
import urllib
import re
from datetime import datetime
import webbrowser

def headlines(storylinks):
    print '==== HackerNews Headlines for ===='
    print '=== ' + str(datetime.now()) + ' ==='
    i = 0
    while i < len(storylinks):
        print str(i + 1) + '. ' + storylinks[i][1]
        i += 1

def openpage(storylinks, index):
    url = storylinks[index - 1][0]
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def handle_error():
    print 'Usage: [--headlines -h] [--open -o][headline number] [--copy -cp][filename]'
    sys.exit(1)

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        currentdir = os.path.abspath('.')
        uf = urllib.urlopen('http://news.ycombinator.com')
        htmlfile = uf.read()
        storylinks = re.findall(r'href="(.+)" class="storylink">(.+)</a><span', htmlfile)

        if arguments[1] == '--headlines' or arguments[1] == '-h':
            headlines(storylinks)
            return

        if arguments[1] == '--open' or arguments[1] == '-o':
            if len(arguments) > 2:
                openpage(storylinks, int(arguments[2]))
                return

        if arguments[1] == '--copy' or arguments[1] == '-cp':
            if len(arguments) > 2:
                writefile = open(currentdir + '/' + arguments[2], 'w+')
                writefile.write(htmlfile)
                return
                
    handle_error()


if __name__ == '__main__':
    main()
