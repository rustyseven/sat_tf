from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsCrawler:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')