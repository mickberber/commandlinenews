#!/usr/bin/python
import sys
import os
import re

import utils

from HTMLParser import HTMLParser

class AJHTMLParser(HTMLParser):
    collectdata = False
    articlelist = {}
    articledata = None
    def handle_starttag(self, tag, attrs):
        try:
            if tag == 'a' and attrs[0][0] == 'onclick':
                AJHTMLParser.articledata = attrs
                AJHTMLParser.collectdata = True
            return
        except:
            return

    def handle_data(self, data):
        if AJHTMLParser.collectdata and data != '\n' and data != ' ':
            AJHTMLParser.collectdata = False
            title = data
            index = len(AJHTMLParser.articlelist)
            url = AJHTMLParser.articledata[1][1]
            if url not in AJHTMLParser.articlelist:
                AJHTMLParser.articlelist[url] = {
                  'title': title,
                  'index': index,
                  'url': url
                }
                AJHTMLParser.articledata = None
        return

class AJARTICLEParser(HTMLParser):
    def handle_starttag():
        return


def get_aj_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('http://www.aljazeera.com/')
        htmlfile = htmlfile.decode('utf-8')
        parser = AJHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.aj_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_aj_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                article = get_aj_article(articlelist, index)
                htmlfile = utils.get_html_file(article['url'])
                parser = AJARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('aj_error')

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/aljaz.html', 'rU')
    htmlfile = f.read()
    htmlfile = htmlfile.decode('utf-8')
    parser = AJHTMLParser()
    parser.feed(htmlfile)
    print parser.articlelist

if __name__ == '__main__':
    main()
