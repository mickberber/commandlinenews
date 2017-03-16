#!/usr/bin/python
import sys
import os

import utils

from HTMLParser import HTMLParser

class WPHTMLParser(HTMLParser):
    def handle_starttag():
        return

class WPARTICLEParser(HTMLParser):
    def handle_starttag():
        return
        
def get_wp_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('https://www.washingtonpost.com')
        parser = WPHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.wp_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_wp_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                article = get_wp_article(articlelist, index)
                htmlfile = utils.get_html_file(article['url'])
                abbrevurl = article['url'][28:]
                print '\n' + article['title'] + ' -- ' + abbrevurl
                print '==================\n'
                parser = WPARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('wp_error')

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/wp.html', 'rU')
    print f.read()
    return

if __name__ == '__main__':
    main()
