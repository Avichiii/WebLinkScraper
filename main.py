import requests
from bs4 import BeautifulSoup


def get_link(url_link):
    url = url_link #<---- enter the web address you want to fetch links from!

    r = requests.get(url)
    print(r.status_code)

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
                    new_links = url_link + link.get('href') #<---- enter the web address you want to fetch links from!
                    # print(new_links)

                if(link.get('href').startswith(url_link)): #<---- enter the web address you want to fetch links from!
                    new_links = link.get('href')
                    # print(new_links)
        
                store_links = f.write(new_links + '\n')
    
    return 1 #<---- means we are returning True


web_url = input("Enter a web address: ")

mod_url = f"https://{web_url}"


get_link(mod_url)


