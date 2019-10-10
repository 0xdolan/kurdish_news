import re
import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(
    filename="textlinks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

with open("urls.txt", "r", encoding="utf-8") as f:
    for link in f:
        ##        print(link)
        ##    url = requests.get('http://www.nnsroj.com/detiles.aspx?id=74').text
        url = requests.get(link).text
        soup = BeautifulSoup(url, "lxml")
        for body in soup.find_all("div", "container body-content"):
            ##    print(body.text)
            with open("nnsroj.txt", "a", encoding="utf-8") as f:
                f.write(body.text)
                f.write("\n")
