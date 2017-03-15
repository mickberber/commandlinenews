#!/usr/bin/python
import os
from HTMLParser import HTMLParser

import utils

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

def cl_news_util(args, cache):
    if not cache:
        htmlfile = utils.get_html_file('http://www.theguardian.com/us')
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
                article = get_ap_article(articlelist, index)
                utils.go_to_page(article['url'])
                return articlelist

            if args[1] == '--read' or args[1] == '-r':
                index = args[2]
                article = get_ap_article(articlelist, index)
                htmlfile = utils.get_html_file(article['url'])
                content = re.search(r'<meta name="description" content="(.+?)" />', htmlfile)
                print_article_header(article['title'], content.group(1))
                return articlelist


    utils.handle_error('ap_error')

def main():
    currentdir = os.path.abspath('.')
    f = open(currentdir + '/test/guardian.html', 'rU')
    htmlfile = f.read()
    parser = GUARDIANHTMLParser()
    parser.feed(htmlfile)
    for article in parser.articlelist:
        article = parser.articlelist[article]
        print article.values()


if __name__ == '__main__':
    main()
