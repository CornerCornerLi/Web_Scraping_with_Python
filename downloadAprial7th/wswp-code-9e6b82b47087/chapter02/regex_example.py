# -*- coding: utf-8 -*-

from urllib import request
import re


def scrape(html):
    area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
    return area


if __name__ == '__main__':
    html = request.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
    print(scrape(html))
