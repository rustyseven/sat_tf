import pandas as pd

class KrxCrawler:
    def __init__(self):
        pass

    def scrap(self):
        code = pd.read_html(self.url, header='0')[0]
        print(code)