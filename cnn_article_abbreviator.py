#!/usr/bin/python

import sys
import os
import urllib
import re

def main(cnn_url):
    currentdir = os.path.abspath('.')
    uf = urllib.urlopen(cnn_url)
    htmlfile = uf.read()
    highlights = re.findall(r'storyhighlights__list">(.+?)</ul>', htmlfile)
    highlights = re.findall(r'normal">(.+?)</li>', highlights[0])
    content = re.findall(r'body__paragraph">(.+?)</', htmlfile)
    print '=== Story Hightlights ==='
    for hl in highlights:
        print hl
    print '========================='
    print content[0][-5:]
    del content[0]
    for p in content:
        print p
    return
