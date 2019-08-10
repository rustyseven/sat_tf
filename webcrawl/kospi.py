from bs4 import BeautifulSoup
import urllib.request as url

class KospiCrawler:
    def __init__(self, param):
        self.param = param

    def scrap(self):
        html = url.urlopen(self.param).read()
        soup = BeautifulSoup(html, 'html.parser')
        #ksp = soup.find(id="KOSPI_now", attrs=({'class':'num'}))
        #print(ksp)
        for i in soup.find_all(id='KOSPI_now', attrs=({'class':'num'})):
            print('KOSPI:'+str(i.text))