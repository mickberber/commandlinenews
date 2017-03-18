#!/usr/bin/python
import sys
import os
import urllib2

import utils

from HTMLParser import HTMLParser

class NYTIMESHTMLParser(HTMLParser):
    collectdata = False
    articledata = None
    articlelist = []
    def handle_starttag(self, tag, attrs):
        if len(NYTIMESHTMLParser.articlelist) == 24:
            return
        if tag == 'article':
            NYTIMESHTMLParser.collectdata = True
            return
        if NYTIMESHTMLParser.collectdata:
            try:
                if attrs[0][0] == 'href' and attrs[0][1][-17:] != 'commentsContainer':
                    NYTIMESHTMLParser.articledata = {
                      'title': '',
                      'url': attrs[0][1],
                      'index': NYTIMESHTMLParser.articlelist
                    }
            except:
                return
        return

    def handle_data(self, data):
        if len(NYTIMESHTMLParser.articlelist) == 24:
            return
        if NYTIMESHTMLParser.collectdata and NYTIMESHTMLParser.articledata and data != 'Comments':
            data = data.strip()
            data = data.split(' ')
            if data[0] != '':
                data = ' '.join(data)
                NYTIMESHTMLParser.articledata['title'] += ' ' + data
        return

    def handle_endtag(self, tag):
        if len(NYTIMESHTMLParser.articlelist) == 24:
            return
        if tag == 'article':
            if NYTIMESHTMLParser.articledata:
                NYTIMESHTMLParser.articlelist.append(NYTIMESHTMLParser.articledata)
                NYTIMESHTMLParser.articledata = None
                NYTIMESHTMLParser.collectdata = False
        return

class NYTIMESARTICLEParser(HTMLParser):
    printdata = False
    nomoreprint = False
    def handle_starttag(self, tag, attrs):
        if NYTIMESARTICLEParser.nomoreprint:
            return
        try:
            if tag == 'p':
                NYTIMESARTICLEParser.printdata = True
        except:
            return

    def handle_data(self, data):
        if NYTIMESARTICLEParser.printdata:
            if data == 'Order Reprints':
                NYTIMESARTICLEParser.nomoreprint = True
                return
            if data != 'Advertisement':
                print data

    def handle_endtag(self, tag):
        if tag == 'p':
            NYTIMESARTICLEParser.printdata = False
        return

def get_nyt_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('https://www.nytimes.com')
        parser = NYTIMESHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.nyt_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_nyt_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = int(args[2]) - 1
                url = articlelist[index]['url']
                htmlfile = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(url)
                htmlfile = htmlfile.read()
                parser = NYTIMESARTICLEParser()
                print '=========nyt=========\n'
                print articlelist[index]['title'] + '\n'
                print '=====================\n'
                parser.feed(htmlfile)
                return articlelist

    utils.handle_error('nyt_error')

def main():
    # currentdir = os.path.abspath('.')
    # f = open(currentdir + '/test/nyt.html', 'rU')
    # parser = NYTIMESHTMLParser()
    # parser.feed(f.read())
    # print parser.articlelist


    # FOR ARTICLES
    url = 'https://www.nytimes.com/2017/03/15/us/politics/trump-travel-ban.html'
    # htmlfile = get_html_file('https://www.nytimes.com/2017/03/15/us/politics/trump-travel-ban.html')
    htmlfile = urllib2.build_opener(urllib2.HTTPCookieProcessor).open(url)
    htmlfile = htmlfile.read()
    parser = NYTIMESARTICLEParser()
    parser.feed(htmlfile)
    return

if __name__ == '__main__':
    main()
