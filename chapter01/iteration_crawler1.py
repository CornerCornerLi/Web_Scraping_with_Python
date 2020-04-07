# -*- coding: utf-8 -*-

import itertools
import time
from common import download


def iteration():
    for page in itertools.count(1):
        print('iteration function, page is:%s'%page)
        time.sleep(5)
        #url = 'http://example.webscraping.com/view/-{}'.format(page)
        url = 'http://example.webscraping.com/places/default/index/{}'.format(page)
        print('url is %s'%url)
        html = download(url)
        if html is None:
                # received an error trying to download this webpage
                # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass

if __name__ == '__main__':
    iteration()

