import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

for i in range(1, 60001):
    generate_url = 'http://www.westganews.net/dreja.aspx?=hewal&jmara=' + str(i) +'&Jor=1'
    logging.debug(i)
    url = requests.get(generate_url).text
    soup = BeautifulSoup(url, 'lxml')
    for i in soup.find_all('div', 'detail'):
        with open('new.txt', 'a', encoding='utf-8') as f:
            f.write(i.text)

##url = requests.get('http://www.westganews.net/dreja.aspx?=hewal&jmara=4&Jor=1').text
##soup = BeautifulSoup(url, 'lxml')
##
##for i in soup.find_all('div', 'detail'):
##    pattern = re.compile(r'([A-Za-z\u0600-\u06FF][^\.!?]*[\.!?])', re.M)
##    if pattern:
##        with open('new.txt', 'a', encoding='utf-8') as f:
##            result = re.findall(pattern, str(i.text))
##            for each_line in result:
##                f.write(each_line)

