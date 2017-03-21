#!/usr/bin/python
import sys
import os

import utils

from HTMLParser import HTMLParser

class WPHTMLParser(HTMLParser):
    printsection = False
    grabdata = False
    articledata = None
    articlelist = []
    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            try:
                if attrs[0][1] == 'main-content':
                    WPHTMLParser.printsection = True
            except:
                return

        if WPHTMLParser.printsection and tag == 'a':
            try:
                WPHTMLParser.articledata = {
                    'url': attrs[1][1],
                    'title': '',
                    'index': len(WPHTMLParser.articlelist)
                }
                WPHTMLParser.grabdata = True
            except:
                return
        return

    def handle_data(self, data):
        if WPHTMLParser.printsection and WPHTMLParser.grabdata:
            WPHTMLParser.articledata['title'] += data
        return

    def handle_endtag(self, tag):
        if tag == 'a' and WPHTMLParser.grabdata:
            WPHTMLParser.articlelist.append(WPHTMLParser.articledata)
            WPHTMLParser.articledata = None
            WPHTMLParser.grabdata = False
        if tag == 'section':
            WPHTMLParser.printsection = False
        return

class WPARTICLEParser(HTMLParser):
    printdata = False
    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            WPARTICLEParser.printdata = True
        return

    def handle_data(self, data):
        if WPARTICLEParser.printdata and data != ' ':
            print data

    def handle_endtag(self, tag):
        if tag == 'article':
            WPARTICLEParser.printdata = False

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('https://www.washingtonpost.com')
        htmlfile = htmlfile.decode('utf-8')
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
                article = articlelist[index]
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = int(args[2]) - 1
                article = articlelist[index]
                htmlfile = utils.get_html_file(article['url'])
                htmlfile = htmlfile.decode('utf-8')
                print '\n' + article['title']
                print '==================\n'
                parser = WPARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('wp_error')

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/wp_article.html', 'rU')
    f = f.read()
    parser = WPARTICLEParser()
    parser.feed(f.decode('utf-8'))
    return

if __name__ == '__main__':
    main()
