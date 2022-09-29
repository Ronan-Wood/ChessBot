from bs4 import BeautifulSoup
import requests

url="https://database.chessui.com"
page = requests.get(url)
#print(page) # We want 200-299 (Works)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('tr', class_="moves-row gane-moves")

move = lists.find('span', class_="simple-line")

print(move)