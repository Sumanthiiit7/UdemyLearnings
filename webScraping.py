import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Battle_of_Hulao')
soup = bs4.BeautifulSoup(res.text, 'lxml')
variable = soup.select('title')
variable[0].getText()