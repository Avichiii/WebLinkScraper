import requests
from bs4 import BeautifulSoup


def get_link(url_link):
    url = url_link #<---- enteres the web address you want to fetch links from!

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    anchors = soup.find_all('a')

    all_links = set(anchors)

    with open('output.txt', 'w') as f:
        f.write('<-----All Links:----->\n')

    for link in all_links:
        with open('output.txt', 'a') as f:
            if(link.get('href') != '#'):
                new_links = ''
        
                if(link.get('href').startswith('/')):
                    new_links = url_link + link.get('href') #<---- enteres the web address you want to fetch links from!
                    # print(new_links)

                if(link.get('href').startswith(url_link)): #<---- enteres the web address you want to fetch links from!
                    new_links = link.get('href')
                    # print(new_links)

                store_links = f.write(new_links + '\n')
    
    return store_links


web_url = input("Enter a web address: ")

get_link(web_url)


