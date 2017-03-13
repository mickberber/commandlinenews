#!/usr/bin/python
import sys
import urllib
import re
from datetime import datetime

import utils

def openpage(storylinks, index):
    url = storylinks[index - 1][0]
    utils.go_to_page(url)

def cl_news_util(arguments):
    if len(arguments) > 1:
        uf = urllib.urlopen('http://news.ycombinator.com')
        htmlfile = uf.read()
        storylinks = re.findall(r'href="(.+)" class="storylink">(.+)</a><span', htmlfile)

        if arguments[1] == '--headlines' or arguments[1] == '-h':
            utils.hn_headlines(storylinks)
            return

        if arguments[1] == '--open' or arguments[1] == '-o':
            if len(arguments) > 2:
                index = int(arguments[2])
                openpage(storylinks, index)
                return

        if arguments[1] == '--copy' or arguments[1] == '-cp':
            if len(arguments) > 2:
                utils.copy_file(arguments[2], htmlfile)
                return

    utils.handle_error('hn_error')

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        uf = urllib.urlopen('http://news.ycombinator.com')
        htmlfile = uf.read()
        storylinks = re.findall(r'href="(.+)" class="storylink">(.+)</a><span', htmlfile)

        if arguments[1] == '--headlines' or arguments[1] == '-h':
            utils.hn_headlines(storylinks)
            return

        if arguments[1] == '--open' or arguments[1] == '-o':
            if len(arguments) > 2:
                index = int(arguments[2])
                openpage(storylinks, index)
                return

        if arguments[1] == '--copy' or arguments[1] == '-cp':
            if len(arguments) > 2:
                utils.copy_file(arguments[2], htmlfile)
                return

    utils.handle_error('hn_error')


if __name__ == '__main__':
    main()
