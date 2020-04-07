# -*- coding: utf-8 -*-

from urllib import  request


def download1(url):
    """Simple downloader"""
    # before
    #return urllib.urlopen(url).read()
    #after, using urllib.request instead
    print('Downloading--1')
    return request.urlopen(url)

from urllib import  request
def download2(url):
    """Download function that catches errors"""
    print('Downloading:%s'%url)
    print('Downloading--2')
    try:
        html = request.urlopen(url).read()
    except request.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
    return html
download2('http://example.webscraping.com')

def download3(url, num_retries=2):
    """Download function that also retries 5XX errors"""
    print('Downloading:%s'%url)
    print('Downloading--3')
    try:
        html = request.urlopen(url).read()
    except request.URLError as e:
        print('Download error:%s'% e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download3(url, num_retries-1)
    return html


def download4(url, user_agent='wswp', num_retries=2):
    """Download function that includes user agent support"""
    print('Downloading:%s'%url)
    print('Downloading--4')
    headers = {'User-agent': user_agent}
    requestnew = request.Request(url, headers=headers)
    try:
        html = request.urlopen(requestnew).read()
    except request.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download4(url, user_agent, num_retries-1)
    return html


def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print('Downloading:%s'%url)
    print('Downloading --- 5')
    headers = {'User-agent': user_agent}
    print(headers)
    print(url)
    requestnew = request.Request(url, headers=headers)
    opener = request.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(request.ProxyHandler(proxy_params))
    try:
        #html = opener.open(requestnew).read().decode('utf-8')
        htmlrsp = opener.open(requestnew)
        html = htmlrsp.read().decode('utf-8')

    except request.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download5(url, user_agent, proxy, num_retries-1)
    return html


download = download5


if __name__ == '__main__':
    print(download('http://example.webscraping.com'))


