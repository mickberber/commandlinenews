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

## Total Bugs Found: 5
## Total Bugs Fixed: 3
## Current Bugs: 2

# Known Bugs:
- Bug Number: 7
- "1.0.0-beta.6"
- Wp articles include what look like multi-line lists
```
The government is demanding to know who this Trump critic is. Twitter is suing to keep it a secret.
==================

(Eric Thayer/Reuters)
Twitter filed a lawsuit Thursday against the U.S. Department of Homeland Security, asking the court to prevent the department from taking steps to unmask the user behind an account critical of the Trump administration.
The tech company said that allowing DHS access to that information would produce a “grave chilling effect on the speech of that account,” as well as other accounts critical of the U.S. government. The case sets up a potential showdown over free speech between Silicon Valley and Washington.
According to
Twitter's court filings
, Homeland Security is “unlawfully abusing a limited-purpose investigatory tool” to find out who is behind the @ALT_USCIS account. Its Twitter feed has publicly criticized the administration's immigration policies, particularly the actions of the U.S. Citizenship and Immigration Services (USCIS) division of Homeland Security.
 [
One thing Trump has stopped doing on Twitter since inauguration
]
```
- Bug Number: 6
- "1.0.0-beta.6"
- Ap articles include "&#039;" instead of " ' "
```

BEIRUT (AP) — Chemical weapons have killed hundreds of people since the start of Syria&#039;s civil war, with the U.N. blaming three attacks on the Syrian government and a fourth on the Islamic State group. Syrian rebels and opposition activists say pro-government forces have used chemical weapons and bombs containing chlorine on numerous occasions. They say a chemical weapons attack on a town in northern Syria on Tuesday killed dozens of people. The Syrian government has denied ever using such weapons. Here is a timeline of events related to chemical weapons use in Syria. Aug. 20, 2012: U.S. President Barack Obama says the use of chemical weapons would be a &quot;red line&quot; that would change his calculus on intervening in the civil war and have &quot;enormous consequences.&quot; March 19, 2013: The Syrian government and opposition trade accusations over a gas attack that killed some 26 people, including more than a dozen government soldiers, in the town of Khan al-Assal in northern Syria. A U.N. investigation later finds that sarin nerve gas was used, but does not identify a culprit. Aug. 21, 2013: Hundreds of people suffocate to death in rebel-held suburbs of the Syrian capital, with many suffering from convulsions, pinpoint pupils, and foaming at the mouth. U.N. investigators visit the sites and determine that ground-to-ground missiles loaded with sarin were fired on civilian areas while residents slept. The U.S. and others blame the Syrian government, the only party to the conflict known to have sarin gas. Aug. 31, 2013: Obama says he will go to Congress for authorization to carry out punitive strikes against the Syrian government, but appears to lack the necessary support in the legislature. Sept. 27, 2013: The U.N. Security Council orders Syria to account for and destroy its chemical weapons stockpile, following a surprise agreement between Washington and Moscow, averting U.S. strikes. The Security Council threatens to authorize the use of force in the event of non-compliance. Oct. 14, 2013: Syria becomes a signatory to the Chemical Weapons Convention, prohibiting it from producing, stockpiling, or using chemical weapons. June 23, 2014: The Organization for the Prohibition of Chemical Weapons says it has removed the last of the Syrian government&#039;s chemical weapons. Syrian opposition officials maintain that the government&#039;s stocks were not fully accounted for, and that it retained supplies. Aug. 7, 2015: The U.N. Security Council authorizes the OPCW and U.N. investigators to probe reports of chemical weapons use in Syria, as reports circulate of repeated chlorine gas attacks by government forces against civilians in opposition-held areas. Chlorine gas, though not as toxic as nerve agents, can be classified as a chemical weapon depending on its use. Aug. 24, 2016: The joint OPCW-U.N. panel determines the Syrian government twice used helicopters to deploy chlorine gas against its opponents, in civilian areas in the northern Idlib province. A later report holds the government responsible for a third attack. The attacks occurred in 2014 and 2015. The panel also finds that the Islamic State group used mustard gas. Feb. 28, 2017: Russia, a stalwart ally of the Syrian government, and China veto a U.N. Security Council resolution authorizing sanctions against the Syrian government for chemical weapons use. April 4, 2017: At least 58 people are killed in what doctors say could be a nerve gas attack on the town of Khan Sheikhoun in the rebel-held Idlib province. Victims show signs of suffocation, convulsions, foaming at the mouth, and pupil constriction. Witnesses say the attack was carried out by either Russian or Syrian Sukhoi jets. Moscow and Damascus deny responsibility.
```

- Bug Number: 5
- "1.0.0-beta.6"
- Some Cnn headlines include <Strong> tags
```
====== 2017-04-02 08:46:05.132756 =======
=========================================
1. <strong>President Xi has closed scores of golf courses in China. He'll be at Mar-a-Lago this week.</strong>
2. Tapper:  Who can call out Trump on mistakes?
3. McCain: Trump doesn't measure up to Reagan
```

- Bug Number: 4
- "1.0.0-beta.6"
- Washington Post shows brackets in articles
```
earing because the topics are covered by the presidential communication privilege.
[
Read the letters from Sally Yates’s lawyer
]
Yates and other former intelligence officials had been asked to testify before the House Intelligence Committee this week, a hearing that was abruptly canceled by the panel’s chairman,

```
- Bug Number: 3
- "1.0.0-beta.6"
- Washington Post breaks when trying to open an article
```
7
Traceback (most recent call last):
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 128, in <module>
    main()
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 125, in main
    pick_article(service)
  File "/Users/michaelberber/sideProjects/commandlinenews/clnews.py", line 46, in pick_article
    wp.cl_news_util(['wp', '-r', command], cache['wp'])
  File "/Users/michaelberber/sideProjects/commandlinenews/services/wp.py", line 89, in cl_news_util
    htmlfile = utils.get_html_file(article['url'])
  File "/Users/michaelberber/sideProjects/commandlinenews/services/utils.py", line 44, in get_html_file
    uf = urllib.urlopen(url)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 87, in urlopen
    return opener.open(url)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 213, in open
    return getattr(self, name)(url)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 469, in open_file
    return self.open_local_file(url)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 483, in open_local_file
    raise IOError(e.errno, e.strerror, e.filename)
IOError: [Errno 2] No such file or directory: 'related'
```

# Archive

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
