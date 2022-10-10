import requests
#import grequests
from bs4 import BeautifulSoup 
import time 


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(
    "https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt?page=1",
    headers = headers, timeout = 10)

try:
    if response.status_code == 200:

        soup = BeautifulSoup(response.text,"lxml")

        titles = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})


        if titles:
            for title in titles:
                result = title.getText()
                print("scraper function running sucessfully")
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



# import requests
# #import grequests
# from bs4 import BeautifulSoup 
# #import time 


# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
# }

# response = requests.get(
#     "https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt?page=1",
#     headers = headers, timeout = 10)

# print(response.status_code)

# soup = BeautifulSoup(response.text,"lxml")

# titles = soup.find_all("a",{'class': 'bbc-uk8dsi e1d658bg0'})

# #if titles:

# for title in titles:    
#     print(title.getText())