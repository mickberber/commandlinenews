# This file will be updated with known bugs:

## How to Report Bugs:
- Bug Number: (create an bug number [bug number = Total Bugs Found + 1])
- Version
- Description
 - Suspected cause(if any info known)
```
Terminal Output Here
```
## Making a pull request:
- Move fixed bug to Archive
- Adjust `Total Bugs Found`
- Adjust `Total Bugs Fixed`
- Adjust `Current Bugs`
- Explanations of:
  - files altered and why
  - code changes/additions/subtractions

## Total Bugs Found: 3
## Total Bugs Fixed: 1
## Current Bugs: 2

# Known Bugs:
- Bug Number: 2
- "1.0.0-beta.6"
- Aljazeea reads only one article, and then only prints headlines.
 - Maybe something with the ARTICLEParser class?
 - example output
```
To read an article enter the headline number.
To go back to the main menu, type "main"
To quit type quit.

1

Tillerson in China to discuss N Korea nuclear programme
=====================

To read more from aljaz type: "y".
Type "main" to return to the Main Menu.
To quit type "quit".
```

- Bug Number: 1
- "1.0.0-beta.6"
- cnn_article_parser breaks on certain articles.
```
To read an article enter the headline number.
To go back to the main menu, type "main"
To quit type quit.

12

Guess where Barack Obama is
Traceback (most recent call last):
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 118, in <module>
    main()
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 115, in main
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 52, in read_more
    main()
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 115, in main
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 52, in read_more
    main()
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 115, in main
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 44, in pick_article
    read_more(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 77, in read_more
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 31, in pick_article
    cnn.cl_news_util(['cnn', '-r', command], cache['cnn'])
  File "/Users/michaelberber/sideProjects/commandlinenews/services/cnn.py", line 41, in cl_news_util
    cnn_article_abbreviator.main(cnn_url)
  File "/Users/michaelberber/sideProjects/commandlinenews/services/cnn_article_abbreviator.py", line 25, in main
    print description[0]
IndexError: list index out of range
```


# Archive


- Bug Number: 0
- "1.0.0-beta.6"
- Guardian article praser breaks on some articles.
 - example output
```
Traceback (most recent call last):
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 118, in <module>
    main()
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 115, in main
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 38, in pick_article
    guardian.cl_news_util(['gu', '-r', command], cache['gu'])
  File "/Users/michaelberber/sideProjects/commandlinenews/services/guardian.py", line 88, in cl_news_util
    parser.feed(htmlfile)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py", line 117, in feed
    self.goahead(0)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py", line 161, in goahead
    k = self.parse_starttag(i)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py", line 308, in parse_starttag
    attrvalue = self.unescape(attrvalue)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py", line 475, in unescape
    return re.sub(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));", replaceEntities, s)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 155, in sub
    return _compile(pattern, flags).sub(repl, string, count)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 44: ordinal not in range(128)
```
