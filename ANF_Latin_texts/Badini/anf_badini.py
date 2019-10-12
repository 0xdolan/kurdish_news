import requests
from bs4 import BeautifulSoup


# # ANF Badini - Kurdistan
# # generate page number links
# links = []
# for link in range(1, 1537):
#     gen_url = "https://anfkurdi.com/kurdistan?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             # links.append(link.get("href"))
#             with open("anf_badini_kurdistan_links.txt", "a", encoding="utf-8") as f:
#                 f.write(str(link.get("href")) + "\n")


# with open("anf_badini_kurdistan_links.txt", "r", encoding="utf-8") as f:
#     for link in f:
#         print(link)
#         url = requests.get(link).text
#         soup = BeautifulSoup(url, "lxml")
#         for text in soup.find_all("article", "post"):
#             # print(text.text)
#             with open("anf_badini_kurdistan.txt", "a", encoding="utf-8") as f:
#                 f.write(str(text.text) + "\n")


# # ANF Badini - Rojane
# # generate page number links
# links = []
# for link in range(1, 1605):
#     gen_url = "https://anfkurdi.com/rojane?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             # links.append(link.get("href"))
#             with open("anf_badini_rojane_links.txt", "a", encoding="utf-8") as f:
#                 f.write(str(link.get("href")) + "\n")


# with open("anf_badini_rojane_links.txt", "r", encoding="utf-8") as f:
#     for link in f:
#         print(link)
#         url = requests.get(link).text
#         soup = BeautifulSoup(url, "lxml")
#         for text in soup.find_all("article", "post"):
#             # print(text.text)
#             with open("anf_badini_rojane.txt", "a", encoding="utf-8") as f:
#                 f.write(str(text.text) + "\n")


# ANF Badini - Jin
# generate page number links
# links = []
# for link in range(1, 230):
#     gen_url = "https://anfkurdi.com/jin?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             # links.append(link.get("href"))
#             with open("anf_badini_jin_links.txt", "a", encoding="utf-8") as f:
#                 f.write(str(link.get("href")) + "\n")

# with open("anf_badini_jin_links.txt", "r", encoding="utf-8") as f:
#     for link in f:
#         print(link)
#         url = requests.get(link).text
#         soup = BeautifulSoup(url, "lxml")
#         for text in soup.find_all("article", "post"):
#             # print(text.text)
#             with open("anf_badini_jin.txt", "a", encoding="utf-8") as f:
#                 f.write(str(text.text) + "\n")


# # ANF Badini - Rojava
# # generate page number links
# links = []
# for link in range(1, 243):
#     gen_url = "https://anfkurdi.com/rojava-sUriye?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_rojava_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_rojava.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Badini - Civak
# # generate page number links
# links = []
# for link in range(1, 97):
#     gen_url = "https://anfkurdi.com/civak?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_civak_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_civak.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Badini - Cihan
# # generate page number links
# links = []
# for link in range(1, 779):
#     gen_url = "https://anfkurdi.com/cihan?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_cihan_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_cihan.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Badini - AnalIz
# # generate page number links
# links = []
# for link in range(1, 3):
#     gen_url = "https://anfkurdi.com/analIz?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_analIz_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_analIz.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Badini - Zanist
# # generate page number links
# links = []
# for link in range(1, 4):
#     gen_url = "https://anfkurdi.com/zanist?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_zanist_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_zanist.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# # ANF Badini - Ewropa
# # generate page number links
# links = []
# for link in range(1, 75):
#     gen_url = "https://anfkurdi.com/ewropa?page=" + str(link)
#     url = requests.get(gen_url).text
#     soup = BeautifulSoup(url, "lxml")
#     # parse the page links
#     for section in soup.find_all("section", id="last-news"):
#         for link in section.find_all("a"):
#             # print(link.get("href"))
#             links.append(link.get("href"))
#             # with open("anf_badini_ewropa_links.txt", "a", encoding="utf-8") as f:
#             #     f.write(str(link.get("href")) + "\n")

# for link in links:
#     print(link)
#     url = requests.get(link).text
#     soup = BeautifulSoup(url, "lxml")
#     for text in soup.find_all("article", "post"):
#         # print(text.text)
#         with open("anf_badini_ewropa.txt", "a", encoding="utf-8") as f:
#             f.write(str(text.text) + "\n")


# ANF Badini - Cand-U-huner
# generate page number links
links = []
for link in range(1, 89):
    gen_url = "https://anfkurdi.com/Cand-U-huner?page=" + str(link)
    url = requests.get(gen_url).text
    soup = BeautifulSoup(url, "lxml")
    # parse the page links
    for section in soup.find_all("section", id="last-news"):
        for link in section.find_all("a"):
            # print(link.get("href"))
            links.append(link.get("href"))
            # with open("anf_badini_cand-U-huner_links.txt", "a", encoding="utf-8") as f:
            #     f.write(str(link.get("href")) + "\n")

for link in links:
    print(link)
    url = requests.get(link).text
    soup = BeautifulSoup(url, "lxml")
    for text in soup.find_all("article", "post"):
        # print(text.text)
        with open("anf_badini_cand-U-huner.txt", "a", encoding="utf-8") as f:
            f.write(str(text.text) + "\n")
