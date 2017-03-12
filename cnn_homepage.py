#!/usr/bin/python
import sys
import os
import urllib
import re
import json
from datetime import datetime

import utils
import cnn_article_abbreviator

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
    while i < 25:
        print str(i + 1) + '. ' + article_list[i]['headline']
        i += 1

def cat_article(cnn_url):
    cnn_article_abbreviator.main('http://www.cnn.com' + cnn_url)

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
                index = int(arguments[2])
                print article_list[index]['headline']
                cat_article(article_list[index]['uri'])
                return

    utils.handle_error('cnn_error')

if __name__ == '__main__':
    main()
