# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

def down_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    response = requests.get(url, headers=headers)
    return response.text

def get_content(html):
    bf = BeautifulSoup(html, 'html.parser')
    bf_html = bf.find_all('div', class_ = 'article block untagged mb15 typs_hot')

    for i in bf_html:
        name = i.find("h2").string
        content = i.find("div", class_ = "content").get_text()
        save_text(name, content)


def save_text(name, content):
    with open('qiushi.txt', 'a', encoding='utf-8') as f:
        f.write(name+content)

def main():
    for i in range(1,13):
        url = "https://www.qiushibaike.com/text/page/{}".format(i)
        html = down_page(url)
        get_content(html)

if __name__ == '__main__':
    main()
