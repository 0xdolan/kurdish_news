import requests
from bs4 import BeautifulSoup


links = []
for link_gen in range(1, 4429):
    url = "https://www.peyam.net/Details/" + str(link_gen)
    links.append(url)


# url = requests.get("https://www.peyam.net/Details/4424").text
# soup = BeautifulSoup(url, "lxml")
# for i in soup.find_all("div", "dreje_rast"):
#     print(i.text)

for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for i in soup.find_all("div", "dreje_rast"):
        # print(i.text)
        with open("peyam.txt", "a", encoding="utf-8") as f:
            f.write(str(i.text) + "\n")
