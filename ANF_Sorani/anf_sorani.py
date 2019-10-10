import requests
from bs4 import BeautifulSoup


# # ANF Sorani - Kurdistan
# # generate page number links
# links = []
# for link in range(1, 176):
#     gen_url = (
#         "https://anfsorani.com/%DA%A9%D9%88%D8%B1%D8%AF%D8%B3%D8%AA%D8%A7%D9%86?page="
#         + str(link)
#     )
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_sorani_kurdistan.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Sorani - Jinan
# # generate page number links
# links = []
# for link in range(1, 20):
#     gen_url = "https://anfsorani.com/%DA%98%D9%86%D8%A7%D9%86?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_sorani_jinan.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")

# # ANF Sorani - World
# # generate page number links
# links = []
# for link in range(1, 90):
#     gen_url = "https://anfsorani.com/%D8%AC%DB%8C%D9%87%D8%A7%D9%86?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_sorani_world.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")

# # ANF Sorani - Rojava
# # generate page number links
# links = []
# for link in range(1, 32):
#     gen_url = (
#         "https://anfsorani.com/%DA%95%DB%86%DA%98%D8%A6%D8%A7%D9%88%D8%A7-%D9%88-%D8%B3%D9%88%D9%88%D8%B1%DB%8C%D8%A7?page="
#         + str(link)
#     )
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_sorani_rojava.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Sorani - Daily
# # generate page number links
# links = []
# for link in range(1, 136):
#     gen_url = "https://anfsorani.com/%DA%95%DB%86%DA%98%D8%A7%D9%86%DB%95?page=" + str(
#         link
#     )
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_sorani_daily.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# ANF Sorani - Hewrami
# generate page number links
links = []
for link in range(1, 32):
    gen_url = "https://anfsorani.com/%D9%87%DB%86%D8%B1%D8%A7%D9%85%DB%8C?page=" + str(
        link
    )
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))

for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_sorani_hewrami.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")


# ANF Sorani - Civak
# generate page number links
links = []
for link in range(1, 5):
    gen_url = "https://anfsorani.com/%D8%AC%DA%A4%D8%A7%D9%83?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))

for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_sorani_civak.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")
