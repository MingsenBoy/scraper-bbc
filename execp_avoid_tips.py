import requests
#import grequests
from bs4 import BeautifulSoup 
import time 


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(
    f"https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}",
    headers = headers, timeout = 5)

try:
    if response.status_code == 200:

        soup = BeautifulSoup(response.text,"lxml")

        titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})

        if titles:
            result = titles.getText()
            print(result)
        else:
            print("elements not found")

        # title_list = []
        # for title in titles:
        #     title_list.append(title.getText())
        #     #print(title.getText())

    else:
        print("status_code error")

except Exception:
    print(str(Exception))