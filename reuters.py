#!/usr/bin/python
import sys
import os

import utils

from HTMLParser import HTMLParser

class REUTERSHTMLParser(HTMLParser):
    return

class REUTERSARTICLEParser(HTMLParser):

def get_reuters_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('http://www.reuters.com/')
        parser = REUTERSHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.reuters_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_reuters_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                article = get_reuters_article(articlelist, index)
                htmlfile = utils.get_html_file(article['url'])
                abbrevurl = article['url'][28:]
                print '\n' + article['title'] + ' -- ' + abbrevurl
                print '==================\n'
                parser = REUTERSARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('reuters_error')

def main():

    return

if __name__ == '__main__':
    main()
