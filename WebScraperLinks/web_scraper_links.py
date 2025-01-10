
import requests
from bs4 import BeautifulSoup

print('\nStarting ...')

# url = 'https://www.arstechnica.com'
url = input('Enter url: ')

response = requests.get(url)

print(f"Status Code: {response.status_code}")
# print(response.text) 

if response.status_code >= 200 and response.status_code < 300:
    b_soup = BeautifulSoup(response.text, 'html.parser')
    all_links = b_soup.find_all('a')
    print(f"Total number of links: {len(all_links)}")
    for idx, link in enumerate(all_links):
        # href, text, title
        print(f"{idx + 1}. {link.text}")
        print(f"    href: {link.get('href')}")
        print(f"    title: {link.get('title')}")
else:
    print('Error getting web page.')

print('Done.')

