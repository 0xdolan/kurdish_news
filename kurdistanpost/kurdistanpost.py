import requests
from bs4 import BeautifulSoup


url = "https://www.kurdistanpost.nu/?mod=news&cid=1&p="
page_links = []
for i in range(1, 246):
    page_links.append(url + str(i))

for link in page_links:
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")

    for text in soup.find_all("div", "normal-news"):
        # print(text.text)
        with open("kurdistanpost_news.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")
