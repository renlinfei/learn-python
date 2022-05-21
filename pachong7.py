from bs4 import BeautifulSoup
import requests

url = 'https://www.infoq.cn/news/'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

# class="article-item image-position-right with-label"

def crawl(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for news in soup.find_all('div', class_='article-item image-position-right with-label'):
        print([title.getText()
            for title in news.find_all('a', class_='com-article-title') if title.getText()
        ])

crawl(url)

print(requests.get(url, headers=headers).text)
