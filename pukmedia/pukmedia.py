import requests
from bs4 import BeautifulSoup


links = []
for link_gen in range(105067, 145031):
    url = "https://www.pukmedia.com/KS_Direje.aspx?Jimare=" + str(link_gen)
    links.append(url)


# url = requests.get("https://www.pukmedia.com/KS_Direje.aspx?Jimare=105067").text
# soup = BeautifulSoup(url, "lxml")
for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for i in soup.find_all("div", "span9 pull-right"):
        # print(i.text)
        with open("pukmedia.txt", "a", encoding="utf-8") as f:
            f.write(str(i.text) + "\n")
