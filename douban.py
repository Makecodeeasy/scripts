#!/usr/bin/env python  
# -*- coding:utf-8 -*- 
# __author__ = 'yanzhengbin'
# __time__   = '2018/8/13 16:13'

import re
import urllib2
from bs4 import BeautifulSoup


def gen_url(url, pages):
    num = pages / 25 + 1
    url_list = [url.format(n*25) for n in range(num)]
    return url_list


def get_html(url):
    html = urllib2.urlopen(url)
    return html


def get_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    table_list = soup.find_all("table")
    if len(table_list) == 2:
        table = table_list[1]
        a_list = table.find_all("a")
        return a_list


def parse_a(li, filename):
    with open(filename, 'a+') as fp:
        for item in li:
            link = item.get("href", None)
            title = item.get("title", None)
            if title:
                ret = re.findall(u"学院路|古翠路|丰潭路|嘉绿|毛家桥|唐宁|南都花园|金都|恩济|紫桂|金城|德伽", title)
                if ret:
                    line = u"{0}  {1}\n\r".format(link, title)
                    fp.write(line.encode("utf8"))


def main():
    url1 = "https://www.douban.com/group/HZhome/discussion?start={0}"
    url2 = "https://www.douban.com/group/145219/discussion?start={0}"
    n = 0
    for base_url in (url1, url2):
        n += 1
        url_list = gen_url(base_url, 2000)
        for url in url_list:
            html = get_html(url)
            tmp_list = get_soup(html)
            parse_a(tmp_list, "rent{0}.txt".format(n))


if __name__ == '__main__':
    main()
