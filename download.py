#pip install builtwith
import builtwith
import whois
import urllib2


def tellthetech(url):
    result = builtwith.parse(url)


def tellthedomain(url):
    itsdomain = whois.whois(url)

def download(urll):
    print('Downloading:%s'%url)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print('Download error:%s'%e.reason)
        html = None
    return html


