#!/usr/bin/python
import sys
import os

import utils

from HTMLParser import HTMLParser

class AJHTMLParser(HTMLParser):
    return

class AJARTICLEParser(HTMLParser):

def get_aj_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('https://www.nytimes.com')
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
                abbrevurl = article['url'][28:]
                print '\n' + article['title'] + ' -- ' + abbrevurl
                print '==================\n'
                parser = AJARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('aj_error')

def main():
    return

if __name__ == '__main__':
    main()
