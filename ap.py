#!/usr/bin/python
import sys
import os
import re
from HTMLParser import HTMLParser

import utils

class APHTMLParser(HTMLParser):
    articlelist = {}
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and len(attrs) == 2:
            if len(attrs[0]) == 2 and len(attrs[1]) == 2:
                if attrs[0][0] == 'href' and attrs[1][0] == 'title':
                    key = re.findall(r'/article/(\w+)/', attrs[0][1])
                    title = attrs[1][1]
                    url = 'http://bigstory.ap.org' + attrs[0][1]
                    if len(key) == 1:
                        if key[0] not in APHTMLParser.articlelist:
                            APHTMLParser.articlelist[key[0]] = {
                                'index': len(APHTMLParser.articlelist),
                                'title': title,
                                'url': url
                            }

def get_ap_url(articlelist, index):
    for article in articlelist:
        i = 0
        while i < len(articlelist):
            if articlelist[article]['index'] == i:
                return articlelist[article]['url']
            i += 1

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('http://bigstory.ap.org/')
        parser = APHTMLParser()
        parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.ap_headlines(articlelist)
            return articlelist

        if len(args) > 2:

            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                url = get_ap_url(articlelist, index)
                utils.go_to_page(url)
                return articlelist


            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                url = get_ap_url(articlelist, index)
                htmlfile = utils.get_html_file(url)
                content = re.search(r'<meta name="description" content="(.+?)" />', htmlfile)
                print content.group(1)
                return articlelist


    utils.handle_error('ap_error')


def main():
    a = 'http://bigstory.ap.org/article/f7645d59944d47228f2eb195a35a19a4/'
    htmlfile = utils.get_html_file(a + 'get-without-planned-parenthood-one-texas-effort-stumbles')
    content = re.search(r'<meta name="description" content="(.+?)" />', htmlfile)
    print content.group(1)

if __name__ == '__main__':
    main()
