import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(
    filename="nns_file.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


url_list = []
for i in range(1, 200000):
    # for i in range(60400, 60548):
    url = "http://www.nnsroj.com/detiles.aspx?id=" + str(i)
    # url = "http://www.nnsroj.com/detiles.aspx?id=60548"
    r = requests.get(url)
    if r.status_code == 302:
        pass
    else:
        # print(r.url)
        if r.url == "http://www.nnsroj.com":
            pass
        else:
            logging.debug(r.url)
            with open("urls.txt", "a", encoding="utf-8") as f:
                f.write(str(r.url))
                f.write("\n")
