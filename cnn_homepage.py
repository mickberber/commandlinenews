#!/usr/bin/python

import sys
import os
import urllib
import re
import json
from datetime import datetime

def get_article_list():
    currentdir = os.path.abspath('.')
    uf = urllib.urlopen('http://cnn.com')
    htmlfile = uf.read()
    articles = re.findall(r'articleList":\[(.+?)\]', htmlfile)
    articles = re.findall(r'({.+?})', articles[0])
    article_list = []
    for article in articles:
        article_list.append(json.loads(article))
    return article_list

def headlines(article_list):
    print ' ====== Command Line News ======'
    print ' ======== CNN Headlines ========'
    print ' == ' + str(datetime.now()) + ' =='
    i = 0
    while i < 15:
        print str(i + 1) + '. ' + article_list[i]['headline']
        # print article_list[i]['uri']
        # print article_list[i]['description']
        i += 1

# def cat_article(index):

def handle_error():
    print 'Usage: [--headlines -h] [--read -r][headline number] [--copy -cp][filename]'
    sys.exit(1)

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        article_list = get_article_list()

        if arguments[1] == '--headlines' or arguments[1] =='-h':
            headlines(article_list)
            return
            
        if len(arguments) > 2:
            if arguments[1] == '--read' or arguments[1] == '-r':
                # cat_article(article_list[2])
                return

    handle_error()

if __name__ == '__main__':
    main()
