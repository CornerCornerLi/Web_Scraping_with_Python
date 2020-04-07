# -*- coding: utf-8 -*-
import re
import time
from common import download


def link_crawler(seed_url, link_regex):
    """
    Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    print(crawl_queue)
    time.sleep(2)
    while crawl_queue:
        url = crawl_queue.pop()
        print(url)
        time.sleep(1)
        print('url is : %s'%url)
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(link)


def get_links(html):
    """
    Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    print('get_links')
    return webpage_regex.findall(html)
    

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)')
