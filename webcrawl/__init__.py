from webcrawl.bugsmusic import BugsCrawler

if __name__ == '__main__':
    bm = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
    bm.scrap()