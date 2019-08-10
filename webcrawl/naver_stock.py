from bs4 import BeautifulSoup
from urllib.request import urlopen
class StockModel:
    def __init__(self,item):
        self.item = item

    def scrap(self):
        url="https://finance.naver.com/item/sise_day.nhn?code=005930".format(code=self.item)
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        for i in soup.find_all(name='span', attrs=({'class':'tah p11'})):
            print('종가:'+str(i.text))