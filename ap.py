#!/usr/bin/python
import sys
import os
from HTMLParser import HTMLParser

import utils

class APHTMLParser(HTMLParser):
    boolean = False
    articlelist = []
    def handle_starttag(self, tag, attrs):
        if len(attrs) and len(attrs[0]) > 1:
            if attrs[0][0] == 'class' and attrs[0][1] == 'article-layout':
                APHTMLParser.boolean = True

        if tag == 'a' and len(attrs):
            if attrs[0][0] == 'href' and APHTMLParser.boolean == True:
                print attrs[0][1]

    def handle_endtag(self, tag):
        if APHTMLParser.boolean and tag == 'div':
          APHTMLParser.boolean = False

    def handle_data(self, data):
        if APHTMLParser.boolean:
            data = data.replace('\n', '')
            data = data.replace('\t', '')
            data = data.split(' ')
            strstore = []
            for index in data:
                if index != '':
                    strstore.append(index)
            if len(strstore):
                APHTMLParser.articlelist.append(' '.join(strstore))

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/ap.html', 'rU')
    parser = APHTMLParser()
    parser.feed(f.read())
    print parser.articlelist

if __name__ == '__main__':
    main()
