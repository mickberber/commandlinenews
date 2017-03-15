#!/usr/bin/python
import os
from HTMLParser import HTMLParser

import utils

class GUARDIANARTICLEParser(HTMLParser):
    collectdata = False
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            GUARDIANARTICLEParser.collectdata = True

    def handle_data(self, data):
        if GUARDIANARTICLEParser.collectdata:
            if data != '\n':
                print data
            GUARDIANARTICLEParser.collectdata = False


class GUARDIANHTMLParser(HTMLParser):
    articlelist = {}
    collectdata = False
    articledata = None
    def handle_starttag(self, tag, attrs):
        try:
            if tag == 'a' and attrs[2][1] == 'article':
                if attrs[1][0] == 'class' and attrs[1][1] == 'fc-item__link':
                    GUARDIANHTMLParser.articledata = attrs
                    GUARDIANHTMLParser.collectdata = True
        except:
            return

    def handle_data(self, data):
        if GUARDIANHTMLParser.collectdata and data != ' ' and data != '\n' and GUARDIANHTMLParser.articledata:
            title = data
            index = len(GUARDIANHTMLParser.articlelist)
            url = GUARDIANHTMLParser.articledata[0][1]
            if url not in GUARDIANHTMLParser.articlelist:
                GUARDIANHTMLParser.articlelist[url] = {
                  'title': title,
                  'index': index,
                  'url': url
                }
                GUARDIANHTMLParser.articledata = None

        return

    def handle_endtag(self, tag):
        if GUARDIANHTMLParser.collectdata and tag == 'a':
            GUARDIANHTMLParser.collectdata = False
        return

def get_gu_article(articlelist, index):
    for article in articlelist:
        if articlelist[article]['index'] == int(index) - 1:
            return articlelist[article]

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('http://www.theguardian.com/us')
        parser = GUARDIANHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.gu_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_ap_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                article = get_gu_article(articlelist, index)
                htmlfile = utils.get_html_file(article['url'])
                abbrevurl = article['url'][28:]
                print '\n' + article['title'] + ' -- ' + abbrevurl
                print '==================\n'
                parser = GUARDIANARTICLEParser()
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('ap_error')

def main():
    # cl_news_util(['gu', '-h'], False)
    htmlfile = utils.get_html_file('https://www.theguardian.com/us-news/2017/mar/14/mosque-obama-visited-trump-travel-ban-muslim')
    parser = GUARDIANARTICLEParser()
    parser.feed(htmlfile)
    print parser.collectdata


if __name__ == '__main__':
    main()
