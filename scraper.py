import requests
from bs4 import BeautifulSoup 

response = requests.get(
    "https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt")

soup = BeautifulSoup(response.text,"lxml")
titles = soup.find_all("h2",{'class': 'bbc-19hmebw e47bds20'})
#print(titles)

title_list = []
for title in titles:
    title_list.append(title.getText())
    #print(title.getText())
print(title_list)
#print(response.text.find("香港疫情管控放鬆：「壓力山大」的特區政府宣佈與世界恢復通關"))