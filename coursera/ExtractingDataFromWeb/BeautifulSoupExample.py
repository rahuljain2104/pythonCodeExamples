import urllib
from BeautifulSoup import *

lnk = "http://python-data.dr-chuck.net/known_by_Caroline.html"


# "http://python-data.dr-chuck.net/known_by_Fikret.html"


def find_link(url, position):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags[position].get('href', None)


#
depth = 8
pos = 17
for i in range(depth):
    print lnk
    lnk = find_link(lnk, pos)


    # import urllib
    # from BeautifulSoup import *
    #
    # train = "http://python-data.dr-chuck.net/comments_42.html"
    # test = "http://python-data.dr-chuck.net/comments_340271.html"
    #
    #
    # def find_sum_of_number_in_html(link):
    #     html = urllib.urlopen(link).read()
    #     soup = BeautifulSoup(html)
    #
    #     nums = soup('span')
    #     s = 0
    #
    #     for num in nums:
    #         s += int(num.text)
    #     return s
    #
    #
    # print find_sum_of_number_in_html(test)
