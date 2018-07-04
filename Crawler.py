#Custom crawler is required for diferent websites unless using open source


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

main_url = 'https://cointelegraph.com/tags/cryptocurrencies'
client = uReq(main_url)
page = client.read()
client.close()  

page_contents= soup(page, "html.parser")

#container = page_contents.findAll("div",{"class":"row result"})


urls = []
for data in page_contents.find_all("div", {"class":"row result"}): # crawler is built to accomodate a specific website
    for a in data.find_all("h2", {"class":"header"}):
        for i in a.find_all("a"):
            urls.append(i.get("href"))

file = open('datasheet.txt', 'w') #done to prevent excessive website scrapping as the acess can be denied (Error 403)

for i in urls:
  file.write("%s\n" % i)


print(len(urls)) # urls





