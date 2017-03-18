# Adding a News Service
If there's a news service you'd like to add to your version of CLN, adding a service can be pretty easy.
In order to show headlines, and print articles we need to parse the homepage and an example article from the service you want to use.
Below is an example guide on how to parse these pages and include them in the rest of the app.

## Getting started:
- Copy `service_stub.py` or copy the following code:
```
#!/usr/bin/python
import sys
import os
import re

import utils

from HTMLParser import HTMLParser

# Rename Me!!!
class SERVICEHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      return

    def handle_data(self, data):
        return

# Rename Me!!!
class SERVICEARTICLEParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        return

    def handle_data(self, data):
        return

# Rename Me!!!
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
            # RENAME ME AND CREATE ME IN utils.py
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

```
- for testing and running the `main` function, make your file executable from the terminal:
 - `chmod +x ./<filename>.py`
---
# Homepages
- When parsing the homepage of your desired service, you will want to parse the html for article links and headlines. Generally these are found in 'a' or article tags. Finding these is easy with handle_starttag and handle_data. Refer to other service files for examples, and when creating your list of articles, you may use a list or a dict, but to make it easy when integrating with the rest of the app, return found data from the article parser in this format:
```
{
  'title': title,
  'index': index,
  'url': url
}
```
- Make sure to create a headline print utility in `utils.py`
---
# Articles
- When parsing articles of your service, use SERVICEARTICLEParser.
  - Currently we are not storing article in cache, so you can just print text as you find it.
  - Article text is often found in p tags.
  - Most services use the same format for every article, btu some don't. Try a few different articles to try to handle different instances.
  - [For reference see: ./services/cnn_article_parser.py](./services/cnn_article_parser.py)
---
# Integrating into ./clnews.py
- `./clnews.py` is made up of 3 functions, we will add 2 lines to each and that's it!
 - add: `import <service file name>`
 - pick_article (the '-r' is the most important part of this!)
 ```
 elif service == '<service abbrev>':
     <service abbrev>.cl_news_util(['<service abbrev>', '-r', command], cache['<service abbrev>'])
 ```
 - read_more:
 ```
 elif service == '<service abbrev>':
         <service abbrev>.cl_news_util(['<service abbrev>', '-h'], cache['<service abbrev>'])
 ```
 - main (main MUST return into the cache, in order to speed up the next lookup):
 ```
 elif service == '<service abbrev>':
     cache['<service abbrev>'] = <service abbrev>.cl_news_util([service, '-h'], cache['<service abbrev>'])
 ```
