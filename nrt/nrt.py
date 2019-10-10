import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")


### GENERATING THE "links.txt" FILE
##for link in range(1, 19113):
##    generate_link = 'http://www.nrttv.com/News.aspx?id=' + str(link) + '&MapID=1'
##    with open('links.txt', 'a', encoding = 'utf-8') as f:
##        f.write(generate_link)
##        f.write('\n')
        
with open('links_5995.txt', 'r', encoding = 'utf-8') as f:
    for each_link in f:
        logging.debug(each_link)
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(each_link, headers=headers, verify=False).text
        soup = BeautifulSoup(r, 'lxml')
        for i in soup.find_all('div', 'detail'):
            for para in i.find_all('p'):
        ##        print(para.text)
                para = para.text
##                print(para)
                with open('texts.txt', 'a', encoding = 'utf-8') as f:
                    f.write(str(para))
                    f.write('\n')
