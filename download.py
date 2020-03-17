#pip install builtwith
import builtwith
import whois
import urllib2


def tellthetech(url):
    result = builtwith.parse(url)


def tellthedomain(url):
    itsdomain = whois.whois(url)

def download(urll):
    return urlib2.urlopen(url).read()


