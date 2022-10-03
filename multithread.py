import requests
from bs4 import BeautifulSoup 
import time
import concurrent.futures   

def scrape(links):

    response = requests.get(links)

    soup = BeautifulSoup(response.text,"lxml")

    titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})
    title_list = []
    for title in titles:
        title_list.append(title.getText())
        #print(title.getText())
        titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})
        title_list = []
        for title in titles:
            title_list.append(title.getText())
            #print(title.getText())

    urls = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})

    # tag_list = []
    # for url in urls:
    #     #print(url.get('href'))
    #     sub_response = requests.get(url.get('href'))
    #     sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    #     tags = sub_soup.find_all("li",{'class':'bbc-1msyfg1 e2o6ii40'})
    #     for tag in tags:
    #         #print(tag.find("a").getText())
    #         tag_list.append(tag.find("a").getText())
    #         #print(tag.getText())

    urls = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})
    tag_list = []
    for url in urls:
        #print(url.get('href'))
        sub_response = requests.get(url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all("li",{'class':'bbc-1msyfg1 e2o6ii40'})
        for tag in tags:
            #print(tag.find("a").getText())
            tag_list.append(tag.find("a").getText())
            #print(tag.getText())
        #print(f"第{page}頁")
    print(title_list)
    print(tag_list)


start_time = time.time()

links = [f"https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}"for page in range(1,4)]

with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
    executor.map(scrape, links)

end_time = time.time()
 
print(f"花費{end_time - start_time}")