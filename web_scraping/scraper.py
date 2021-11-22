import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content,'html.parser')
    para_p = soup.find_all('span',text="citation needed")
    return len(para_p)

def get_citations_needed_report(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content,'html.parser')
    # para_div = soup.find('div',id='mw-content-text')
    para_p = soup.find_all('span',text = "citation needed")
    for p in para_p:
        parent = p.find_parent('p')
        print('*'*100)
        print(parent.get_text().strip())
        print('*'*100)
    # para_p = para_div.find_all('p')
    # for p in para_p:
    #     sp=p.find_all("span",text = "citation needed")
    #     if sp:
    #         for spam in sp:
    #             stri = f"{p.get_text().strip()}  {spam.get_text().strip()}"
    #             print('*'*100)
    #             print(stri)
    #             print('*'*100)

if __name__ == "__main__":
    link = "https://en.wikipedia.org/wiki/History_of_Mexico"
    # link = "https://en.wikipedia.org/wiki/Guitar"
    counter = get_citations_needed_count(link)
    print(counter)
    get_citations_needed_report(link)



