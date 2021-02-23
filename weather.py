import requests
from bs4 import BeautifulSoup

x = input("enter the location:")
search ="weather in {}"+ x

url =f"http://www.google.com/search?&q={search}"

r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")

update = s.find("div",class_="BNeawe").text

print(update)
