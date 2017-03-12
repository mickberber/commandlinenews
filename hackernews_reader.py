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
    return

def openpage(storylinks, index):
    url = storylinks[index][0]
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)


def main():


    if len(sys.argv) > 1:
        argument = sys.argv[1]
        currentdir = os.path.abspath('.')
        uf = urllib.urlopen('http://news.ycombinator.com')
        htmlfile = uf.read()
        storylinks = re.findall(r'href="(.+)" class="storylink">(.+)</a><span', htmlfile)

        if argument == '--headlines' or argument == '-h':
            headlines(storylinks)

        if argument == '--open' or argument == '-o':
            openpage(storylinks, int(sys.argv[2]))

        else:
            writefile = open(currentdir + '/' + sys.argv[1], 'w+')
            writefile.write(htmlfile)
    else:
        print 'Usage: [--headlines -h] [-cp htmlfile]'
        sys.exit(1)
    return


if __name__ == '__main__':
    main()
