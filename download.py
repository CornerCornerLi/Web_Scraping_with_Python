#pip install builtwith
import builtwith
import whois
import urllib2
import itertools
import re


def tellthetech(url):
    result = builtwith.parse(url)


def tellthedomain(url):
    itsdomain = whois.whois(url)

def download(url, user_agent='wswp',num_reties=2):
    print('Downloading:%s'%url)
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                #retry 5XX HTTP errors
                return downlaod(url, user_agent, num_retries - 1)
    return html

def craw_sitemap(url):
    #download the sitemap file
    sitemap = download(url)
    #extract the sitmap links
    links = re.findall('<loc>(.*?)', sitemap)
    #download each link
    for link in links:
        html = download(link)
        #scrape heml here
        #...
