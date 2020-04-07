# -*- coding: utf-8 -*-

from urllib import request


def download(url, user_agent=None):
    print('Downloading:%s'%url)
    headers = {'User-agent': user_agent or 'wswp'}
    newrequest = request.Request(url, headers=headers)
    try:
        html = request.urlopen(newrequest).read()
    except request.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
    return html


if __name__ == '__main__':
    print(download('http://example.webscraping.com'))

