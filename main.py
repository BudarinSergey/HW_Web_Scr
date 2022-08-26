import requests
import bs4


KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'ПК', 'ваш', 'Path'}

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1646070523; _ym_uid=1590416197797180666; _ga=GA1.2.12282187.1646070523; fl=ru; hl=ru; __gads=ID=6c8dc47f727e9350:T=1646117789:S=ALNI_Mb5Nxxd3P9rmrvoK9me-14u6mkIIQ; habr_web_home_feed=/all/; _gid=GA1.2.1508794189.1661456291; _ym_isad=2; visited_articles=684148:531472',
'Host': 'habr.com',
'Referer': 'https://habr.com/ru/all/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36}'}




response = requests.get('https://habr.com/ru/all/' , headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-article-snippet")


for article in articles:
    article_text = article.find('h2').find('a')
    hub_set = set(article_text.text.split())
    # print(article_text)


    if KEYWORDS & hub_set:
        date = article.find('time').text
        title = article.find('h2').find('a').text
        print(title)
        href = article_text.attrs['href']
        url = 'https://habr.com' + href
        print(f'Дата: {date} - Заголовок: {title}   Ссылка: {url}')


