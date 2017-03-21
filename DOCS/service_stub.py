#!/usr/bin/python
import sys
import os
import re

import utils

from HTMLParser import HTMLParser

class SERVICEHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      return

    def handle_data(self, data):
        return

class SERVICEARTICLEParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        return

    def handle_data(self, data):
        return


def get_service_article(articlelist, index):
    return

def cl_news_util(args, cache):
    if not cache:
        # Used to parse homepage
        # parser = SERVICEHTMLParser()
        # parser.feed(htmlfile)
        articlelist = parser.articlelist
    else:
        articlelist = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.service_headlines(articlelist)
            return articlelist

        if len(args) > 2:
            # SERVICEARTICLEParser will be called for these options
            # Dont worry about this, when you get reading working, opening works the same way
            # if you use a service like hacker news with multiple sources, use open instead of read
            if args[1] == '--open' or args[1] == '-o':
                index = args[2]
                article = get_service_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                # Used to parse articles
                index = args[2]

                return articlelist

def main():
    # You can use main to test with before integrating into clnews.py
    return

if __name__ == '__main__':
    main()
