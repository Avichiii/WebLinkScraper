import requests
from bs4 import BeautifulSoup


def get_link(url_link):
    try:
        r = requests.get(url_link)
        print(r.status_code)
        soup = BeautifulSoup(r.content, 'lxml')
        anchors = soup.find_all('a')

        for link in anchors:
            if 'href' in link.attrs:
                if link['href'].startswith('/'):
                    with open('links.txt', 'a') as f:
                        f.write(url_link + link['href'] + '\n')
                        f.write('\n')
                else:
                    with open('links.txt', 'a') as f:
                        f.write(link['href'] + '\n')
                        f.write('\n')    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    web_url = input("Enter a web address: ")
    get_link(f"https://www.{web_url}")





