from text_mining.model import SamsungReport
if __name__ == '__main__':
    sam = SamsungReport()
    #sam.download()
    #print(sam.extract_noun())
    #print(sam.read_stopword())
    #print(sam.remove_stopword())
    #print(sam.find_freq())
    print(sam.draw_wordcloud())
