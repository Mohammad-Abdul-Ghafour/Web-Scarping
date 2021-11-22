import requests
from bs4 import BeautifulSoup
from lxml import html


# URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
# res = requests.get(URL)
# tree = html.fromstring(res.text)
with open('web_scraping/res.html','r') as f:
    res = f.read()
# print(res)
# print(res)
soup = BeautifulSoup(res,'html.parser')
# print(soup)
# with open('res.html' , 'w') as f:
#     f.write(res.text)
para_div = soup.find('div',id='mw-content-text')
para_p = para_div.find_all('p')

counter = 0
for p in para_p:
    sp=p.find_all("span")
    
    if sp:
        for iner in sp:
            # print(iner.get_text().strip())
            counter += 1
        # if p.children:
        #     print("*"*100)
        #     print(p)
        #     print("*"*100)
print(counter)


def get_citations_needed_count(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content,'html.parser')
    para_div = soup.find('div',id='mw-content-text')
    para_p = para_div.find_all('p')
    counter = 0
    for p in para_p:
        sp=p.find_all("span")
        if sp:
            for spam in sp:
                counter += 1
    return counter

def get_citations_needed_report(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content,'html.parser')
    para_div = soup.find('div',id='mw-content-text')
    para_p = para_div.find_all('p')
    for p in para_p:
        sp=p.find_all("span",text = "citation needed")
        if sp:
            for spam in sp:
                stri = f"{p.get_text().strip()}  {spam.get_text().strip()}"
                print('*'*100)
                print(stri)
                print('*'*100)