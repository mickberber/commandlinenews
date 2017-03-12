#!/usr/bin/python
import sys
import os
import urllib
import re

def main():
    currentdir = os.path.abspath('.')
    uf = urllib.urlopen('http://news.ycombinator.com')
    htmlfile = uf.read()
    if len(sys.argv) == 2:
        writefile = open(currentdir + '/' + sys.argv[1], 'w+')
        writefile.write(htmlfile)
    else:
        print 'Usage: htmlfile'
        sys.exit(1)
    return


if __name__ == '__main__':
    main()
