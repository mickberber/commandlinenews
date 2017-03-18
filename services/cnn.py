#!/usr/bin/python
import sys
import os
import re
import json

import utils
import cnn_article_abbreviator

def get_article_list():
    htmlfile = utils.get_html_file('http://cnn.com')
    articles = re.findall(r'articleList":\[(.+?)\]', htmlfile)
    articles = re.findall(r'({.+?})', articles[0])
    article_list = []
    for article in articles:
        article_list.append(json.loads(article))
    return article_list

def cl_news_util(args, cache):
    if not cache:
        article_list = get_article_list()
    else:
        article_list = cache

    if len(args) > 1:
        if args[1] == '--headlines' or args[1] =='-h':
            utils.cnn_headlines(article_list)
            return article_list

        if len(args) > 2:
            index = int(args[2]) - 1
            cnn_url = 'http://www.cnn.com/' + article_list[index]['uri']

            if args[1] == '--open' or args[1] == '-o':
                utils.go_to_page(cnn_url)
                return article_list

            if args[1] == '--read' or args[1] == '-r':
                os.system('clear')
                print article_list[index]['headline']
                cnn_article_abbreviator.main(cnn_url)
                return article_list

    utils.handle_error('cnn_error')

def main():
    args = sys.argv
    if len(args) > 1:
        article_list = get_article_list()

        if args[1] == '--headlines' or args[1] =='-h':
            utils.cnn_headlines(article_list)
            return

        if len(args) > 2:
            index = int(args[2])
            cnn_url = 'http://www.cnn.com/' + article_list[index]['uri']

            if args[1] == '--open' or args[1] == '-o':
                utils.go_to_page(cnn_url)
                return

            if args[1] == '--read' or args[1] == '-r':
                print article_list[index]['headline']
                cnn_article_abbreviator.main(cnn_url)
                return

    utils.handle_error('cnn_error')

if __name__ == '__main__':
    main()
