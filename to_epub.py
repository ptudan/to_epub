#from bs4 import BeautifulSoup as bs
#from urllib.request import (urlopen, urlparse, urlunparse, urlretrieve)
from selenium import webdriver
import os
import sys

def main(url):

	driver = webdriver.PhantomJS()
	driver.get(url)
	print(driver)
	return
	soup=bs(urlopen(url), 'html.parser')
	print(soup.prettify)


def _usage():
    print("usage: python to_epub.py http://example.com ")

if __name__ == "__main__":
    url = sys.argv[-1]
    if not url.lower().startswith("http"):
        url = sys.argv[-2]
        if not url.lower().startswith("http"):
            _usage()
            sys.exit(-1)
    main(url)