#!/usr/bin/python

import sys
import os
import urllib
import re
import webbrowser

def main(cnn_url):
    currentdir = os.path.abspath('.')
    uf = urllib.urlopen(cnn_url)
    htmlfile = uf.read()
    highlights = re.findall(r'storyhighlights__list">(.+?)</ul>', htmlfile)
    if len(highlights):
        highlights = re.findall(r'normal">(.+?)</li>', highlights[0])
        print '=== Story Hightlights ==='
        for hl in highlights:
            print hl
        print '========================='
        content = re.findall(r'body__paragraph">(.+?)</', htmlfile)
        print content[0][-5:]
        del content[0]
        for p in content:
            print p
    else:
        description = re.findall(r'media__video-description--inline">(.+?)</div>', htmlfile)
        print description[0]
        print '========================='
        print 'This is a video article, would you like to open the page?(y/n)'
        user_input = raw_input()
        if user_input == 'y':
            print 'Opening: ' + cnn_url + ' in Chrome...'
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(cnn_url)
    return
