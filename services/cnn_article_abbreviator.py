#!/usr/bin/python
import sys
import urllib
import re

import utils

def main(cnn_url):
    uf = urllib.urlopen(cnn_url)
    htmlfile = uf.read()
    highlights = re.findall(r'storyhighlights__list">(.+?)</ul>', htmlfile)
    description = re.findall(r'media__video-description--inline">(.+?)</div>', htmlfile)
    paras = re.findall(r'class="zn-body__paragraph">(.+?)</', htmlfile)
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
    elif len(description):
        print description[0]
        print '========================='
        print 'This is a video article, would you like to open the page?(y/n)'
        user_input = raw_input()
        if user_input == 'y':
            utils.go_to_page(cnn_url)
    elif len(paras):
        print '========================='
        for p in paras:
            print p
    return
