#!/usr/bin/python
import sys
import os
import re
import webbrowser
import urllib
from datetime import datetime


#Handle user quitting
def quit():
    print '\n================= Thanks for reading! ================='
    print '          ____ ____ ____ ____ ____ ____ ____ '
    print '         ||c |||o |||m |||m |||a |||n |||d ||'
    print '         ||__|||__|||__|||__|||__|||__|||__||'
    print '         |/__\|/__\|/__\|/__\|/__\|/__\|/__\|'
    print '   ____ ____ ____ ____ _________ ____ ____ ____ ____ '
    print '  ||l |||i |||n |||e |||       |||n |||e |||w |||s ||'
    print '  ||__|||__|||__|||__|||_______|||__|||__|||__|||__||'
    print '  |/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|'
    print '\n========================================================\n'
    sys.exit(1)

#handle usage errors
def handle_error(error_string):
    if error_string == 'cnn_error':
        print 'Usage: [--headlines -h] [--read -r][headline number] [--open -o][headline number]'
    if error_string == 'hn_error':
        print 'Usage: [--headlines -h] [--open -o][headline number] [--copy -cp][dest filename]'
    if error_string == 'ap_error':
        print 'Usage: [--headlines -h] [--read -r][headline number] [--open -o][headline number]'
    if error_string == 'guardian_error':
        print 'Usage: [--headlines -h] [--read -r][headline number] [--open -o][headline number]'
    sys.exit(1)

#Open page in Chrome
def go_to_page(url):
    print 'Opening: ' + url + ' in Chrome...'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

#Get HTML file
def get_html_file(url):
    uf = urllib.urlopen(url)
    return uf.read()

#Copies file to current directory
def copy_file(dest, htmlfile):
    currentdir = os.path.abspath('.')
    print 'Writing article to: ' + currentdir + dest
    writefile = open(currentdir + '/' + dest, 'w+')
    writefile.write(htmlfile)

#PRINT UTILITIES

#Print CLN Headline
def cl_news_headline():
    os.system('clear')
    print '\n================== Command Line News ==================\n'
    print '   CCCCCCCCCCCC    LLLLL           NNNNNN       NNNN'
    print '   CC              LL  L           NN    N      N  N'
    print '   CC  CCCCCCCC    LL  L           NN     N     N  N'
    print '   CC  C           LL  L           NN  NN  N    N  N'
    print '   CC  C           LL  L           NN  N N  N   N  N'
    print '   CC  C           LL  L           NN  N  N  N  N  N'
    print '   CC  CCCCCCCC    LL  LLLLLLLL    NN  N   N  N N  N'
    print '   CC              LL              NN  N    N  NN  N'
    print '   CCCCCCCCCCCC    LLLLLLLLLLLL    NN  N     N  N  N\n'

    print '\n\nWhat would you like to read?\n\n'
    # print '  Command Line News Twitter Feed => type: twits\n'
    print '  CNN => type: cnn\n'
    # print '  The Washington Post => type: wp\n'
    print '  The New York Times => type: nyt\n'
    print '  Associated Press => type: ap\n'
    # print '  The BBC => type: bbc\n'
    print '  Al Jazeera => type: aljaz\n'
    # print '  Reuters => type: re\n'
    print '  The Guardian => type: gu\n'
    print '  HackerNews => type: hn\n\n'
    print '  quit => type: quit\n\n'

#CLN prompt Print Util
def command_prompt():
    print '\nTo read an article enter the headline number.'
    print 'To go back to the main menu, type "main"'
    print 'To quit type quit.\n'

def read_more(service):
    print '\nTo read more from ' + service + ' type: "y".'
    print 'Type "main" to return to the Main Menu.'
    print 'To quit type "quit".\n'

#CNN Print Utility
def cnn_headlines(article_list):
    print '=========== Command Line News ===========\n'
    print '    _____   _____     _________      ___     '
    print '  /    __| |     \   |   ||     \   |   |    '
    print ' / / /     | |  \ \  | | || |  \ \  | | |    '
    print '| | |      | | \ \ \ | | || | \ \ \ | | |    '
    print '| | |      | | |\ \ \| | || | |\ \ \| | |    '
    print ' \ \ \_____| | | \ \ \ | || | | \ \ \ | |    '
    print '  \____________|  \______||___|  \______|    '
    print '           The most trusted name in news.    '
    print '\n========================================='
    print '============== CNN Headlines ============'
    print '====== ' + str(datetime.now()) + ' ======='
    print '========================================='
    i = 0
    while i < 25:
        print str(i + 1) + '. ' + article_list[i]['headline']
        i += 1

#HackerNews Print Utility
def hn_headlines(storylinks):
    print '======== Command Line News =========\n'
    print '===========yy========yy============='
    print '===========yy========yy============='
    print '============yy======yy=============='
    print '=============yy====yy==============='
    print '===============yyyyy================'
    print '=================yy================='
    print '================yy==combinator======'
    print '===============yy==================='
    print '=============yy=====================\n\n'
    print '===== HackerNews Headlines for ====='
    print '==== ' + str(datetime.now()) + ' ====\n'
    print '===================================='
    print '=HackerNews atricles open in Chrome='
    print '====================================\n'
    i = 0
    while i < len(storylinks):
        print str(i + 1) + '. ' + storylinks[i][1]
        i += 1

#Associated Press Print Utility
def ap_headlines(articlelist):
    print '======= Command Line News ========\n'
    print '==THE====AAA========PPPPPPP======='
    print '========AA=AA=======PP====PP======'
    print '=======AA===AA======PP====PP======'
    print '======AAAAAAAAA=====PPPPPPP======='
    print '=====AA=======AA====PP============'
    print '====AA=========AA===PP============'
    print '=== __________________________ ==='
    print '===|                          |==='
    print '===|__________________________|==='
    print '=================The Big Story.===\n\n'
    print '======== AP Headlines for ========'
    print '=== ' + str(datetime.now()) + ' ==='
    print '=================================='
    i = 0
    while i < len(articlelist):
        for article in articlelist:
            if articlelist[article]['index'] == i:
                print str(i + 1) + '. ' + articlelist[article]['title']
        i += 1

# The Guardian Headlines
def gu_headlines(articlelist):
    print '======= Command Line News ========\n'
    print '              gggggggg   ggggg    '
    print '           gggg       gg ggggg    '
    print '         gggg          ggggg      '
    print '         gggg            ggg      '
    print '         gggg            ggg      '
    print '         gggg           ggg       '
    print '           ggggggggggggggg        '
    print '             ggggggggggg          '
    print '          ggggg                   '
    print '           ggggggggggg            '
    print '              gggggggggggg        '
    print '       gggggg           gggg      '
    print '         ggg            gggg      '
    print '          gggggggggggggggg        '
    print '             gggggggggg           '
    print '==================================\n\n'
    print '===== The Guardian Headlines ====='
    print '=== ' + str(datetime.now()) + ' ==='
    print '=================================='
    i = 0
    while i < 25:
        for article in articlelist:
            if articlelist[article]['index'] == i:
                abbrevurl = articlelist[article]['url'][28:]
                # urldata = re.search(r'(.+?)/(.+?)/(.+?)/(.+?)/(.+)', abbrevurl)
                # section = urldata.group(1).split('-')
                # blurb = urldata.group(5).split('-')
                # details = section + blurb
                # print details
                print str(i + 1) + '. ' + articlelist[article]['title'] + ' -- ' + abbrevurl
        i += 1

# Reuters Headlines
def reuters_headlines(articlelist):
    print r"'||'''|,                   ||                        "
    print r" ||   ||                   ||                        "
    print r" ||...|' .|''|, '||  ||` ''||''  .|''|, '||''| ('''' "
    print r" || \\   ||..||  ||  ||    ||    ||..||  ||     `'') "
    print r".||  \\. `|...   `|..'|.   `|..' `|...  .||.   `...' "
    return

# Washington Post Headlines
def wp_headlines(articlelist):
    print r" ___"
    print r"-   ---___- ,,"
    print r"   (' ||    ||"
    print r"  ((  ||    ||/\\  _-_"
    print r" ((   ||    || || || \\"
    print r"  (( //     || || ||/"
    print r"   -____-   \\ |/ \\,/"
    print r"              _/"
    print r""
    print r" _                                                          "
    print r"- - /, /,              ,,                     ,              "
    print r"  )/ )/ )    _         ||     '         _    ||              "
    print r"  )__)__)   < \,  _-_, ||/\\ \\ \\/\\  / \\ =||=  /'\\ \\/\\ "
    print r" ~)__)__)   /-|| ||_.  || || || || || || ||  ||  || || || || "
    print r"  )  )  )  (( ||  ~ || || || || || || || ||  ||  || || || || "
    print r"  /-_/-_/   \/\\  ,-_- \\ |/ \\ \\ \\ \\_-|  \\, \\,/  \\ \\ "
    print r"                         _/            /  \                  "
    print r"                                      '----`                 "
    print r""
    print r"-__ /\\                ,  "
    print r"  ||  \\              ||  "
    print r" /||__||  /'\\  _-_, =||= "
    print r" \||__|| || || ||_.   ||  "
    print r"  ||  |, || ||  ~ ||  ||  "
    print r"_-||-_/  \\,/  ,-_-   \\, "
    print r"  ||                      "
    return

# Vice Headlines
def vice_headlines(articlelist):
    print " _   _ _            _   _                   "
    print "| | | (_)          | \ | |                  "
    print "| | | |_  ___ ___  |  \| | _____      _____ "
    print "| | | | |/ __/ _ \ | . ` |/ _ \ \ /\ / / __|"
    print "\ \_/ / | (_|  __/ | |\  |  __/\ V  V /\__ \\"
    print " \___/|_|\___\___| \_| \_/\___| \_/\_/ |___/"
    return

# BBC Headlines
def bbc_headlines(articlelist):
    print "88888888ba  88888888ba    ,ad8888ba,   "
    print "88       8b 88       8b  d8'      `8b  "
    print "88      ,8P 88      ,8P d8'            "
    print "88aaaaaa8P' 88aaaaaa8P' 88             "
    print "88      8b, 88      8b, 88             "
    print "88      `8b 88      `8b Y8,            "
    print "88      a8P 88      a8P  Y8a.    .a8P  "
    print "88888888P   88888888P     ` Y8888Y'   "
    print "================NEWS==================="
    return

# Al Jazeera Headlines
def aj_headlines(articlelist):
    print '============= Command Line News =================\n'
    print '================================================='
    print "                                                 "
    print ",---.|            |                              "
    print "|---||            |,---.,---,,---.,---.,---.,---."
    print "|   ||            |,---| .-' |---'|---'|    ,---|"
    print "`   '`---'    `---'`---^'---'`---'`---'`    `---^"
    print '=================================================\n\n'
    print '============= Al Jazeera Headlines =============='
    print '========== ' + str(datetime.now()) + ' =========='
    print '================================================='
    i = 0
    while i < len(articlelist):
        for article in articlelist:
            if articlelist[article]['index'] == i:
                print str(i + 1) + '. ' + articlelist[article]['title']
        i += 1

# NYTIMES Headlines
def nyt_headlines(articlelist):
    print '========================= Command Line News ========================\n'
    print '==The==============================================================='
    print '\n   __     __)           __     __)              ______)             '
    print '  (, /|  /             (, )   /        /)      (, /   ,             '
    print '    / | /   _ _   _      /   /  _____ (/_        /     ___    _  _  '
    print ' ) /  |/  _(/_(_(/      (___/_ (_)/ (_/(__    ) /   _(_// (__(/_/_)_'
    print '(_/                    )   /                 (_/                    '
    print '                      (__ /                                         \n'
    print '====================================================================\n\n'
    print '========================= NYT Headlines ============================'
    print '==================== ' + str(datetime.now()) + ' ===================='
    print '====================================================================\n\n'
    i = 0
    while i < len(articlelist):
        try:
            print str(i + 1) + '. ' + articlelist[i]['title']
        except:
            print ''
        i += 1

def main():
    return

if __name__ == '__main__':
    main()
