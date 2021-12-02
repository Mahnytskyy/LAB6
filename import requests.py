import requests 
from bs4 import BeautifulSoup
from array import *
r= requests.get("https://www.reddit.com/")
page= BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
ryadok1= page.head.title.text
ryadok2= page.body.text
words=ryadok2.split(' ')
unik_words=[]
for elem in words:
    if elem in unik_words:
        continue
    else:
        unik_words.append(elem)

L=len(unik_words)
Numbers=array('i',[])
n=0
for elem in unik_words:
    n=words.count(elem)
    Numbers.append(n)

print(unik_words[16],' '.numbers[16])