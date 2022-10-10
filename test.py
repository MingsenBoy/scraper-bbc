#import requests
import grequests
from bs4 import BeautifulSoup 
import time 

start_time = time.time()

links = [f"https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}" for page in range(1,4)]

#g_response = (grequests.get(link) for link in links)
g_response = grequests.imap((grequests.get(link) for link in links), grequests.Pool(3))

for index, res in enumerate(g_response):
    soup = BeautifulSoup(res.text,"lxml")

    titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})
    title_list = []
    for title in titles:
        title_list.append(title.getText())
        #print(title.getText())


    urls = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})

    sub_links = [url.get('href') for url in urls]
    sub_responses = grequests.imap((grequests.get(sub_link) for sub_link in sub_links), grequests.Pool(10))

    tag_list = []
    for sub_response in sub_responses:
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all("li",{'class':'bbc-1msyfg1 e2o6ii40'})
        for tag in tags:
            tag_list.append(tag.getText())

    print(f"第{index+1}頁")
    print(title_list)
    print(tag_list)

ent_time = time.time()
print(f"耗時{ent_time - start_time}秒")

# for page in range(1,4):
#     response = requests.get(
#         f"https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}")

#     soup = BeautifulSoup(response.text,"lxml")

#     titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})
#     title_list = []
#     for title in titles:
#         title_list.append(title.getText())
#         #print(title.getText())


#     urls = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})
#     tag_list = []
#     for url in urls:
#         #print(url.get('href'))
#         sub_response = requests.get(url.get('href'))
#         sub_soup = BeautifulSoup(sub_response.text, 'lxml')
#         tags = sub_soup.find_all("li",{'class':'bbc-1msyfg1 e2o6ii40'})
#         for tag in tags:
#             #print(tag.find("a").getText())
#             tag_list.append(tag.find("a").getText())
#             #print(tag.getText())
#     print(f"第{page}頁")
#     print(title_list)
#     print(tag_list)

# ent_time = time.time()
# print(f"耗時{ent_time - start_time}秒")