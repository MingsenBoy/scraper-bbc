import requests

from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt',
                        headers = headers, timeout = 10)

#soup = BeautifulSoup(response.text, 'lxml')


try:
    if response.status_code == 200:

        soup = BeautifulSoup(response.text,"lxml")

        title = soup.find("a",{'class': 'bbc-uk8dsi e1d658bg0'})


        if title:
            result = title.getText()
            print(result)

        else:
            print("elements not found")


    else:
        print("status_code != 200")

except Exception:
    print(str(Exception))