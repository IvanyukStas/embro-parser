import json

import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': '*/*'
    }

def get_category(url:str)-> dict:

    # resp = requests.get(url, headers)
    # with open('1.html', 'w') as f:
    #     f.write(resp.text)
    with open('1.html', 'r') as f:
        raw_data = f.read()
    category_dict = {}
    soup = BeautifulSoup(raw_data, 'lxml')
    for a  in soup.find('li', id="comp-j6uprizx0").find_all('a', attrs={'data-testid': "linkElement"})[1:]:
        category_dict[a.text] = a.get('href')
    print(category_dict)
    return category_dict

def get_category_items(url: str):
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        links = []
        for i, raw_link in enumerate(soup.find_all('a', class_="_20wJG")):
            links.append(raw_link.get('href'))
        return links


def get_content(url, category):
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    item_title = soup.find('h1', class_='_2qrJF').getText()
    item_article = soup.find('div', class_='_1rwRc').getText()
    item_price = soup.find('div', class_='_26qxh').find('span').getText().split(' ')
    item_description = soup.find('div', class_='_3cRjW').getText()
    item_image_url = soup.find('div', class_="_3j9OG media-wrapper-hook V-iTp").get('href')
    print(item_description)
    item_data = {
        'item-title': item_title,
        'item-price': item_price[0],
        'item-article': item_article,
        'item-description': item_description,
        'image-url': item_image_url,
        'item-category': category
    }
    return item_data

def main():
    url = 'https://www.embroplace.com/ru/embroidery-1'
    categories = get_category(url)
    category_items = []
    data_for_json = []
    for category, link in categories.items():
        category_items = get_category_items(link)
        for url in category_items:
           data_for_json.append(get_content(url, category))
    len(data_for_json)
    with open('data.json', 'w') as f:
        json.dump(data_for_json, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # main()
    with open('data.json', 'r') as r:
        data = json.load(r)
        for i, v in enumerate(data):
            print(i, v)
        print(len(data))