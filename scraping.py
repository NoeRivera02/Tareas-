import requests
import csv
from bs4 import BeautifulSoup

page = requests.get("https://parascrapear.com/")
soup = BeautifulSoup(page.text, "html.parser")

blockquote_items = soup.find_all("blockquote")
lista1 = []
for blockquote in blockquote_items:
    for i in range(0,1):
        autor = blockquote.find(class_="author").text
        categoria = blockquote.find(class_="cat").text
        frase = blockquote.find("q").text
        lista = [autor, categoria, frase]
        lista1.append(lista)
    
        print([autor, categoria, frase])
with open("datos.csv","w",newline="") as file:
        writer = csv.writer(file ,delimiter=";")
        writer.writerows(lista1)
        

