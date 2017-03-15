#!/usr/bin/python
import os
from HTMLParser import HTMLParser

import utils

class GUARDIANHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      if tag == 'a':
          try:
              if attrs[2][0] == 'data-link-name' and attrs[2][1] == 'article':
                  print tag, attrs
          except:
              print None



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


if __name__ == '__main__':
    main()
