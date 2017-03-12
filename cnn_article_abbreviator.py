#!/usr/bin/python

import sys
import os
import urllib
import re

def main():
    arguments = sys.argv
    currentdir = os.path.abspath('.')
    uf = urllib.urlopen(arguments[1])
    htmlfile = uf.read()
    storylinks = re.findall(r'storyhighlights__list">(.+?)</ul>', htmlfile)
    # print storylinks
    print re.findall(r'normal">(.+?)</li>', storylinks[0])
    return

if __name__ == '__main__':
    main()
