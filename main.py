import requests
from bs4 import BeautifulSoup
import urllib
import time

def get_html(url):
    request = requests.get(url)
    return False if request.status_code == 404 else request.text

def main():

    soup = BeautifulSoup(get_html("https://www.nvidia.com/ru-ru/geforce/graphics-cards/30-series/rtx-3050/"), 'lxml')
    src = soup.text
    objBuyBtn = src.find_all(class_="partners").find('a')
    print(objBuyBtn.text)
    # if(objBuyBtn.text.replace('  ', '').replace('\n', '').replace('\t', '').strip().lower() == 'сообщите мне'):
    #       print("Видеокарта RTX 3050 недоступна для покупки")
    #     # get_html("https://api.telegram.org/bot1540937288:AAEp5-YpjImIo-YiBgGVIXNEv38-LqZDVmA/sendMessage?chat_id=849685423&text=" + urllib.parse.quote("Видеокарта RTX 3050 недоступна для покупки"))
    # else:
    #     #print("Видеокарта RTX 3070 доступна для покупки")
    #     get_html(
    #         "https://api.telegram.org/bot1540937288:AAEp5-YpjImIo-YiBgGVIXNEv38-LqZDVmA/sendMessage?chat_id=849685423&text=" + urllib.parse.quote(
    #             "Видеокарта RTX 3050 доступна для покупки"))

if __name__ == '__main__':
    main()
    while 1:
        main()
        time.sleep(10)