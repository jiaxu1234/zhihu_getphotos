#coding:utf-8
import requests
from lxml import etree
import os
import re

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def get_urls(url):
    response = requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36' })
    content = response.content
    print content
    tree = etree.HTML(content)
    # image_all = tree.xpath('''//div[@class="zm-editable-content clearfix"]/img/@data-original''')
    image_all = tree.xpath('''//div[@class="RichContent-inner"]//img/@data-original''')
    global name
    # name = tree.xpath('''//span[@class="zm-editable-content"]/text()''')
    name = url.split("/")[-1]
    if not name:
        name = "jx"
    url_list = []
    for url in image_all:
        url_list.append(url)
        # print url
    print '----totle number', len(url_list)

    return url_list

def get_photos(url):
    url_list = get_urls(url)
    n = 1
    for url in url_list:
        print url
        response = requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20' })
        content = response.content
        cd = mkdir()
        with open(cd + '/' + url[-11:], 'wb') as code:
            code.write(content)
        print "download ok --", n
        n += 1


def mkdir():
    path = sys.path[0]
    if not os.path.exists(path + r'\%s'%name):
        os.makedirs(path + r'\%s'%name)
    os.chdir(path + r'\%s'%name)

    cd = os.getcwd()

    return cd



if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/22046806'
    url = 'https://www.zhihu.com/question/49364343'
    get_photos(url)