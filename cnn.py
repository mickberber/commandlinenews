#!/usr/bin/python
import sys
import re
import json
from datetime import datetime

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

def cl_news_util(arguments):
    if len(arguments) > 1:
        article_list = get_article_list()

        if arguments[1] == '--headlines' or arguments[1] =='-h':
            utils.cnn_headlines(article_list)
            return

        if len(arguments) > 2:
            index = int(arguments[2]) - 1
            cnn_url = 'http://www.cnn.com/' + article_list[index]['uri']

            if arguments[1] == '--open' or arguments[1] == '-o':
                utils.go_to_page(cnn_url)
                return

            if arguments[1] == '--read' or arguments[1] == '-r':
                print article_list[index]['headline']
                cnn_article_abbreviator.main(cnn_url)
                return

    utils.handle_error('cnn_error')

def main():
    arguments = sys.argv
    if len(arguments) > 1:
        article_list = get_article_list()

        if arguments[1] == '--headlines' or arguments[1] =='-h':
            utils.cnn_headlines(article_list)
            return

        if len(arguments) > 2:
            index = int(arguments[2])
            cnn_url = 'http://www.cnn.com/' + article_list[index]['uri']

            if arguments[1] == '--open' or arguments[1] == '-o':
                utils.go_to_page(cnn_url)
                return

            if arguments[1] == '--read' or arguments[1] == '-r':
                print article_list[index]['headline']
                cnn_article_abbreviator.main(cnn_url)
                return

    utils.handle_error('cnn_error')

if __name__ == '__main__':
    main()
