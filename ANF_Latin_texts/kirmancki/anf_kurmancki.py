import requests
from bs4 import BeautifulSoup


# # ANF Latini - Kurdistan
# # generate page number links
# links = []
# for link in range(1, 94):
#     gen_url = "https://anfkirmancki.com/kurdistan?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_kirmancki_kurdistan_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")


# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_kirmancki_kurdistan.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# ANF Latini - Aktuel
# generate page number links
links = []
for link in range(1, 71):
    gen_url = "https://anfkirmancki.com/aktuel?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_aktuel_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_aktuel.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - CinI
# generate page number links
links = []
for link in range(1, 27):
    gen_url = "https://anfkirmancki.com/cinI?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_cinI_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_cinI.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - Rojawan-sUrIye
# generate page number links
links = []
for link in range(1, 22):
    gen_url = "https://anfkirmancki.com/rojawan-sUrIye?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_rojawan-sUrIye_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_rojawan-sUrIye.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - Ewropa
# generate page number links
links = []
for link in range(1, 27):
    gen_url = "https://anfkirmancki.com/ewropa?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_ewropa_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_ewropa.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - Komel
# generate page number links
links = []
for link in range(1, 6):
    gen_url = "https://anfkirmancki.com/komel?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_komel_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_komel.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - CIhan
# generate page number links
links = []
for link in range(1, 11):
    gen_url = "https://anfkirmancki.com/cIhan?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_cIhan_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_cIhan.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - Kultur
# generate page number links
links = []
for link in range(1, 10):
    gen_url = "https://anfkirmancki.com/kultur?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_kultur_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_kultur.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Latini - Zanist
# generate page number links
links = []
for link in range(1, 2):
    gen_url = "https://anfkirmancki.com/zanist?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_kirmancki_zanist_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")


for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_kirmancki_zanist.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")
