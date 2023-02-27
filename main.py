from bs4 import BeautifulSoup
import requests

url = 'http://172.16.221.101/home.asp'
headers = {"Authorization": "Basic cm9vdDpyb290"}

r = requests.get(url, headers=headers)
texto = r.text
# soup = BeautifulSoup(texto, 'html.parser')
# title = soup.find_all('')
print(texto)